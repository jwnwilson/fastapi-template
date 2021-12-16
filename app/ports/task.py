from pydantic import BaseModel


class TaskArgs(BaseModel):
    args: list
    kwargs: dict


class TaskOutData(BaseModel):
    task_id: int
    status: str
    data: dict


class TaskAdapter:
    def create_task(self, task_name: str, task_args: TaskArgs) -> TaskOutData:
        raise NotImplementedError

    def get_task(self, task_id: int) -> TaskOutData:
        raise NotImplementedError