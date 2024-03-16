FROM python:3.12


WORKDIR /usr/src/tests

COPY . .
COPY infra C:\Users\odehm\Desktop\new\AirbnbSeleniumGridProject\infra
COPY logic C:\Users\odehm\Desktop\new\AirbnbSeleniumGridProject\logic



RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install unzip
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*



#docker run --name aya -e PYTHONPATH=/usr/src/tests/AirbnbSeleniumGridProject -v C:/Users/odehm/Desktop/new/AirbnbSeleniumGridProject/infra:/usr/src/tests/AirbnbSeleniumGridProject/infra tests:latest python test/tankerkoenig_stats_api_test.py

