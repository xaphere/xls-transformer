# XLS transfomer

This is a small utility service that transforms xls files to csv upon request. It is not intended in any way, shape or form to be used for something serious.

## Local build

```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Local run

```
export FLASK_APP=app.py && \
flask run
```

## Containered run

```
docker build -t transformer:latest .
docker run -p 8080:5000 -t transformer:latest
```

## API
Currently there is only single endpoint:

```yml
openapi: 3.0.1
info:
  title: XLS Transfomer
  version: 1.0.0
paths:
  /transform:
    post:
      summary: transform xls file
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                fileURL:
                  type: string
                  description: Location from where the xml file could be downloaded
                  example: "https://www.parliament.bg/pub/StenD/20170425094229iv190417.xls"
        required: true
      responses:
        200:
          content:
            text/html; charset=utf-8:
              schema:
                type: string
                example: |
                  0,,,,,1,2,3,4,5,,6,7,8
                  1,АДЛЕН ШУКРИ ШЕВКЕД,,1245.0,ДПС,П,+,+,+,+,,+,+,+
                  2,АЛБЕНА ВЛАДИМИРОВА НАЙДЕНОВА,,1246.0,ВОЛЯ,П,+,+,+,+,,+,+,+
          description: transformed file
        404:
          description: File not found
```
