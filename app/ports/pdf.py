from pydantic import BaseModel


class PdfInData(BaseModel):
    html: str


class PdfOutData(BaseModel):
    pdf_url: str
    task_id: int
    status: str