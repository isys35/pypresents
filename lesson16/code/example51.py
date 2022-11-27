from pydantic import BaseModel

class User(BaseModel):
    name: str
    surname: str
    age: int


def get_user_from_json(json_dict: Dict[str, Optional[Union[int, str]]]) -> User:
    return User(**json_dict)

get_user_from_json({
    "name": "ssa",
    "surname": "ddd",
    "age": 10
})
>>> User(name='ssa', surname='ddd', age=10)

get_user_from_json({
    "name": "ssa",
    "surname": "ddd",
    "age": "10"
 })
>>> User(name='ssa', surname='ddd', age=10)

get_user_from_json({
    "name": "ssa",
    "surname": "ddd",
    "age": "d"
})
--------------------------------------
ValidationError: 1 validation error for User
age
 value is not a valid integer (type=type_error.integer)