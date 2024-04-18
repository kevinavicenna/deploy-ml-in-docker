FROM tensorflow/tensorflow:latest

WORKDIR /models/app

COPY load.py requirements.txt /models/app
COPY requirements.txt models/app/requirements.txt

RUN apt update && \
    apt install -y python3-pip && \
    pip install -r requirements.txt 

EXPOSE 8502:8502

ENTRYPOINT ["streamlit", "run", "load.py", "--server.port=8502", "--server.address=0.0.0.0"]
