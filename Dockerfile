FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

# Setting up environment for Encoding fix
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    locales \
    build-essential \
    curl \
    git \
    gnupg2 \
    wget \
    busybox \
    python3 \
    python3-dev \
    python3-pip \
    python3-lxml \
    pv \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install required setup tools
RUN pip3 install --upgrade pip
RUN pip3 install setuptools wheel yarl multidict

# Force install latest Pyrogram to fix 'enums' import error
RUN pip3 install -U pyrogram tgcrypto

WORKDIR /app
COPY requirements.txt .

# Install other python dependencies
RUN pip3 install -r requirements.txt

RUN dpkg-reconfigure locales
COPY . /app

CMD ["python3", "bot.py"]
