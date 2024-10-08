from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import Annotated
from tinydb import TinyDB, Query, where

IMG_PATH = "static/img"
DB_PATH = "db.json"

db = TinyDB(DB_PATH)
memes_table = db.table("memes")
token_table = db.table("tokens")

tokens = [it["token"] for it in token_table.all()]

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return 'OK'

@app.post("/upload")
async def upload(file: Annotated[UploadFile, File()], description: Annotated[str, Form()], token: Annotated[str, Form()]):
    if token not in tokens:
        return {"error": "Invalid token"}
    with open(os.path.join(IMG_PATH, file.filename), "wb") as buffer:
        buffer.write(await file.read())
    memes_table.insert({"url": '/api/static/img/' + file.filename, "description": description})
    return {"file": file.filename}

@app.get("/memes")
def get_memes():
    return {"memes": memes_table.all()}

@app.get("/memeswithid")
def get_memes_with_id():
    memes_with_id = []
    for meme in memes_table:
        memes_with_id.append({"id": str(meme.doc_id), "url": meme["url"], "description": meme["description"]})
    return {"memes": memes_with_id}

@app.delete("/memes/{meme_id}")
def delete_meme(meme_id: str, token: str):
    if token not in tokens:
        return {"error": "Invalid token"}
    file_path = memes_table.get(doc_id=int(meme_id))["url"]
    file_path = file_path.split("/")[-1]
    file_path = os.path.join(IMG_PATH, file_path)
    try:
        os.remove(file_path)
    except Exception:
        pass
    memes_table.remove(doc_ids=[int(meme_id)])
    return {"message": "Meme deleted"}

@app.get("/memes/{meme_description}")
def get_meme(meme_description: str):
    meme = memes_table.search(where("description").matches(f'.*{meme_description}.*'))
    return {"memes": meme}

