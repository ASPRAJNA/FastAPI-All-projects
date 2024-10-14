from fastapi import APIRouter,Request
from models.note import Note
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from config.db import conn
from schemas.note import noteEntity,notesEntity

note=APIRouter()


note.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@note.get("/")
async def home(request:Request):
    docs=conn.notesCollection.notes.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "title":doc["title"],
            "note":doc["note"]
        })
    return templates.TemplateResponse("index.html",{"request":request, "docs":newDocs})

@note.post("/add",response_class=HTMLResponse)
async def add_note(request:Request):
    form=await request.form()
    inserted_note=conn.notesCollection.notes.insert_one(dict(form))
    response = RedirectResponse(url="/")
    return response