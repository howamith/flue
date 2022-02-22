# Project modules.
from server import tasks

# Flask modules.
from flask import Blueprint, request
from flask.typing import ResponseValue

api = Blueprint("api", __name__, url_prefix="/api")


@api.post("/start_task")
def start_task() -> ResponseValue:
    data = request.get_json()

    task = tasks.long_task.delay(data["name"], int(data["time"]))
    return {"state": "Task starting...", "task_id": task.id}


@api.get("/task_status/<task_id>")
def task_status(task_id: str) -> ResponseValue:
    task = tasks.long_task.AsyncResult(task_id)
    if task.successful():
        response = task.get()
    else:
        status = (
            str(task.info) if task.failed() else task.info.get("status", "")
        )
        response = {
            "state": task.state,
            "current": task.info.get("current", 0),
            "total": task.info.get("total", 1),
            "status": status,
        }
    return response
