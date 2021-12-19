from fastapi import FastAPI

from .routes import pdf

app = FastAPI()
app.include_router(pdf.router)


@app.get("/")
async def root():
    return {"message": "pdf generator service"}
