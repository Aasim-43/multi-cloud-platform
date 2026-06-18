from fastapi import APIRouter
from app.services.aws_service import get_ec2_instances

router = APIRouter()

@router.get("/instances")
def instances():

    return {
        "provider":"aws",
        "instances":get_ec2_instances()
    }