from fastapi import APIRouter


router = APIRouter(
    prefix="/region",
    tags=["region"],
)


@router.post("")
async def add_region():
    pass


@router.get("")
async def get_regions():
    pass