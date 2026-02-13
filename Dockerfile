# Use the official Python base image
FROM python:3.11-alpine

# Install build essentials and development libraries.
# Added the installation of build-base, libffi-dev, and openssl-dev packages using apk. These packages provide essential
# build tools and libraries for compiling C code and building Python packages that depend on C extensions.
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    postgresql-dev \
    rust \
    cargo \
    bash
# Set work directory
WORKDIR /web/medicalka_app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1

# Create directory and copy project
COPY requirements.txt /web/requirements.txt

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /web/requirements.txt

# Copy the rest of the project
COPY . /web/medicalka_app

# Expose port
EXPOSE 8000

# # Continue with the rest of your Dockerfile
# CMD ["python", "./web/manage.py", "migrate"]
# CMD ["python", "./web/manage.py", "runserver", "0.0.0.0:8000"]
CMD ["sh", "-c", "python manage.py migrate && gunicorn medicalka_app.wsgi:application --bind 0.0.0.0:8000"]