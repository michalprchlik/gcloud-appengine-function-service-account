FROM python:3.8.12-slim

ENV PYTHONUNBUFFERED=1
ENV PORT=8184
ENV GUNICORN_PID_FILE=/tmp/gunicorn.pid

RUN pip install --upgrade pip

RUN useradd -ms /bin/bash  appuser
USER appuser
WORKDIR /home/appuser
ENV PATH="/home/appuser/.local/bin:${PATH}"

COPY --chown=appuser:appuser requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

EXPOSE ${PORT}

COPY --chown=appuser:appuser . .

RUN python3 manage.py test
RUN python3 manage.py collectstatic --noinput
CMD gunicorn yamp.wsgi -b 127.0.0.1:${PORT} --pid ${GUNICORN_PID_FILE} --access-logfile - --error-logfile -
