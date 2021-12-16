from ..domain.pdf import create_pdf
from ..ports.pdf import PdfOutData
from ..ports.task import TaskAdapter


def get_pdf(task_adapter: TaskAdapter, pdf_id: str) -> PdfOutData:
    """[summary]

    Args:
        html (str): [description]
        file_path (str): [description]

    Returns:
        [type]: [description]
    """
    # return pdf task data
    return task_adapter.get_task(pdf_id)
