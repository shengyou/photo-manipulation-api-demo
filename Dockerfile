FROM python:3.12.2-bullseye as builder

WORKDIR /app

COPY requirements.txt .

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install uv && \
    uv venv && \
    uv pip install --no-cache-dir -r requirements.txt

FROM python:3.12.2-slim-bullseye as runner

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY main.py .
COPY utils.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
