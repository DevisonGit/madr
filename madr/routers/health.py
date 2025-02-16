from http import HTTPStatus

from fastapi import APIRouter

from madr.schemas.general import Message

router = APIRouter(prefix='/health', tags=['health'])


@router.get('/', status_code=HTTPStatus.OK, response_model=Message)
def check_health():
    return {'message': 'ok'}
