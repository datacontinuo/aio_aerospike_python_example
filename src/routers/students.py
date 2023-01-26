from fastapi import APIRouter

from utils.common import get_aerospike_client
router = APIRouter()

@router.get("/")
async def get_all():
    client = get_aerospike_client()
    data = client.get_many()

@router.get("/")
async def get_bi_id():
    client = get_aerospike_client()
    data = rerer
    
@router.post("/")
async def get():
    return {}

@router.put("/")
async def put():
    return {}
        
@router.delete("/")
async def delete():
    return {}
    