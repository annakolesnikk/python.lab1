from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    position: str
    department: str
    salary: float

    @property
    def info(self) -> str:
        return f"{self.name} ({self.position}, {self.department})"