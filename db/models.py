from pydantic import BaseModel


class TypeSubscribe(BaseModel):
    free_subscribe: str = "бесплатная"
    week_subscribe: str = "1 неделя"
    month_subscribe: str = "1 месяц"
    half_year_subscribe: str = "6 месяцев"


class CountMessageSubscribe(BaseModel):
    free_subscribe: int = 2
    week_subscribe: int = 180
    month_subscribe: int = 800
    half_year_subscribe: int = 6000


class CountDaySubscribe(BaseModel):
    free_subscribe: int = 1
    week_subscribe: int = 7
    month_subscribe: int = 30
    half_year_subscribe: int = 180


class Price(BaseModel):
    week_subscribe: float = 29000
    month_subscribe: float = 39000
    half_year_subscribe: float = 190000


class TypeAI(BaseModel):
    write: str = "что ей написать?"
    say: str = "что ей ответить?"
