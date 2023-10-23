from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, desc
from questions.models import question
from database import get_async_session
import aiohttp
from sqlalchemy.testing import db
from sqlalchemy.sql import exists

router = APIRouter(
    prefix='/questions',
    tags=['Question']
)
async def unique_question(question_api: dict, session: AsyncSession = Depends(get_async_session)) -> bool:
    stmt = (select(exists().where(question.c.question_id == question_api['id'])))
    result = await session.execute(stmt)
    return result.scalar()


@router.post('/question/{questions_num}')
async def get_question(questions_num: int, session: AsyncSession = Depends(get_async_session)):
    async with aiohttp.ClientSession() as http_session:
        async with http_session.get(f'https://jservice.io/api/random?count={questions_num}') as resp:
            data = await resp.json()
            query = select(question).order_by(desc(question.c.id)).limit(1)
            result = await session.execute(query)
            for i in data:
                while await unique_question(i, session=session):
                    print(f'Повторная запись!')
                    async with http_session.get(f'https://jservice.io/api/random') as new_resp:
                        new_question = await new_resp.json()
                        i = new_question[0]

                stmt = insert(question).values(question_id=i['id'],
                                               text_question=i['question'],
                                               text_answer=i['answer'],
                                               date=i['created_at']
                                               )
                await session.execute(stmt)
            await session.commit()

    return {'status': 'success',
            'data': result.mappings().all()}


