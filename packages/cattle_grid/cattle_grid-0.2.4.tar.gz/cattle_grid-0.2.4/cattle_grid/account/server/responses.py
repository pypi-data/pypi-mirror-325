from typing import List
from pydantic import BaseModel, Field, ConfigDict


class SignInData(BaseModel):
    """Used to sign into an account"""

    name: str = Field(description="Name of the account")
    password: str = Field(description="Password")


class SignUpData(BaseModel):
    name: str
    password: str


class TokenResponse(BaseModel):
    """Returns the token to be used with Bearer authentication, i.e.
    add the Header `Authorization: Bearer {token}` to the request"""

    token: str = Field(description="The token")


class LookupRequest(BaseModel):
    actor_id: str = Field(alias="actorId")
    uri: str


class LookupResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    raw: dict


class PublicIdentifierInformation(BaseModel):
    identifier: str
    name: str
    preference: int


class ActorInformationRequest(BaseModel):
    actor_id: str = Field(alias="actorId")
    update: dict | None = None


class ActorInformationResponse(BaseModel):
    raw: dict
    identifiers: List[PublicIdentifierInformation] = Field(default_factory=list)
    automatically_accept_followers: bool = False


class SettingsResponse(BaseModel):
    base_urls: List[str] = Field(
        default_factory=list,
        examples=["http://domain.example"],
        serialization_alias="baseUrls",
    )
