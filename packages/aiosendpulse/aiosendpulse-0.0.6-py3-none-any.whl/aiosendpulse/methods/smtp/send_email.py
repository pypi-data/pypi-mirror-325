from __future__ import annotations

from base64 import b64encode
from typing import Annotated, Union

from httpx import URL, Request
from pydantic import Field, PlainSerializer, ValidationError, model_validator

from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import Recipient, Result, Sender, TemplateMeta


__all__ = ["SendEmail"]


class SendEmail(SendPulseMethod[Result]):
    html: Annotated[
        Union[str, None], PlainSerializer(func=lambda v: b64encode(v.encode()).decode() if v else None, return_type=str)
    ] = None
    text: Union[str, None] = None
    template: Union[TemplateMeta, None] = None
    auto_plaint_text: bool = False
    subject: str
    sender: Annotated[Sender, Field(serialization_alias="from")]
    to: list[Recipient]
    cc: Union[list[Recipient], None] = None
    bcc: Union[list[Recipient], None] = None
    attachments: Union[dict[str, str], None] = None
    attachments_binary: Annotated[
        Union[dict[str, str], None],
        PlainSerializer(
            func=lambda v: {k: b64encode(v.encode()).decode() for k, v in v.items()} if v else None,
            return_type=Union[dict[str, str], None],
        ),
    ] = None

    __http_method__ = "POST"
    __api_endpoint__ = "/smtp/emails"
    __returning__ = Result

    @model_validator(mode="after")
    def model_validator(self) -> SendEmail:
        if self.html and self.template:
            raise ValidationError("")

        if not self.html and not self.template:
            raise ValidationError("")

        return self

    def build_request(self, base_url: URL) -> Request:
        return Request(
            method=self.__http_method__,
            url=base_url.join(url=self.__api_endpoint__),
            json={
                "email": self.model_dump(mode="json", exclude_none=True, exclude_unset=True, by_alias=True),
            },
        )
