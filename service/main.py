from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.stock_prices import stock_prices_router

app = FastAPI()

origins = [

    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Programador message": "Aiuda esto es sobre explotacion laboral"}