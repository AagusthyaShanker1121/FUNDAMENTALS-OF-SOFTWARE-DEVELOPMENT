from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from typing import Annotated

router = APIRouter()
templates = Jinja2Templates("templates")

class User(BaseModel):
    # id: int
    username: str
    name: str
    password: str
    password_2: str

@router.get("/register")
async def register(request: Request, response_class=HTMLResponse):
    output = templates.TemplateResponse(
        request, 
        "register.html", 
        {"title": "Register", "content_header": "Register details"}
        )
    return output

@router.post("/register")
async def create_user(user: Annotated[User, Depends()]):
    if user.password == user.password_2:
        print("Passwords match.")
    else:
        print("Passwords do not match.")

    
    return RedirectResponse("/", status_code=303)

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

