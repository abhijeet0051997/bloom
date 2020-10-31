from typing import Dict

from fastapi import APIRouter, Depends
from starlette.status import  HTTP_202_ACCEPTED

from app.api.dependencies.account import update_account_dependency

router = APIRouter()

@router.put(
    "/dataset.create",
    status_code=HTTP_202_ACCEPTED,
    response_model=Dict[str,str],
    name="account:update",
)
async def update_account(
    account_update: Dict[str,str] = Depends(update_account_dependency),
) -> Dict[str,str]:
    return account_update
