from typing import Union
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv
import os, uvicorn
# si ton prof avait schema et crud déjà préparés, tu peux les importer aussi :
# import schema, crud  

# Charger les variables d’environnement depuis .env
load_dotenv()  # take environment variables from .env

# Instancie FastAPI
app = FastAPI()

# Traitement des fichiers statiques (HTML, CSS, JS, images…)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Traitement des templates (Jinja2)
templates = Jinja2Templates(directory="templates")

from fastapi.responses import RedirectResponse

@app.get("/")
async def read_root():
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