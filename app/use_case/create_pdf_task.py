from domain.task import TaskEntity
from ports.pdf import PdfInData
from ports.task import TaskAdapter, TaskData
from ports.db import DbAdapter
from ports.storage import StorageAdapter


def create_pdf(
    event_adapter: TaskAdapter, db_adapter: DbAdapter, storage_adapter: StorageAdapter, pdf_data: PdfInData
) -> TaskData:
    """[summary]

    Args:
        html (str): [description]
        file_path (str): [description]

    Returns:
        [type]: [description]
    """
    # store html data to create pdf later
    html_url = storage_adapter.save(pdf_data)
    pdf_task_data: TaskData = TaskData(result=html_url)

    # create pdf task
    task_service = TaskEntity(event_adapter=event_adapter, db_adapter=db_adapter)
    pdf_task_data: TaskData = task_service.create_task(pdf_task_data)

    # return pdf task data
    return pdf_task_data
