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