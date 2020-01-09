
FROM alpine:3.3
MAINTAINER Vitor Lobo Ramos <lobocode@gmail.com>

RUN apk --no-cache add \
        bash \
        build-base \
        curl \
        git \
        libffi-dev \
        make \
        openssl-dev \
        python python-dev py-pip \
    && pip install virtualenv

ENV VIRTUAL_ENV=/twitterCollect/.venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
WORKDIR /twitterCollect
COPY requirements.txt .
RUN pip install -r requirements.txt

VOLUME /twitterCollect

EXPOSE 5000 3000

# Run the application:
#COPY myapp.py .
CMD ["/env/bin/python", "app.py"]
