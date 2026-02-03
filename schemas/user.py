from pydantic import BaseModel as base, EmailStr as emails , Field
from typing import Optional as op
from datetime import datetime as dt


class userBase(base):
    username: str
    email:emails
class createuser(userBase):
    password : str
class updateuser(base):
    username : op[str] = None
    email : op[emails] = None
    password : op[str] = None
    is_active : op[bool] = None
class userdb(userBase):
    id : int
    is_active : bool
    created_at : dt
    updated_at : dt

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
class userResponse(userdb):
    pass
