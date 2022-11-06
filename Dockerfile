FROM python:3.7

LABEL Maintainer="Raeveen Pasupathy <igadget28@gmail.com>"

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY . /app

# Run server
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]