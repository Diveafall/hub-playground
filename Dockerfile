FROM tensorflow/tensorflow:latest

WORKDIR /app

ADD . .
RUN pip install --upgrade pip
# RUN pip3 install hub==1.0.0b5
RUN pip3 install -e ./Hub
RUN pip3 install tensorflow_datasets

CMD [ "bash", "-c", "sleep infinity" ]