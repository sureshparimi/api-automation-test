FROM python:3.8
ENV PYTHONBUFFERED 1
ENV APP_URL https://ssd-api.jpl.nasa.gov/cad.api
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
RUN pip install ./bin/behavex-web-1.3.4.zip
RUN pip install ./bin/behavex-xray-1.0.1.zip
ENTRYPOINT [ "bash","test.sh" ]