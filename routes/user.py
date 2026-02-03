from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session as ses
from typing import List as list
from db.database import get_db
from schemas.user import createuser,updateuser,userResponse
from services.user import create_user,get_user_id,get_user,update_user,delete_user

router = APIRouter(prefix = "/users", tags = ["Users"])
@router.post("/",response_model = userResponse,status_code = status.HTTP_201_CREATED)
def create_new_user(user:createuser,db:ses = Depends(get_db)):
    return create_user(db=db,user = user)
@router.get("/{user_id}", response_model = userResponse)
def read_user(user_id: int, db : ses = Depends(get_db)):
    db_user = get_user_id(db, user_id = user_id)
    if db_user is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User not found")
    return db_user
@router.put("/{user_id}", response_model = userResponse)
def update_user_endpoint(user_id: int, user : updateuser, db: ses = Depends(get_db)):
    return update_user(db = db , user_id = user_id, user = user)
@router.delete("/{user_id}", status_code = status.HTTP_200_OK)
def delete_user_endpoint(user_id: int, db: ses =Depends(get_db)):
    return delete_user(db= db, user_id = user_id)
