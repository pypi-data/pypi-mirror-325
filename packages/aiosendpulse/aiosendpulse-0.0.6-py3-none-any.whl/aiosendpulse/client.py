from __future__ import annotations

from http import HTTPStatus
from typing import Literal, Union

from httpx import URL, AsyncClient, HTTPError, HTTPStatusError, Request, Response

from aiosendpulse.auth import BearerTokenAuth
from aiosendpulse.logger import logger
from aiosendpulse.methods import Authorize
from aiosendpulse.services.email import EmailService
from aiosendpulse.services.smtp import SmtpService
from aiosendpulse.storage.base import BaseTokenStorage
from aiosendpulse.storage.exceptions import CacheUnavailableError


__all__ = ["AioSendPulseClient"]


BASE_URL: str = "https://api.sendpulse.com"


class AioSendPulseClient:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        token_storage: BaseTokenStorage,
        grant_type: Literal["client_credentials"] = "client_credentials",
        token: str = None,
    ) -> None:
        self.http_client = AsyncClient()
        self.auth_class: type[BearerTokenAuth] = BearerTokenAuth
        self.__token_cache_backend = token_storage
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__grant_type = grant_type
        self.__auth: Union[BearerTokenAuth, None] = None
        self.base_url = URL(url=BASE_URL)

        if token is not None:
            self.__auth = self.auth_class(token=token)

    async def close(self) -> None:
        await self.http_client.aclose()

    async def send(self, request: Request, retry_if_unauthorized: bool = True) -> Response:
        try:
            response = await self.http_client.send(request=request, auth=self.__auth, follow_redirects=True)
        except HTTPError as e:
            logger.error(f"Failed to send request with error: {e}")
            raise
        else:
            try:
                response.raise_for_status()
            except HTTPStatusError:
                if response.status_code == HTTPStatus.UNAUTHORIZED and retry_if_unauthorized:
                    await self.authorize()
                    return await self.send(request=request, retry_if_unauthorized=False)
                logger.error(f"Failed to send request with status {response.status_code} and error: {response.content}")
                raise

            return response

    async def authorize(self) -> None:
        try:
            token = await self.__token_cache_backend.get()
        except CacheUnavailableError as e:
            logger.error(f"Token cache unavailable with error: {e}")
            token = None

        if token is None:
            logger.debug("SendPulse token not cached")
            method = Authorize(
                client_id=self.__client_id,
                client_secret=self.__client_secret,
                grant_type=self.__grant_type,
            )
            response = await method(client=self)
            token = response.access_token.get_secret_value()
            ex = response.expires_in

            try:
                await self.__token_cache_backend.set(token=token, ex=ex)
            except CacheUnavailableError as e:
                logger.error(f"Token cache unavailable with error: {e}")
            else:
                logger.debug("Cache SendPulse token")

        self.__auth = self.auth_class(
            token=token,
        )

    @property
    def email(self) -> EmailService:
        return EmailService(client=self)

    @property
    def smtp(self) -> SmtpService:
        return SmtpService(client=self)

    async def __aenter__(self) -> AioSendPulseClient:
        if self.__auth is None:
            await self.authorize()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
