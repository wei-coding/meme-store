from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from tinydb import TinyDB, Query, where

IMG_PATH = "static/img"
DB_PATH = "db.json"

db = TinyDB(DB_PATH)
memes_table = db.table("memes")
token_table = db.table("tokens")

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
def upload(file: UploadFile = File(), description: str = Form()):
    print(file.filename)
    print(description)
    with open(os.path.join(IMG_PATH, file.filename), "wb") as buffer:
        buffer.write(file.file.read())
    memes_table.insert({"filename": file.filename, "description": description})
    return {"filename": file.filename}

@app.get("/memes")
def get_memes():
    for meme in memes_table.all():
        print(meme)
    return {"memes": memes_table.all()}

@app.get("/memes/{meme_description}")
def get_meme(meme_description: str):
    meme = memes_table.search(where("description").matches(f'.*{meme_description}.*'))
    return meme

