from pydantic import BaseModel


class Subscribe(BaseModel):
    free_subscribe: str = "бесплатная"
    week_subscribe: str = "1 неделя"
    month_subscribe: str = "1 месяц"
    half_year_subscribe: str = "6 месяцев"


