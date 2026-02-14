FROM python:3.10-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Setting up environment for Encoding fix
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    gnupg2 \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install --upgrade pip

WORKDIR /app

# Install Pyrogram and TgCrypto first to avoid version issues
RUN pip3 install -U pyrogram tgcrypto

COPY requirements.txt .

# Install other python dependencies
RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python3", "bot.py"]
