FROM python:3.10-slim

# Обновление и установка всех нужных пакетов
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    gnupg \
    firefox-esr \
    xvfb \
    wget \
    tar \
    && rm -rf /var/lib/apt/lists/*

# Установка geckodriver (фиксированная версия)
ENV GECKO_VERSION v0.34.0

RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/${GECKO_VERSION}/geckodriver-${GECKO_VERSION}-linux64.tar.gz" && \
    tar -xzf "geckodriver-${GECKO_VERSION}-linux64.tar.gz" -C /usr/local/bin && \
    rm "geckodriver-${GECKO_VERSION}-linux64.tar.gz"

# Создание рабочей директории
WORKDIR /app

# Копируем проект
COPY . /app

# Установка зависимостей Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Запуск pytest с xvfb
ENTRYPOINT ["xvfb-run", "pytest"]
