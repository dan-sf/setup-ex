FROM python:3.6-slim

ENV PYTHONPATH=/code

COPY . /code

RUN cd /code && pip install -e .

CMD se

# docker build -t test-py-dev .
# docker run --rm -it -v $(pwd):/src test-py-dev

