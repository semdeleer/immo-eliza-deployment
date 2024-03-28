FROM python:3.12.2
COPY . ./app
WORKDIR /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "--server.address", "127.0.0.1", "./steamlit.py"]