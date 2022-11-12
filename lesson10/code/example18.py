from typing import Any

result: Any = "SUCCESS"

# также работает, потому что переменные типа Any совместимы с другими типами
result = 10

state: str = "PENDING"

# работает, потому что все остальные типы совместимы с типом Any.
state = result