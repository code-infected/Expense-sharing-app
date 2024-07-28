from pydantic import BaseModel
from typing import List, Dict


class Expense(BaseModel):
    description: str
    total_amount: float
    participants: List[str]
    split_method: str  # 'equal', 'exact', or 'percentage'
    split_details: Dict[str, float]  # {user_email: amount/percentage}
