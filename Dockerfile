FROM python:3.12.2
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8501
COPY ./app
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit.py"]