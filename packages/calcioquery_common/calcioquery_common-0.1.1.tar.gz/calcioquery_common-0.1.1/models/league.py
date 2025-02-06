from pydantic import BaseModel

from proto import data_pb2


class League(BaseModel):
    id: int
    name: str
    competition_type: str
    country: str
    start_year: int
    end_year: int

    @classmethod
    def from_proto(cls, proto: data_pb2.League) -> "League":
        return cls(**proto.__dict__)

    def to_proto(self) -> data_pb2.League:
        return data_pb2.League(**self.model_dump())
