"""client module"""

from gaclw.client.drive import DriveApiClient
from gaclw.client.spreadsheet import SpreadsheetsApiClient
from gaclw.core.config import settings
from gaclw.utils import logger


class ClientWrapper:
    def __init__(self):
        self._drive = DriveApiClient(
            settings.OAUTH_CREDENTIALS_FILE_PATH,
            settings.OAUTH_TOKEN_FILE_PATH,
            logger,
        )
        self._spreadsheets = SpreadsheetsApiClient(
            settings.OAUTH_CREDENTIALS_FILE_PATH,
            settings.OAUTH_TOKEN_FILE_PATH,
            logger,
        )

    @property
    def drive(self) -> DriveApiClient:
        return self._drive

    @property
    def spreadsheets(self) -> SpreadsheetsApiClient:
        return self._spreadsheets


wrapper = ClientWrapper()
