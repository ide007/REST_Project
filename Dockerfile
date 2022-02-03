FROM python:3.10.1

RUN pip install --upgrade pip
COPI ./ ./
RUN pip install -r requirements.txt
RUN pip install gunicorn
