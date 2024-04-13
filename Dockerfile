FROM  python:3.11.1-alpine

WORKDIR /core

COPY requirements.txt .

RUN echo "Installing Dependencies"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD [ "python", "manage.py" , "runserver","0.0.0.0:8000" ]