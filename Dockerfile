from debian

RUN apt update -y && apt install -y python3 python-pip && pip install feedparser Slacker

add main.py /main.py

ENTRYPOINT ["python", "main.py"]
