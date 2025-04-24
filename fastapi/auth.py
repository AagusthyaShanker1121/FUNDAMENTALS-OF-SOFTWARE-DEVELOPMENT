from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from typing import Annotated
from uniapp.users import Student, register_student

router = APIRouter()
templates = Jinja2Templates("templates")

class UserForm(BaseModel):
    name: str
    email: str
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
async def create_user(
    name: Annotated[str, Form()],
    email: Annotated[str, Form()],
    password: Annotated[str, Form()],
    password_2: Annotated[str, Form()]
):
    user = UserForm(name=name, email=email, password=password, password_2=password_2)
    if user.password == user.password_2:
        print("Passwords match.")
        register_student(user)
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

