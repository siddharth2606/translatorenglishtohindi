from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

translator = Translator()

class Text(BaseModel):
    text:str

@app.post("/translate")
def translate_text(data: Text):
    result = translator.translate(data.text,dest="hi")
    return{"translation":result.text}

