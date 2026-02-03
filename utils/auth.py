from passlib.context import CryptContext as cy

pwd_context = cy(schemes = ["bcrypt"],deprecated = "auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)
def get_password(password):
    return pwd_context.hash(password)



