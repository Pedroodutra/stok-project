from fastapi.responses import JSONResponse
from app.routes.user.route import router as user_router
from app.database.database import engine, Base
from app.models.user_model import User 
from fastapi import FastAPI

app = FastAPI()
app.include_router(user_router)
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



