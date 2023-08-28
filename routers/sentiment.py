from fastapi import APIRouter , Depends, Request

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 
from fastapi import APIRouter , Depends, Form, Request
from fastapi.responses import RedirectResponse

router = APIRouter()
templates =  Jinja2Templates(directory= "templates")


@router.get("/sentiment", response_class=RedirectResponse)
def test_model():
    return RedirectResponse(url="https://shorturl.at/loOZ7")