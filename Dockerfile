FROM python:3.12-alpine

RUN apk add --no-cache nginx tini

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /var/www/html/index.html
COPY server.py .

EXPOSE 80

ENTRYPOINT ["/sbin/tini", "--", "sh", "-c", "nginx && exec python server.py"]
