FROM python:3.7
LABEL maintainer="info@optimum-web.com"

ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
    python-dev \
    curl \
    locales \
    gcc \
    make \
    libc6-dev \
    libpq-dev \
    libffi-dev \
    uwsgi-src \
    uuid-dev \
    libcap-dev \
    libpq5\
    git \
    curl \
    supervisor \
    unzip \
    procps \
    uwsgi \
    && apt-get clean && rm -rf /var/lib/apt/lists/*; \
    groupadd -r -g 2000 flask; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/flask -s /bin/bash flask

# Set the locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install uwsgi
COPY supervisord.conf /etc/supervisord.conf
COPY src/flask_app.tar.gz .
RUN pip install git+https://github.com/Supervisor/supervisor
