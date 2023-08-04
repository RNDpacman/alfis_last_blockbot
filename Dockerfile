FROM python

WORKDIR /alfis

COPY ["main.py", "utils.py", "config.py", "./"]

RUN pip install aiogram apscheduler

ENV ALFIS_DB_PATH="."

ENV ALFIS_DB_FILE="blockchain.db"

ENV SCHEDULE_SECONDS=64

ENV ALERT_TIME=600

ENV ALERT_SECONDS=1024

VOLUME /alfis

ENTRYPOINT ["python"]

CMD ["main.py"]


