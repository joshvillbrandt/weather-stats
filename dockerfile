FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/workspace"

ENV APP_CACHE_DIR "/workspace"

WORKDIR /workspace
COPY . /workspace

RUN pip install --trusted-host pypi.python.org --upgrade pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt

CMD python src/run.py
