FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN conda install -c conda-forge libstdcxx-ng=14.2.0
RUN pip install rdkit==2023.3.2
RUN pip install xgboost==1.5.0
RUN pip install scikit-learn==1.0.1
RUN pip install numpy==1.23.5

WORKDIR /repo
COPY . /repo
