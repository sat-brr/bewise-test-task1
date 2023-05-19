import uvicorn
from fastapi import APIRouter, FastAPI

from app.api.handlers import question_router
from app.database.db_models.question import Question
from app.database.engine import init_db

app = FastAPI()
main_router = APIRouter()


main_router.include_router(
    question_router,
    prefix="/questions",
    tags=["questions"]
)
app.include_router(main_router)


@app.on_event("startup")
async def on_startup():
    await init_db()


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)
