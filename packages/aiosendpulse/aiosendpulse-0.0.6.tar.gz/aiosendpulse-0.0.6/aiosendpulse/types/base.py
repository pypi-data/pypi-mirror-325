from pydantic import BaseModel, ConfigDict


class SendPulseObject(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        extra="allow",
        validate_assignment=True,
        frozen=True,
        populate_by_name=True,
        arbitrary_types_allowed=True,
        defer_build=True,
    )


class MutableSendPulseObjectObject(SendPulseObject):
    model_config = ConfigDict(
        frozen=False,
    )
