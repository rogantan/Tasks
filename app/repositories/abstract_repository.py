from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete

class AbstractRepository:
  def __init__(self, model, session: AsyncSession):
    self.model = model
    self.session = session

  async def get_all(self):
    query = select(self.model)
    result = await self.session.execute(query)
    return result.scalars().all()

  async def get_by_id(self, model_id: int | str):
    query = select(self.model).where(self.model.id == model_id)
    result = await self.session.execute(query)
    return result.scalars().one_or_none()

  async def insert(self, **data):
    query = insert(self.model).values(**data)
    result = await self.session.execute(query.returning(self.model))
    return result.scalars().one()

  async def update(self, model_id: int | str, **data):
    query = update(self.model).where(self.model.id == model_id).values(**data)
    result = await self.session.execute(query.returning(self.model))
    return result.scalars().one()

  async def delete(self, model_id: int | str):
    obj = self.get_by_id(self.session, model_id)
    await self.session.delete(obj)
