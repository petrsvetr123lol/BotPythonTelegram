FROM python:3

RUN mkdir -p /usr/src/bot
RUN pip install beautifulsoup4
RUN pip install requests
WORKDIR /usr/src/bot

COPY . .

CMD [ "python3", "main.py" ]