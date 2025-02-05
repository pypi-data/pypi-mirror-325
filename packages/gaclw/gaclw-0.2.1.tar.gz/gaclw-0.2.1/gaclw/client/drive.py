"""define GoogleDriveApiClient class"""

import logging
import pathlib
from typing import Literal, TypedDict

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from gaclw.client.base import ApiClientBase


Role = Literal["owner", "organizer", "fileOrganizer", "writer", "commenter", "reader"]


class Permission(TypedDict):
    """Permission type definition"""

    id: str
    type: Literal["user", "group", "domain", "anyone"]
    kind: Literal["drive#permission"]
    role: Role


class DriveApiClient(ApiClientBase):
    """Google Drive API client"""

    def __init__(self, oauth_credentials: str, oauth_token: str, logger: logging.Logger):
        super().__init__(
            service_name="drive",
            version="v3",
            oauth_credentials=oauth_credentials,
            oauth_token=oauth_token,
            logger=logger,
        )
        self._files = self.service.files()  # type: ignore
        self._permissions = self.service.permissions()  # type: ignore

    @property
    def files(self):
        return self._files

    @property
    def permissions(self):
        return self._permissions

    def find_folder(
        self, folder_name: str, parent_folder_id: str | None = None
    ) -> str | None:
        """Find folder by name and parent folder ID in Google Drive."""
        query = (
            f"name='{folder_name}'"
            + " and trashed=false"
            + " and mimeType='application/vnd.google-apps.folder'"
        )
        if parent_folder_id:
            query += f" and '{parent_folder_id}' in parents"
        results = self.files.list(
            q=query,
            fields="files(id, name)",
            supportsTeamDrives=True,
            includeItemsFromAllDrives=True,
        ).execute()

        try:
            items: list[dict[str, str]] = results.get("files", [])
            self.logger.warning(
                "Found multiple folders with the same name: %s", folder_name
            )
            for item in results.get("files", []):
                self.logger.debug("Found folder: %s (ID: %s)", item["name"], item["id"])
            return next(i["id"] for i in items)
        except StopIteration:
            self.logger.warning("No folder found with the name: %s", folder_name)
            return None

    def _find_file(
        self, file_name: str, parent_folder_id: str | None = None
    ) -> str | None:
        query = (
            f"name='{file_name}'"
            + " and trashed=false"
            + " and mimeType!='application/vnd.google-apps.folder'"
        )
        if parent_folder_id:
            query += f" and '{parent_folder_id}' in parents"
        results = self.files.list(
            q=query,
            fields="files(id, name)",
            supportsTeamDrives=True,
            includeItemsFromAllDrives=True,
        ).execute()

        try:
            items: list[dict[str, str]] = results.get("files", [])
            self.logger.warning("Found multiple files with the same name: %s", file_name)
            for item in results.get("files", []):
                self.logger.debug("Found file: %s (ID: %s)", item["name"], item["id"])
            return next(i["id"] for i in items)
        except StopIteration:
            self.logger.warning("No file found with the name: %s", file_name)
            return None

    def upload_file(
        self, file_path: pathlib.Path, parent_folder_id: str | None
    ) -> str | None:
        """Upload file to Google Drive."""
        metadata = {
            "name": file_path.name,
            "parents": [] if parent_folder_id is None else [parent_folder_id],
        }
        media = MediaFileUpload(file_path, resumable=True)

        try:
            existing_id = self._find_file(file_path.name, parent_folder_id)
            if existing_id:
                _ = metadata.pop("parents")
                uploaded_file: dict[str, str] = self.files.update(
                    fileId=existing_id,
                    body=metadata,
                    media_body=media,
                    removeParents=f"{parent_folder_id}",
                    addParents=f"{parent_folder_id}",
                    supportsTeamDrives=True,
                ).execute()
                self.logger.info(
                    "Updated file: %s with ID: %s",
                    file_path.name,
                    uploaded_file.get("id"),
                )
            else:
                uploaded_file = self.files.create(
                    body=metadata,
                    media_body=media,
                    fields="id",
                    supportsTeamDrives=True,
                ).execute()
                self.logger.info(
                    "Uploaded file: %s with ID: %s",
                    file_path.name,
                    uploaded_file.get("id"),
                )
            return uploaded_file.get("id")
        except HttpError as error:
            self.logger.error("An error occurred: %s", error)
            return None

    def create_folder(
        self, folder_name: str, parent_folder_id: str | None = None
    ) -> str | None:
        """Create folder in Google Drive."""
        metadata = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [] if parent_folder_id is None else [parent_folder_id],
        }
        try:
            existing_id = self.find_folder(folder_name, parent_folder_id)
            if existing_id:
                _ = metadata.pop("parents")
                created_folder: dict[str, str] = self.files.update(
                    fileId=existing_id,
                    body=metadata,
                    removeParents=f"{parent_folder_id}",
                    addParents=f"{parent_folder_id}",
                    supportsTeamDrives=True,
                ).execute()
                self.logger.info(
                    "Updated folder: %s with ID: %s",
                    folder_name,
                    created_folder.get("id"),
                )
            else:
                created_folder = self.files.create(
                    body=metadata, fields="id", supportsTeamDrives=True
                ).execute()
                self.logger.info(
                    "Created folder: %s with ID: %s",
                    folder_name,
                    created_folder.get("id"),
                )
        except HttpError as error:
            self.logger.error("An error occurred: %s", error)
            return None
        else:
            return created_folder.get("id", "NA")

    def get_permissions(self, file_id: str) -> list[Permission]:
        """Get permissions of file in Google Drive."""
        permissions: dict = self.permissions.list(
            fileId=file_id, supportsAllDrives=True
        ).execute()
        return permissions.get("permissions", [])

    def delete_permission(self, file_id: str, permission_id: str) -> None:
        """Delete specified permissions from file in Google Drive."""
        self.permissions.delete(fileId=file_id, permissionId=permission_id).execute()

    def create_permission(self, file_id: str, email: str, role: Role) -> None:
        """Create permission for file in Google Drive."""
        permission = {
            "role": role,
            "type": "user",
            "emailAddress": email,
        }
        self.permissions.create(
            fileId=file_id,
            body=permission,
            sendNotificationEmail=False,
            supportsAllDrives=True,
        ).execute()
        self.logger.info(
            "Created permission: %s with role: %s for file ID: %s",
            email,
            role,
            file_id,
        )
