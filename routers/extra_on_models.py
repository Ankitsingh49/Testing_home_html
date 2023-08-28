from fastapi import APIRouter , Depends, Request
from fastapi import Body , Path , Query , HTTPException
from pydantic import BaseModel , Field
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 
from fastapi import APIRouter , Depends, Form, Request
import numpy as np 


router = APIRouter()

templates =  Jinja2Templates(directory= "templates")

@router.get("/extra_on_models", response_class=HTMLResponse)
def test_model(request:Request):
    return templates.TemplateResponse("extra_on_models.html", {"request":request})



