from pydantic import BaseModel, Field

class movie(BaseModel):
    title: str
    year: int
    genre: str
    rating: int = Field(..., ge=0, le=6)  # rating must be between 0 and 6

class Prompt(BaseModel):
    prompt: str


