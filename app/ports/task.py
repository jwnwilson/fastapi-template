from pydantic import BaseModel


class TaskArgs(BaseModel):
    args: list
    kwargs: dict


class TaskData(BaseModel):
    task_id: int
    task_name: str
    status: str
    data: dict
    result: dict


class TaskAdapter:
    def create_task(self, task_name: str, task_args: TaskArgs) -> TaskData:
        raise NotImplementedError

    def get_task(self) -> TaskData:
        raise NotImplementedError