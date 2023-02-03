FROM python:3.10

ENV PYTHONUNBUFFERED: 1

WORKDIR ./fastApiProject

RUN pip install --upgrade pip

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . ./fastApiProject

EXPOSE 8000

CMD ["uvicorn", "fastApiProject.main", "--host", "0.0.0.0", "--port", "8000"]