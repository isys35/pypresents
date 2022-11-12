from typing import Literal

GENDER = Literal["male", "female", "non–conforming"]

def create_user(first_name: str, last_name: str, gender: GENDER) –> dict[str, str, GENDER]:
    return {"first_name": first_name, "last_name": last_name, "gender": gender}

create_user("John", "Bond", "male")