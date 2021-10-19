FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2020.03
RUN pip install xgboost==1.0.2
RUN pip install scikit-learn==0.22.1

WORKDIR /repo
COPY ./repo
