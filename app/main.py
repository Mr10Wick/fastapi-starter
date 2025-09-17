from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

from app import schemas  # pour importer User

# Charger les variables d’environnement depuis .env
load_dotenv()

# Instancie FastAPI
app = FastAPI()

# Traitement des fichiers statiques (HTML, CSS, JS, images…)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Traitement des templates (Jinja2)
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root():
    """Redirection vers index.html"""
    return RedirectResponse("/static/index.html")


@app.get("/items/{item_id}")
def read_item(request: Request, item_id: int, q: Union[str, None] = None):
    """
    Recherche d'un item, sous forme de template
    :param request: Request lié à l'appel GET
    :param item_id: l'ID de l'item
    :param q: un paramètre optionnel
    :return: Le template avec le contexte de l'item
    """
    return templates.TemplateResponse(
        "item.html",
        {"request": request, "item_id": item_id, "q": q}
    )


@app.post("/user/{user_id}", response_model=schemas.User)
def post_user(request: Request, user: schemas.User):
    """
    Création de User
    :param request: Request lié à l'appel GET
    :param user: Un objet de type User
    :return: le User en question
    """
    print("USER", user)
    return user

@app.get("/health")
def health():
    return {"status": "ok"}
