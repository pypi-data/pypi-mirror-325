import uuid
from datetime import date, datetime, time
from decimal import Decimal
from enum import StrEnum
from typing import List, Literal, Optional
from uuid import UUID

import pytest
from pydantic import BaseModel, EmailStr, Field, HttpUrl, SecretStr

from dainty.dainty import DaintyExtras, DaintyModel, DaintyParsingWarning
from dainty.documentation import generate_model_docs, get_style


class Gender(StrEnum):
    MALE = "Male"
    FEMALE = "Female"
    NON_BINARY = "Non binary"
    OTHER = "Other"


class UserType(StrEnum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class Parent(DaintyModel):
    name: str
    age: int


class Person(DaintyModel):
    name: str = Field(
        ..., min_length=2, max_length=50, description="Full name of the person"
    )
    email: EmailStr
    password: SecretStr
    gender: Gender
    age: int = Field(gt=17, lt=41, description="Age must be between 18 and 40")
    birth_date: date
    website: Optional[HttpUrl] = None
    user_type: UserType = Field(default=UserType.USER)
    balance: Decimal = Field(ge=0, default=0)
    active: bool = True
    login_time: time = Field(default=time(9, 0))
    last_login: datetime = Field(default=datetime.now())
    user_id: UUID = Field(default_factory=uuid.uuid4)
    country: Literal["US", "UK", "NZ"] = Field(
        json_schema_extra=DaintyExtras(dainty_select_type="radio").model_dump()
    )
    parent: Parent


def test_dainty_to_html():
    with pytest.warns(DaintyParsingWarning):
        with open("dainty.html", "w") as f:
            f.write(str(Person.to_html(form=True)))


def test_dainty_documentation():
    class Car(BaseModel):
        """Details about a car."""

        make: str = Field(description="The manufacturer of the car")
        price: int = Field(description="The price of the car in dollars")

    class User(BaseModel):
        """A user in the system."""

        id: int = Field(description="Unique identifier for the user")
        username: str = Field(description="User's login name")
        email: str = Field(description="User's email address")
        full_name: Optional[str] = Field(None, description="User's full name")
        age: Optional[int] = Field(None, description="User's age in years")
        tags: List[str] = Field(default_factory=list, description="List of user tags")
        car: Optional[Car] = Field(None, description="User's car details")

    # Generate documentation
    style = get_style()
    docs = style + generate_model_docs(User)

    # Save to file
    with open("user_model_docs.html", "w") as f:
        f.write(docs)


if __name__ == "__main__":
    test_dainty_to_html()
    test_dainty_documentation()
