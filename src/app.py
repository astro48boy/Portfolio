from fastapi import Depends, FastAPI, HTTPException, Body, Request, Form, UploadFile, WebSocket, WebSocketDisconnect, \
    status
from starlette.responses import RedirectResponse, Response

from typing import Annotated

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="../templates")  # Change this path accordingly
app.mount("/assets", StaticFiles(directory="../templates/assets"), name="assets")


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
