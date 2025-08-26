from fastapi import APIRouter, HTTPException
from project.banks import get_bank_info, banks_data

router = APIRouter()

@router.get("/banks")
def get_all_banks():
    return {"banks": banks_data}

@router.get("/banks/{bank_name}")
def get_bank(bank_name: str):
    bank = get_bank_info(bank_name)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")
    return {"bank": bank}