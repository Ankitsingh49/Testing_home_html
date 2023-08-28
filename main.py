from fastapi import APIRouter , Depends, Form, Request
from fastapi import Body , Path , Query , HTTPException
from routers import models , extra_on_models, real_time, aboutme, sentiment , resources

from routers import telemetics

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles



app = FastAPI()
templates = Jinja2Templates(directory= "templates")

app.mount("/static", StaticFiles(directory="static"), name = "static")

@app.get("/")
def get_index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# Santander transaction prediction 


app.include_router(models.router)

app.include_router(extra_on_models.router)


app.include_router(real_time.router)

app.include_router(aboutme.router)



app.include_router(sentiment.router)

app.include_router(resources.router)

app.include_router(telemetics.router)

 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)

    
    


    
    
     



























