FROM python:3.12.2-bullseye
LABEL authors="shengyou"

ENTRYPOINT ["top", "-b"]