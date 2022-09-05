FROM python:3
WORKDIR /flask_template
COPY requirements.txt /flask_template
RUN pip install -U pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir
COPY . /flask_template
CMD [ "python", "run.py" ]