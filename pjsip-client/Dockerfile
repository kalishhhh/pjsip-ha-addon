FROM debian:12

ENV DEBIAN_FRONTEND=noninteractive

# 1️⃣ Install build dependencies
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
    libportaudio2 \
    portaudio19-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 2️⃣ Clone PJSIP
WORKDIR /opt
RUN git clone https://github.com/pjsip/pjproject.git

# 3️⃣ Configure PJSIP (enable pjsua2 + Python)
WORKDIR /opt/pjproject
RUN ./configure \
    CFLAGS="-fPIC" \
    --enable-shared \
    --disable-video \
    --disable-opencore-amr \
    --disable-sdl \
    --disable-ffmpeg

# 4️⃣ Build & install
RUN make dep && make -j1 && make install

# 5️⃣ Build Python bindings
WORKDIR /opt/pjproject/pjsip-apps/src/python
RUN make -j1 && python3 setup.py install
RUN ln -s /usr/bin/python3 /usr/bin/python



# 6️⃣ Refresh linker cache
RUN ldconfig

# 7️⃣ Install Flask
RUN pip3 install flask

# 8️⃣ Copy your app
WORKDIR /app
COPY sip_service.py /app/sip_service.py
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
