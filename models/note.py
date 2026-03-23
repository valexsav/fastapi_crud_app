from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str
    important: bool = False

class Note(BaseModel):
    id: int
    title: str
    content: str
    important: bool