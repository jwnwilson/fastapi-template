from fastapi import APIRouter, Depends, HTTPException

from .....use_case import create_pdf, get_pdf
from .....ports.pdf import PdfInData, PdfOutData
from ..dependencies import get_sqs_adapater


router = APIRouter(
    prefix="/pdf",
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create_pdf_route(pdf_data: PdfInData, task_adapter = Depends(get_sqs_adapater)):
    # call create use case
    pdf_task_data: PdfOutData = create_pdf(task_adapter, pdf_data)
    # return pdf id with pdf job data
    return pdf_task_data


@router.get("/{pdf_id}")
async def get_pdf_route(pdf_id: str, task_adapter = Depends(get_sqs_adapater)):
    # Attempt to get pdf data by id
    return get_pdf(task_adapter, pdf_id)