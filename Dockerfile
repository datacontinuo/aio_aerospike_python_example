FROM python:3.11.1

ENV INSTALL_PATH /app_install

RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt



#Default command
RUN mkdir /keys
RUN mkdir /conf
RUN mkdir /app
WORKDIR /app

COPY src . 

VOLUME ["/app"]

CMD  uvicorn main:app --reload
