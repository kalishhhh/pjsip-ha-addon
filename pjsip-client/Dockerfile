FROM debian:12

# Install runtime dependencies only
RUN apt update && apt install -y \
    python3 \
    python3-pip \
    libasound2 \
    libssl3 \
    libopus0 \
    libspeex1 \
    libspeexdsp1 \
    portaudio19-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Make python available as `python`
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install Python dependencies (THIS IS THE KEY)
RUN pip3 install --no-cache-dir \
    flask \
    aiohttp \
    pjsua2 \
    --break-system-packages

# Copy service files
COPY sip_service.py /app/sip_service.py
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
