from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from enum import Enum


router = APIRouter()
templates = Jinja2Templates("templates")

class User(Enum):
    username: str
    name: str

@router.get("/register")
async def register(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={
            "title": "Register",
            "content_header": "Register details"
            }
        )

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="log_in.html",
        context={
            "title": "Log In",
            "content_header": "Enter details to log in"
            }
        )

