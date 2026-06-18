from fastapi import APIRouter
from app.services.azure_service import get_resource_groups

router = APIRouter()

@router.get("/resource-groups")
def resource_groups():

    return {
        "provider":"azure",
        "groups":get_resource_groups()
    }