FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install xgboost==1.2.0
RUN pip install scikit-learn==1.0.1

WORKDIR /repo
COPY ./repo
