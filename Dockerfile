FROM python:3.8

WORKDIR /git-noxx

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","./root.py"]
