FROM debian:12

# Install deps
RUN apt update && apt install -y \
    python3 python3-dev python3-pip \
    build-essential \
    git \
    swig \
    libssl-dev \
    libasound2-dev \
    libopus-dev \
    libspeex-dev \
    libspeexdsp-dev \
    portaudio19-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 🔴 THIS LINE IS REQUIRED
RUN ln -s /usr/bin/python3 /usr/bin/python

# Clone PJSIP
WORKDIR /opt
RUN git clone https://github.com/pjsip/pjproject.git

# Configure
WORKDIR /opt/pjproject
RUN ./configure CFLAGS="-fPIC" --enable-shared --disable-video

# Build core
RUN make dep && make -j1 && make install

# Build Python bindings
WORKDIR /opt/pjproject/pjsip-apps/src/python
RUN make -j1 && python3 setup.py install

# Install Python dependencies
RUN pip3 install --no-cache-dir flask aiohttp --break-system-packages

ENV PYTHONPATH="/usr/local/lib/python3.11/site-packages:/usr/local/lib/python3/dist-packages"
ENV LD_LIBRARY_PATH="/usr/local/lib"



# Copy service files
COPY sip_service.py /app/sip_service.py
COPY run.sh /run.sh

RUN chmod +x /run.sh

CMD ["/run.sh"]
