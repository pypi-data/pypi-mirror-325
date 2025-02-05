"""Base class for clients"""

import logging
from pathlib import Path
from typing import Any

from google.auth.external_account_authorized_user import (
    Credentials as ExternalAccountCredentials,
)
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import Resource, build

from gaclw.core.config import settings
from gaclw.utils import logger as default_logger


class Singleton:
    _INSTANCE: dict[object, Any] = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._INSTANCE:
            cls._INSTANCE[cls] = super().__new__(cls)
        return cls._INSTANCE[cls]


class ApiClientBase(Singleton):
    """Base class for clients"""

    # https://developers.google.com/drive/api/guides/api-specific-auth
    # https://developers.google.com/sheets/api/scopes?hl=ja
    def __init__(
        self,
        service_name: str,
        version: str,
        oauth_credentials: str = settings.OAUTH_CREDENTIALS_FILE_PATH,
        oauth_token: str = settings.OAUTH_TOKEN_FILE_PATH,
        scopes: list[str] = settings.SCOPES,
        logger: logging.Logger = default_logger,
    ):
        if not hasattr(self, "initialized"):
            self._logger = logger
            self._credentials = self.authenticate(oauth_credentials, oauth_token, scopes)
            self._service = build(service_name, version, credentials=self._credentials)
            self.initialized = True

    @property
    def logger(self) -> logging.Logger:
        """_summary_

        Returns:
            logging.Logger: _description_
        """
        return self._logger

    @property
    def service(self) -> Resource:
        """_summary_

        Returns:
            Resource: _description_
        """
        return self._service

    @classmethod
    def authenticate(
        cls, credentials_file: str, token_file: str, scopes: list[str]
    ) -> Credentials | ExternalAccountCredentials:
        """_summary_

        Args:
            scopes (list[str]): _description_

        Returns:
            Credentials | ExternalAccountCredentials: _description_
        """
        credentials = None
        credentials_file_path = Path(credentials_file)
        token_file_path = Path(token_file)
        if token_file_path.exists():
            credentials = Credentials.from_authorized_user_file(token_file_path, scopes)

        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_file_path, settings.SCOPES
                )
                credentials = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_file_path, "w", encoding="utf-8") as token:
                token.write(credentials.to_json())
        return credentials
