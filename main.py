#Importing necessary packages
from fastapi import FastAPI, Requst, Form 
from fasta pi.responses import HTMLResponse
from typing import Optional

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

# Creating Request body class
class RequestBody(BaseModel):
    name: str
    # description: Optional[str] = None
    # price: float
    # tax: Optional[float] = None

# create an instant of an package
app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


@app.get('/home', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    # return {"message": "Welcome to the Fast API Development site"}


@app.get("/message")
def message():
    context = {"message": "Welcome To Fast API calling proccess.... "}
    print("context", context)
    return context


@app.post('/strMessage/')
async def strMessage(body: RequestBody):
    body.name = "This is the response from FastAPI and your input is " + \
        body.name + ", Thanks to calling. :) Developeed bt Vikas Ukani- keep learning keep smiling... "
    print("context", body)
    return body
