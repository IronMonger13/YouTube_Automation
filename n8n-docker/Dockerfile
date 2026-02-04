FROM node:20-bookworm-slim

USER root

# Install minimal dependencies
RUN apt-get update -o Acquire::Check-Valid-Until=false && \
    apt-get install -y --no-install-recommends \
        ffmpeg \
        tini \
        curl \
        ca-certificates && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install n8n
RUN npm install -g n8n

USER node

EXPOSE 5678

ENTRYPOINT ["tini", "--"]
CMD ["n8n"]
