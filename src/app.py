from fastapi import FastAPI, HTTPException, Body, Form
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from src.utils.bot import bot_response
from pydantic import BaseModel, Field
from typing import Annotated
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")




@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )



class Payload(BaseModel):
    prompt: str = Field(
        default=None, title="Enter a prompt", max_length=300
    )

@app.post("/request")
async def make_request(prompt: str = Form(...)):
    try:
        print(prompt)
        res = bot_response(prompt=prompt)
        return {"message": res}
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))
 