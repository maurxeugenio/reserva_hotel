# Use the base Python image
FROM python:3.11.4-alpine

# Set working directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy entrypoint script
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Make entrypoint script executable
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy the rest of the application code
COPY . /usr/src/app/
EXPOSE  2525
# Set entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
