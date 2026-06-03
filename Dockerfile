FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask numpy pandas scikit-learn nltk

EXPOSE 10000

CMD ["python", "app.py"]
