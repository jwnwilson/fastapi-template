import boto3
import json

from ...ports.task import TaskAdapter, TaskArgs, TaskOutData


class SqsTaskAdapter(TaskAdapter):
    def __init__(self, config):
        # Create SQS client
        self.sqs = boto3.client('sqs')
        self.queue_url = config["queue"]

    def create_task(self, task_name: str, task_args: TaskArgs) -> TaskOutData:
        # Send message to SQS queue
        task_data = {
            "task_name": task_name,
            "task_args": task_args.to_dict()
        }
        sqs_resp = self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=(
                json.dumps(task_data)
            )
        )
        
        resp = TaskOutData(
            task_id = sqs_resp['MessageId'],
            status = "pending",
            data = sqs_resp
        )

        return resp

    def get_task(self, task_id: int) -> TaskOutData:
        sqs_resp = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )

        return TaskOutData(
            task_id = sqs_resp['MessageId'],
            status = "processing",
            data = sqs_resp
        )