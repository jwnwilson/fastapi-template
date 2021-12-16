import pdfkit


def create_pdf(html: str, file_path: str):
    """[summary]

    Args:
        html (str): [description]
        file_path (str): [description]

    Returns:
        [type]: [description]
    """
    return pdfkit.from_url(html, file_path)
