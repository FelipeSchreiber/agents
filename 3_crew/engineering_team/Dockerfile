FROM python:3.11-slim

# Install Docker CLI
RUN apt-get update && \
    apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

# Set up crewai
WORKDIR /crewai
COPY . /crewai
RUN pip install -e .

CMD ["/bin/bash"]
