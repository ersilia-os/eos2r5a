FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2023.3.2
RUN pip install xgboost==1.2.0
RUN pip install scikit-learn==1.0.1
RUN pip install numpy==1.21.6

WORKDIR /repo
COPY . /repo
