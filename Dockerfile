FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -U setuptools
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-u", "bot.py"]
