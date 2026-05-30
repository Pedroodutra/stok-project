from app.database.database import engine, Base
from app.models.user_model import User 
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():

    try:
        # testa banco aqui

        return {"status": "healthy"}

    except Exception:

        return JSONResponse(
            status_code=503,
            content={"status": "unhealthy"}
        )
