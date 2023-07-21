FROM python

WORKDIR /alfis

COPY ["main.py", "utils.py", "config.py", "./"]

RUN pip install aiogram apscheduler

ENV ALFIS_DB_PATH="/db"

ENV ALFIS_DB_FILE="blockchain.db"

ENV SCHEDULE_SECONDS=60

VOLUME /alfis

ENTRYPOINT ["python"]

CMD ["main.py"]


