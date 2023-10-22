from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, desc
from questions.models import question
from database import get_async_session
import aiohttp
from sqlalchemy.testing import db

router = APIRouter(
    prefix='/questions',
    tags=['Question']
)





@router.post('/question/{questions_num}')
async def get_question(questions_num: int, session: AsyncSession = Depends(get_async_session)):
    async with aiohttp.ClientSession() as http_session:
        async with http_session.get(f'https://jservice.io/api/random?count={questions_num}') as resp:
            data = await resp.json()
            query = select(question).order_by(desc(question.c.id)).limit(1)
            result = await session.execute(query)
            for i in data:
                stmt = insert(question).values(id=i['id'],
                                               text_question=i['question'],
                                               text_answer=i['answer'],
                                               date=i['created_at']
                                               )
                await session.execute(stmt)
            await session.commit()


    return {'status': 'success',
            'data': result.mappings().all()}
