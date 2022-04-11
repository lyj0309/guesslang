FROM python:3.10


WORKDIR /app
# install requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9000
ENTRYPOINT [ "python3","index.py" ]