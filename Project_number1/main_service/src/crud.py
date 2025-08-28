from sqlalchemy.orm import Session
import chemas
import models

def get_lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.List).offset(skip).limit(limit).all()

def create_list(db: Session, list: chemas.ListCreate):
    db_list = models.List(name=list.name)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list

def get_links(db: Session, list_id: int | None = None, search: str | None = None):
    query = db.query(models.Link)
    if list_id:
        query = query.filter(models.Link.list_id == list_id)
    if search:
        query = query.filter(
            (models.Link.title.ilike(f"%{search}%")) |
            (models.Link.description.ilike(f"%{search}%"))
        )
    return query.all()


def create_link(db: Session, link: chemas.LinkCreate):
    db_link = models.Link(**link.dict())
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def update_link(db: Session, link_id: int, link: chemas.LinkCreate):
    db_link = db.query(models.Link).filter(models.Link.id == link_id).first()
    if db_link:
        for key, value in link.dict().items():
            setattr(db_link, key, value)
        db.commit()
        db.refresh(db_link)
    return db_link

