FROM python:3-buster
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY app.py collect_data.py __init__.py keys.py logic_db.py mongo_config.py oauth.py flask_graylog.py /var/server/
CMD python /var/server/app.py
