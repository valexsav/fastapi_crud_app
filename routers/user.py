from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def main_page():
    return {"message": "yo hows life?"}

@router.get("/health")
def health_check():
    return {"health": "good"}
