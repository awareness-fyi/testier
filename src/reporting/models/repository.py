from pydantic import BaseModel


class Repository(BaseModel):
    id: str

    def __eq__(self, other: "Repository") -> bool:
        return self.id == other.id
