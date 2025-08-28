from pydantic import BaseModel

class ListBase(BaseModel):
    name: str

class ListCreate(ListBase):
    pass

class List(ListBase):
    id: int

    class Config:
        from_attributes = True

class LinkBase(BaseModel):
    url: str
    title: str
    description: str | None = None
    list_id: int | None = None

class LinkCreate(LinkBase):
    pass

class Link(LinkBase):
    id: int

    class Config:
        from_attributes = True
