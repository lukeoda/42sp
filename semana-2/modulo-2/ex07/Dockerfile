FROM python:3.12.10-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]


#para instalar basta digitar os comandos
#docker build -t minha_api .
#docker run -d -p 8000:8000 minha_api
