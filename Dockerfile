FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "MLTest_3.11", "/bin/bash", "-c"]

ENV PATH /opt/conda/envs/myenv/bin:$PATH

COPY . .

EXPOSE 8501

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "MLTest_3.11", "streamlit", "run", "main.py", "--server.address", "0.0.0.0"]

