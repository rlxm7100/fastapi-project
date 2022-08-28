from unicodedata import name
import uvicorn
from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel, HttpUrl
from typing import Optional, List  # 추가: List
from fastapi import FastAPI, File, UploadFile
from tempfile import NamedTemporaryFile
from typing import IO

app = FastAPI()


@app.get("/users")
def get_users(is_admin: bool, limit: int = 100):  # 추가: q
    return {"is_admin": is_admin, "limit": limit}  # 추가: q



if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)