FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app/
COPY . /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 9207
RUN chmod +x /app/deploy.sh
CMD ["/app/deploy.sh"]