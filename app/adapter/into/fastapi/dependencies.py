from ....infrastructure.sqs import SqsTaskAdapter

def get_sqs_adapater() -> SqsTaskAdapter:
    return SqsTaskAdapter()

    