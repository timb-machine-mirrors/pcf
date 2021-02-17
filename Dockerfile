FROM python:3.8
ADD . /code
WORKDIR /code
RUN pip install -r requirements_unix.txt
CMD if [ ! -e "./configuration/database.sqlite3" ]; then echo 'DELETE_ALL' | python new_initiation.py; fi; python app.py