from pydantic import BaseModel
from typing import Optional

from proto import data_pb2


class BirthInfo(BaseModel):
    date: Optional[str]
    place: Optional[str]
    country: Optional[str]


class Player(BaseModel):
    id: int
    name: str
    first_name: Optional[str]
    last_name: Optional[str]
    birth: Optional[BirthInfo]
    nationality: str
    height: Optional[str]
    weight: Optional[str]
    # for now we will dump all the stats in a dictionary
    statistics: Optional[dict]
