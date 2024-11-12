FROM python:3.12-slim

WORKDIR /usr/local/test

COPY requirements.txt ./
COPY features ./

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps

VOLUME ["./allure-results"]

ENTRYPOINT ["sh", "-c", "behave -f allure_behave.formatter:AllureFormatter -o ./allure-results ./features"]

