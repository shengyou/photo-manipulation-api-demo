FROM python:3.12.2-bullseye
LABEL authors="shengyou"

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY utils.py .

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
