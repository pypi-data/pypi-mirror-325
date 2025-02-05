from typing import Union

from aiosendpulse.methods.email.addressbook import (
    AddEmailsToAddressbook,
    CreateAddressbook,
    EditAddressbook,
    GetAddressbook,
    GetEmailsFromAddressbook,
    GetListOfAddressbook,
    GetListOfAddressbookVariables,
    GetTotalEmails,
    SearchEmails,
)
from aiosendpulse.services.base import BaseService
from aiosendpulse.types import Addressbook, AddressbookId, AddressbookVariable, EmailDetail, Result, TotalEmails


__all__ = ["AddressbookService"]


class AddressbookService(BaseService):
    async def create(self, name: str) -> AddressbookId:
        return await CreateAddressbook(
            book_name=name,
        )(client=self.client)

    async def edit(self, addressbook_id: int, name: str) -> Result:
        return await EditAddressbook(id=addressbook_id, name=name)(client=self.client)

    async def get_list(self, limit: int = None, offset: int = None) -> list[Addressbook]:
        return await GetListOfAddressbook(
            limit=limit,
            offset=offset,
        )(client=self.client)

    async def get(self, addressbook_id: int) -> Addressbook:
        method = GetAddressbook(id=addressbook_id)
        response = await method(client=self.client)
        if response:
            return response[0]

    async def variables(self, addressbook_id: int) -> list[AddressbookVariable]:
        return await GetListOfAddressbookVariables(
            id=addressbook_id,
        )(client=self.client)

    async def add_emails(self, addressbook_id: int, emails: list[Union[EmailDetail, dict]]) -> Result:
        return await AddEmailsToAddressbook(
            addressbook_id=addressbook_id,
            emails=emails,
        )(client=self.client)

    async def get_emails(
        self, addressbook_id: int, limit: int = None, offset: int = None, active: bool = None, not_active: bool = None
    ) -> list[EmailDetail]:
        return await GetEmailsFromAddressbook(
            id=addressbook_id,
            limit=limit,
            offset=offset,
            active=active,
            not_active=not_active,
        )(client=self.client)

    async def get_total_emails(self, addressbook_id: int) -> TotalEmails:
        return await GetTotalEmails(id=addressbook_id)(client=self.client)

    async def search_emails(self, addressbook_id: int, variable_name: str, variable_value: str) -> list[EmailDetail]:
        return await SearchEmails(id=addressbook_id, variable_name=variable_name, search_value=variable_value)(
            client=self.client
        )
