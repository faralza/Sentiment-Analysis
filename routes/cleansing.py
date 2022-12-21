from typing import Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Query
from services.cleansing import CleansingServices

router = APIRouter()

@router.get( "/split")
async def cleansing_split(
    text: str 
):
    result = await CleansingServices().split_word(text= text)
    return result