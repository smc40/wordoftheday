# Taken from https://www.section.io/engineering-education/how-to-deploy-streamlit-app-with-docker/

# Firstly we define our base image where we want to build our file from, as demostrated below.
FROM python:3.8

# Create a working directory
WORKDIR ./app

# Coppy the needed files
COPY app/app.py ./app.py
COPY requirements.txt ./requirements.txt

# Install the requirements
RUN pip install -r requirements.txt

# Expose the port to be used to run the application
EXPOSE 8501

# Create an entry point to make our image executable
ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]