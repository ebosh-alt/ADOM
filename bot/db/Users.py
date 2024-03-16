from collections import namedtuple
from typing import Iterator, Optional, Type

from .SQLite import Sqlite3_Database
from ..config import link_to_bot
from .models import TypeSubscribe, TypeAI


class User:
    def __init__(self, id, **kwargs):
        """
        :param id: int;
        :param kwargs:
        count_message: int;
        count_day: int;
        username: str;
        ref_link: str;
        subscribe: Subscribe;
        """
        self.id: int = id
        if len(kwargs):
            self.count_message: int = kwargs.get("count_message")
            self.count_day: int = kwargs.get("count_day")
            self.username: Optional[str] = kwargs.get("username")
            self.ref_link: str = kwargs.get("ref_link")
            self.subscribe: str = kwargs.get("subscribe")
            self.type_ai: str = kwargs.get("type_ai")

        else:
            self.count_message: int = 10
            self.count_day: int = 3
            self.username: Optional[str] = None
            self.ref_link: str = f"{link_to_bot}?start={self.id}"
            self.subscribe: str = TypeSubscribe().free_subscribe
            self.type_ai: str = TypeAI().write

    def __iter__(self):
        dict_class = self.__dict__
        Result = namedtuple("Result", ["name", "value"])
        for attr in dict_class:
            if not attr.startswith("__"):
                if attr != "flag":
                    yield Result(attr, dict_class[attr])
                else:
                    yield Result(attr, dict_class[attr].value)


class Users(Sqlite3_Database):
    def __init__(self, db_file_name, table_name, *args) -> None:
        Sqlite3_Database.__init__(self, db_file_name, table_name, *args)
        self.len = 0

    def add(self, obj: User) -> User | None:
        self.add_row(obj)
        self.len += 1
        return self.get(obj.id)

    def __len__(self):
        return self.len

    def __delitem__(self, key):
        self.del_instance(key)
        self.len -= 1

    def __iter__(self) -> Iterator[User]:
        keys = self.get_keys()
        for id in keys:
            user = self.get(id)
            yield user

    def get(self, id: int) -> User | None:
        if id in self:
            obj_tuple = self.get_elem_sqllite3(id)
            obj = User(
                id=obj_tuple[0],
                count_message=obj_tuple[1],
                count_day=obj_tuple[2],
                username=obj_tuple[3],
                ref_link=obj_tuple[4],
                subscribe=obj_tuple[5],
                type_ai=obj_tuple[6],
            )
            return obj
        return None
