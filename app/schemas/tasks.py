from pydantic import BaseModel, ConfigDict

class TaskRead(BaseModel):
  model_config=ConfigDict(from_attributes=True)

  id: int
  title: str
  completed: bool = False

class TaskCreate(BaseModel):

  title: str

class TaskUpdate(BaseModel):

  title: str | None
  completed: bool | None