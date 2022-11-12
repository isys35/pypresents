from typing import TypedDict, Union


class Card(TypedDict):
    rank: Union[str, int]
    suit: str

# класс Card теперь имеет поведение обоих классов TypedDict и dict

# Card может быть использован для аннотации переменной
ace_of_spade: Card = {'rank': 'A', 'suit': '♤'}

# или может быть инстанцирован
ace_of_spade = Card(rank='A', suit='♤')