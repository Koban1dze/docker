FROM python:3.8.10
COPY . /server
WORKDIR /server
EXPOSE 5000
RUN pip install -r requirements.txt
CMD FLASK_APP=app.py flask run