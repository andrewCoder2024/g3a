from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import pandas as pd
import requests 

app = FastAPI()
import os
@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}

@app.post("/generate")
async def generate_text(prompt: str):
    with open('prompt_script.txt', 'r') as infile:
        prompt = infile.read().replace('<<ED>>', prompt)
    url = 'https://api.openai.com/v1/completions'
    headers = {'Content-Type': 'application/json', 'Authorization': os.environ['openai_key']}
    r = requests.post(url, json = {"model": "text-davinci-003",
  "prompt": prompt,
  "max_tokens": 256,
  "temperature": 0.7}, headers=headers)
    completion = r["choices"][0]["text"]
    lines = completion.split("\n")
    lines = [line for line in lines if line]
    data = {}
    for line in lines:
        parts = line.split(":")

        key = parts[0].strip()
        value = parts[1].strip()

        data[key] = value
    json_data = json.dumps(data)
    return json_data