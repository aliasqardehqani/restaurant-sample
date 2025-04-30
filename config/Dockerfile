FROM 110.112.55.18:6061/python:3.9-slim

EXPOSE 8008

WORKDIR /app    

COPY requirements.txt


RUN pip install --trusted-host 110.112.55.18 -i http://110.112.55.18/repository/pypi_group/simple/ --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8008"]
