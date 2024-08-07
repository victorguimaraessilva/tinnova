FROM python:3-alpine

WORKDIR /usr/src/app

RUN mkdir /usr/src/app/staticfiles

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]