from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    age: int

    @validator('age')
    def validate_age(cls, value):
        if int(value) < 10:
            raise ValueError("too low")
        return str(value)

User(name='Brian', age=33)
>>> User(name='Brian', age='33')