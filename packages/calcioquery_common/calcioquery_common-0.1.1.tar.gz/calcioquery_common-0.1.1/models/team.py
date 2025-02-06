from typing import Optional
from pydantic import BaseModel

from proto import data_pb2


class Team(BaseModel):
    id: int
    name: str
    country: str
    founded_year: int
    is_national: bool
    stadium_id: int

    @classmethod
    def from_proto(cls, proto: data_pb2.Team) -> "Team":
        return cls(**proto.__dict__)

    def to_proto(self) -> data_pb2.Team:
        return data_pb2.Team(**self.model_dump())


class GoalsSummary(BaseModel):
    goals_for: int
    goals_against: int


class TeamLeaguePerformance(BaseModel):
    played: int
    win: int
    draw: int
    lose: int
    goals: GoalsSummary


class TeamLeagueStanding(BaseModel):
    team_id: int
    rank: int
    points: int
    description: Optional[str]
    league_id: int
    group: Optional[str]
    season: int
    all: TeamLeaguePerformance
    home: TeamLeaguePerformance
    away: TeamLeaguePerformance
