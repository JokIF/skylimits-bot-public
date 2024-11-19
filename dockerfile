FROM --platform=linux/amd64 python:3.10.11-slim-bullseye

ENV PYTHONPATH="${PYTHONPATH}:/app"

WORKDIR /app

RUN set +x \
    && apt update \
    && apt upgrade -y \
    && apt install -y netcat

COPY . /app

RUN pip install -r requirements.txt
RUN chmod +x /app/script/entrypoint.sh \
    && cd /bin \ 
    && ln -s /app/script/entrypoint.sh
    

ENTRYPOINT ["entrypoint.sh"]
