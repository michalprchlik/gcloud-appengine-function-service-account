FROM python:3.8.12-slim

RUN pip install --upgrade pip

RUN useradd -ms /bin/bash  appuser
USER appuser
WORKDIR /home/appuser

COPY --chown=appuser:appuser requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/appuser/.local/bin:${PATH}"
ENV TEST_IN_CONTAINER=True

COPY --chown=appuser:appuser . .

CMD ["manage.py", "test"]
ENTRYPOINT ["python3"]
