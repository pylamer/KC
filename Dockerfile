FROM python
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY main.py main.py
COPY utils.py utils.py
ENV FLASK_PORT=5000
EXPOSE $FLASK_PORT
CMD python ./main.py