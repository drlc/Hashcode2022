from typing import List

from pydantic import BaseModel


class Skill(BaseModel):
    name: str
    level: int


class Contributor(BaseModel):
    name: str
    skills: List[Skill] = []


class Role(BaseModel):
    name: str
    level: int


class Proj(BaseModel):
    name: str
    days: int
    score: int
    best_before: int
    roles: List[Role] = []
