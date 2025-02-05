from enum import StrEnum
from typing import Literal, Optional

from pydantic import Field

from dainty import DaintyModel
from dainty.dainty import DaintyExtras, DaintyForm, Number


class Parent(DaintyModel):
    name: str
    age: int


class Gender(StrEnum):
    MALE = "Male"
    FEMALE = "Female"
    NON_BINARY = "Non Binary"
    OTHER = "Other"


class MyModel(DaintyModel):
    name: str
    age: Number = Field(gt=17, lt=41, description="Age must be between 18 and 40")
    gender: list[Gender] | None = Field(
        "Other",
        json_schema_extra=DaintyExtras(dainty_select_type="checkbox").model_dump(),
    )
    origin: Optional[Literal["Earth", "Mars", "Venus"]] = Field(
        json_schema_extra=DaintyExtras(dainty_select_type="radio").model_dump()
    )
    parent: Parent

    dainty_form = DaintyForm(target_url="/submit")


html = MyModel.to_html(form=True)

# print(html)
