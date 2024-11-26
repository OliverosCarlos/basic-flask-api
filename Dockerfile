FROM python:3.12-alpine

WORKDIR /src

COPY requirements.txt /src
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /src

ENTRYPOINT ["python3"]
CMD ["app.py"]