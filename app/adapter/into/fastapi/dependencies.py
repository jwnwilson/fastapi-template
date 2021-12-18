from ports.task import TaskAdapter
from ports.db import DbAdapter
from infrastructure.sqs import SqsTaskAdapter
from infrastructure.db import DynamoDbAdapter


def get_task_adapater() -> TaskAdapter:
    return SqsTaskAdapter()


def get_db_adapater() -> DbAdapter:
    return DynamoDbAdapter()