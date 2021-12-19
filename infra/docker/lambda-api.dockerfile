FROM public.ecr.aws/lambda/python:3.8

# Install libraries
RUN apt-get update && \
    apt-get install -y \
    wkhtmltopdf

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* ${LAMBDA_TASK_ROOT}

RUN bash -c "poetry install --no-root --no-dev"

ADD ./app ${LAMBDA_TASK_ROOT}

CMD ["app.adapter.fastapi.lambda.handler"]