FROM python:3.10.7-alpine3.16

ARG FLASK_APP=app.py
ARG FLASK_RUN_HOST=0.0.0.0
ARG FLASK_ENV=production

WORKDIR /usr/local/share/rpn

RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install Flask python-dotenv watchdog redis

ENV FLASK_APP=${FLASK_APP}
ENV FLASK_RUN_HOST=${FLASK_RUN_HOST}
ENV FLASK_ENV=${FLASK_ENV}

EXPOSE 5000
CMD ["flask", "run"]