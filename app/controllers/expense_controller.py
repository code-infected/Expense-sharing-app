from fastapi import APIRouter, HTTPException
from app.models.expense_model import Expense
from app.utils.firebase import db

router = APIRouter()


@router.post("/expenses")
async def add_expense(expense: Expense):
    try:
        # Add your logic for validating split details here
        expense_ref = db.collection('expenses').document()
        expense_ref.set(expense.dict())
        return {"message": "Expense added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/expenses/{user_email}")
async def get_user_expenses(user_email: str):
    try:
        expenses = db.collection('expenses').where('participants', 'array-contains', user_email).stream()
        expenses_list = [expense.to_dict() for expense in expenses]
        return expenses_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/expenses")
async def get_all_expenses():
    try:
        expenses = db.collection('expenses').stream()
        expenses_list = [expense.to_dict() for expense in expenses]
        return expenses_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/expenses/download")
async def download_balance_sheet():
    try:
        # Add logic to generate and return balance sheet (CSV or other format)
        return {"message": "Balance sheet download not implemented yet"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
