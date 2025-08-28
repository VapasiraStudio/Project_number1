from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/lists/", response_model=schemas.List)
def create_list(list: schemas.ListCreate, db: Session = Depends(get_db)):
    return crud.create_list(db=db, list=list)

@app.get("/lists/", response_model=List[schemas.Link])
def read_lists(db: Session = Depends(get_db),skip: int = 0, limit: int = 100):
    return crud.get_lists(db=db, skip=skip, limit=limit)

@app.post("/links/", response_model=schemas.Link)
def create_link(
    link: schemas.LinkCreate,db: Session = Depends(get_db)):
    return crud.create_link(db=db, link=link)

@app.put("/links/{link_id}", response_model=schemas.Link)
def update_link(link_id: int, link: schemas.LinkCreate, db: Session = Depends(get_db)):
    return crud.update_link(db=db, link_id=link_id, link=link)

@app.delete("links/{link_id}", response_model=schemas.Link)
def delete_link(link_id: int, db: Session = Depends(get_db)):
    crud.delete_link(db=db, link_id=link_id)
    return {"message": "Successfully deleted"}


