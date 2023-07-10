FROM python

WORKDIR /alfis

COPY ["main.py", "utils.py", "config.py", "./"]

RUN pip install aiogram motor pymongo apscheduler

ENV ALFIS_DB_PATH="/db"

ENV ALFIS_DB_FILE="blockchain.db"

ENV SCHEDULE_SECONDS=60

ENTRYPOINT ["python"]

CMD ["main.py"]


