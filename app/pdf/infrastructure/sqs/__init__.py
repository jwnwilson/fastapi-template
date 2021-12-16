from ...ports.task import TaskAdapter, TaskArgs, TaskOutData


class SqsTaskAdapter(TaskAdapter):
    def create_task(task_name: str, task_args: TaskArgs) -> TaskOutData:
        pass

    def get_task(task_id: int) -> TaskOutData:
        pass