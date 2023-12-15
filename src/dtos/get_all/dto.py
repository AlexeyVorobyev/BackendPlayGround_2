from pydantic import BaseModel


class GetAllDTO(BaseModel):
    total_pages: int
    total_elements: int
    data: list
