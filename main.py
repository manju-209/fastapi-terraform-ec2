from fastapi import FastAPI as fa
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routes.user import router as User

app = fa(
   description = "User Management",
   title = "User API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)
app.include_router(User,prefix ="/api/user")

@app.get("/")
def start():
    return {"Message" : "Running Sucessfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
