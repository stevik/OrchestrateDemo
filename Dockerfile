FROM python:3.10
WORKDIR /OrchestrateDemo
COPY . /OrchestrateDemo/
RUN pip3 install -r requirements.txt
CMD ["pytest", "-v"]
