from domain.task import TaskEntity
from ports.pdf import PdfInData, PdfOutData
from ports.task import TaskAdapter
from ports.db import DbAdapter
from ports.storage import StorageAdapter


def create_pdf(
    event_adapter: TaskAdapter, db_adapter: DbAdapter, storage_adapter: StorageAdapter, pdf_data: PdfInData
) -> PdfOutData:
    """[summary]

    Args:
        html (str): [description]
        file_path (str): [description]

    Returns:
        [type]: [description]
    """
    # store html data to create pdf later

    pdf_data: PdfInData = PdfInData(html_url=)


    # create pdf task
    task_service = TaskEntity(event_adapter=event_adapter, db_adapter=db_adapter)
    pdf_out_data: PdfOutData = task_service.create_task(pdf_data)

    # return pdf task data
    return pdf_out_data
