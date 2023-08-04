FROM python

WORKDIR /alfis

COPY ["main.py", "utils.py", "config.py", "./"]

RUN pip install aiogram apscheduler

ENV ALFIS_DB_PATH

ENV ALFIS_DB_FILE

ENV SCHEDULE_SECONDS

ENV ALERT_TIME

ENV ALERT_SECONDS

VOLUME /alfis

ENTRYPOINT ["python"]

CMD ["main.py"]


