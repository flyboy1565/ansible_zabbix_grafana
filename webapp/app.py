from dataclasses import dataclass
from typing import List, Optional, Dict, Any

from litestar import Litestar, get, post, put
from litestar.exceptions import NotFoundException

from litestar import status_codes
from random import choice


def random_response_code():
    code_name = choice(status_codes.__all__)
    code = status_codes.__dict__[code_name]
    return code, code_name

@dataclass
class TodoItem:
    title: str
    done: bool


TODO_LIST: List[TodoItem] = [
    TodoItem(title="Start writing TODO list", done=True),
    TodoItem(title="???", done=False),
    TodoItem(title="Profit", done=False),
]

STATUS = {
    "value1": False,
    "value2": True
}


def get_todo_by_title(todo_name) -> TodoItem:
    for item in TODO_LIST:
        if item.title == todo_name:
            return item
    raise NotFoundException(detail=f"TODO {todo_name!r} not found")


@get("/")
async def get_list(done: Optional[bool] = None) -> List[TodoItem]:
    if done is None:
        return TODO_LIST
    return [item for item in TODO_LIST if item.done == done]


@post("/")
async def add_item(data: TodoItem) -> List[TodoItem]:
    TODO_LIST.append(data)
    return TODO_LIST


@put("/{item_title:str}")
async def update_item(item_title: str, data: TodoItem) -> List[TodoItem]:
    todo_item = get_todo_by_title(item_title)
    todo_item.title = data.title
    todo_item.done = data.done
    return TODO_LIST


@get("/status/{key:str}")
async def get_status(key: str) -> bool:
    return STATUS[key]


@get("/post/{key:str}/{value:str}")
async def set_status(key: str, value: str) -> Dict[str, str]:
    if value.strip().lower() == "true":
        STATUS[key] = True
    elif value.strip().lower() == "false":
        STATUS[key] = False
    return STATUS


@get("/get_teapot", status_code=status_codes.HTTP_418_IM_A_TEAPOT, media_type="application/problem+json")
async def retrieve_resource() -> dict[str, Any]:
    return {
        "title": "This should return a 418 response",
        "type": "Server delusion",
        "status": status_codes.HTTP_418_IM_A_TEAPOT,
    }


@get("/get_random_response_code", media_type="application/problem+json")
async def get_random_response_code() -> dict[str, Any]:
    status_code, code_type = random_response_code()
    return {
        "title": f"This should return a random status code response. {code_type}",
        "type": "Server delusion",
        "status": status_code,
    }

handlers = [get_list, add_item, update_item, get_status, set_status, retrieve_resource, get_random_response_code]
app = Litestar(handlers)
