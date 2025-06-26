FROM python:3.12.10-bullseye

WORKDIR /app

COPY /newsite .
COPY /public .

ENTRYPOINT ["python3", "-m", "http.server"]
CMD ["8000"]


# # CMD define os valores *padrão*.  Serão sobrescritos no docker run.
