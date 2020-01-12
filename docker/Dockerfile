FROM python:3.7-alpine
EXPOSE 5000

WORKDIR /twittercollector
COPY . .
RUN apk add --update --no-cache --virtual .build-deps \
        g++ \
        python-dev \
        libxml2 \
        libxml2-dev && \
    apk add libxslt-dev && \
    pip install --no-cache-dir -r req.txt && \
    apk del .build-deps

#CMD []