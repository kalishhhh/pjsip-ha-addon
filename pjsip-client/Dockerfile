FROM debian:12
RUN apt update && apt install -y \
    python3 python3-pip \
    python3-dev \
    build-essential \
    swig \
    libssl-dev \
    libasound2-dev \
    libpjsua2 \
    && rm -rf /var/lib/apt/lists/*

# Install Flask
RUN pip3 install flask

COPY sip_service.py /app/sip_service.py
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
