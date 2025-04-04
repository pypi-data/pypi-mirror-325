FROM python:3.13-slim-bookworm
LABEL org.opencontainers.image.source=https://github.com/openzim/warc2zim

RUN apt-get update -y \
 && apt-get install -y --no-install-recommends \
    locales-all libmagic1 libcairo2 \
 && rm -rf /var/lib/apt/lists/* \
 && python -m pip install --no-cache-dir -U \
      pip \
 && mkdir -p /output

WORKDIR /output

# Copy pyproject.toml and its dependencies
COPY pyproject.toml README.md /src/
COPY src/warc2zim/__about__.py /src/src/warc2zim/__about__.py

# Install Python dependencies
RUN pip install --no-cache-dir /src

# Copy code + associated artifacts
COPY src /src/src
COPY *.md /src/

# Install + cleanup
RUN pip install --no-cache-dir /src \
 && rm -rf /src

CMD ["warc2zim", "--help"]
