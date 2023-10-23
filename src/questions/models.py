from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, func

metadata = MetaData()

question = Table(
    'question',
    metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('question_id', Integer),
    Column('text_question', String, nullable=False),
    Column('text_answer', String, nullable=False),
    Column('date', String)
)