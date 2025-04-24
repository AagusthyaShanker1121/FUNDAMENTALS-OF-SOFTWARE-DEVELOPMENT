from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 
import arel
import auth
from uniapp.main import __main__, initialize_app

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth.router)

templates = Jinja2Templates("templates")

app_objects = initialize_app()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="base.html",
        context={
            "title": "Home",
            "content_header": "Welcome to the bank app!"
            }
        )

@app.get("/courses", response_class=HTMLResponse)
async def get_courses():
    return {"courses": app_objects["courses"]}

@app.get("/admins", response_class=HTMLResponse)
async def get_admins():
    return {"admins": app_objects["admins"]}


