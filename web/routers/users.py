from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_user():
    return {"user_id": 1}
