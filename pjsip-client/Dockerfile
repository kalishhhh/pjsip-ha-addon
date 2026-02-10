FROM debian:12

RUN apt update && apt install -y \
    baresip \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
