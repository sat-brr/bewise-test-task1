import uvicorn
from fastapi import APIRouter, FastAPI
from app import settings
from app.api.questions_handler import question_router

app = FastAPI()
main_router = APIRouter()


main_router.include_router(
    question_router,
    prefix="/questions",
    tags=["questions"]
)
app.include_router(main_router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)
