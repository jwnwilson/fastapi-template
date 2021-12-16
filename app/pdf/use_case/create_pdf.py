from ..domain.pdf import create_pdf
from ..ports.pdf import PdfInData, PdfOutData
from ..ports.task import TaskAdapter


def create_pdf(task_adapter: TaskAdapter, pdf_data: PdfInData) -> PdfOutData:
    """[summary]

    Args:
        html (str): [description]
        file_path (str): [description]

    Returns:
        [type]: [description]
    """
    # create pdf task
    pdf_out_data: PdfOutData = task_adapter.create_task(pdf_data)

    # return pdf task data
    return pdf_out_data
