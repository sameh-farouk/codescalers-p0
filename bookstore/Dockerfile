# pull official base image
FROM python:3.9.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.dev.txt .
RUN pip install -r requirements.dev.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .



# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]