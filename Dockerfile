FROM python:3.10.12-slim

RUN pip install --no-cache-dir --upgrade pip telegram-notifier-bot

COPY tg_notifier_send.py /tg_notifier_send.py

ENTRYPOINT ["python", "/tg_notifier_send.py"]
