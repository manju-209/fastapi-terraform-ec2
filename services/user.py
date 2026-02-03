from abc import update_abstractmethods
from sqlalchemy.orm import Session as ses
from fastapi import HTTPException,status
from models.user import User
from schemas.user import createuser,updateuser as userupdate
from utils.auth import get_password, verify_password
from utils.email import validate_email

def get_user_id(db:ses,user_id:int):
    return db.query(User).filter(User.id == user_id).first()
def get_user_email(db: ses,email : str):
    return db.query(User).filter(User.email == email).first()
def get_user_username(db:ses,name:str):
    return db.query(User).filter(User.username == name).first()
def get_user(db: ses, skip: int = 0, limit : int = 100):
    return db.query(User).offset(skip).limit(limit).all()
def create_user(db : ses , user = createuser):
    valid,message = validate_email(user.email)
    if not valid:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = message)
    db_user =  get_user_email(db , email = user.email)
    if db_user:

        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Email already registered")
    hashed_password = get_password(user.password)
    db_user = User(username = user.username, email = user.email, password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db:ses, user_id : int , user : userupdate):
    db_user = get_user_id(db,user_id)
    if not db_user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User not found")
    update = user.model_dump(exclude_unset = True)
    if "email" in update:
        valid,message = validate_email(update["email"])
        if not valid:
            raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = message)
        existing_user = get_user_email(db, email = update["email"])
        if existing_user and existing_user.id != user_id:
            raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Email already registered")
    
    if "password" in update:
        update["password"] = get_password(update["password"])
       
    for key , value in update.items():
        setattr(db_user,key,value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:ses,user_id:int):
    db_user = get_user_id(db,user_id)
    if not db_user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User not Found")
    db.delete(db_user)
    db.commit()
    return{"message":f"User Deleted Successfully{user_id}"}


    


