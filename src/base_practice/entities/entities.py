from typing import List

from pydantic import BaseModel


class Skill(BaseModel):
    name: str
    level: int


class Contributor(BaseModel):
    name: str
    skills: List[Skill] = []
    hired_until: int = -1



class Role(BaseModel):
    name: str
    level: int


class Proj(BaseModel):
    name: str
    days: int
    score: int
    best_before: int
    roles: List[Role] = []
    end_day: int = None
    hires: List[Contributor] = []

    def hire(self, contributor_by_skills, current_day) -> List[Contributor]:
        hired = []
        end_project_day = current_day + self.days -1
        try:
            print(f"Hiring for {self.name} day {current_day}===")
            for role in self.roles:
                print(f"Looking for {role.name}")
                print(contributor_by_skills[role.name])
                contrib_el = next(filter(lambda x: x[1].level >= role.level and x[0].hired_until <= current_day, contributor_by_skills[role.name]))
                contrib = contrib_el[0]
                hired.append((contrib, role))
            self.hires = [x[0] for x in hired]
            self.end_day = end_project_day
        except Exception:
            print(f"hiring exception for {self.name}")
            return []

        for hire, role in hired:
            print(f"HIRE: {hire.name} untill {end_project_day}")
            hire.hired_until = end_project_day
            hire_role = next(x for x in hire.skills if x.name == role.name)
            if hire_role.level == role.level:
                print(f"{hire.name} levelup {role.name}")
                hire_role.level += 1

        return hired

    def __str__(self):
        return f"{self.name}\n{' '.join([x.name for x in self.hires])}"



