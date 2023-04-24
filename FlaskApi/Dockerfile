FROM python

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "NBPRequests.py"]

