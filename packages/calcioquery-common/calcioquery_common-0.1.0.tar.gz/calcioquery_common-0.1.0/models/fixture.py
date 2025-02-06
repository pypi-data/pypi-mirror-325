from pydantic import BaseModel
from typing import Optional

from proto import data_pb2


class FixtureTeamInfo(BaseModel):
    team_id: int
    goals: int
    winner: Optional[bool]


class FixtureIntermediateScore(BaseModel):
    home: Optional[int]
    away: Optional[int]


class FixtureScore(BaseModel):
    halftime: FixtureIntermediateScore
    fulltime: FixtureIntermediateScore
    extratime: Optional[FixtureIntermediateScore] = None
    penalties: Optional[FixtureIntermediateScore] = None


class Fixture(BaseModel):
    id: int
    referee: Optional[str]
    timezone: str
    date_time: str
    stadium_id: int
    league_id: int
    league_season: int
    league_round: str
    home_team: FixtureTeamInfo
    away_team: FixtureTeamInfo
    score: FixtureScore

    @classmethod
    def from_proto(cls, proto: data_pb2.Fixture) -> "Fixture":
        return cls(**proto.__dict__)

    def to_proto(self) -> data_pb2.Fixture:
        return data_pb2.Fixture(**self.dict())
