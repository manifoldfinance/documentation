FROM python:3.9.2-alpine3.13

# Build-time flags
ARG WITH_PLUGINS=true

# Environment variables
ENV PACKAGES=/usr/local/lib/python3.9/site-packages
ENV PYTHONDONTWRITEBYTECODE=1

# Set build directory
WORKDIR /tmp

# Copy files necessary for build
COPY material material
COPY MANIFEST.in MANIFEST.in
COPY package.json package.json
COPY README.md README.md
COPY requirements.txt requirements.txt
COPY setup.py setup.py

# Perform build and cleanup artifacts and caches
RUN \
  apk upgrade --update-cache -a \
&& \
  apk add --no-cache \
    cairo \
    freetype-dev \
    git \
    git-fast-import \
    jpeg-dev \
    openssh \
    zlib-dev \
&& \
  apk add --no-cache --virtual .build \
    gcc \
    libffi-dev \
    musl-dev \
&& \
  pip install --no-cache-dir . \
&& \
  if [ "${WITH_PLUGINS}" = "true" ]; then \
    pip install --no-cache-dir \
      "mkdocs-minify-plugin>=0.3" \
      "mkdocs-redirects>=1.0"; \
  fi \
&& \
  apk del .build \
&& \
  for theme in mkdocs readthedocs; do \
    rm -rf ${PACKAGES}/mkdocs/themes/$theme; \
    ln -s \
      ${PACKAGES}/material \
      ${PACKAGES}/mkdocs/themes/$theme; \
  done \
&& \
  rm -rf /tmp/* /root/.cache \
&& \
  find ${PACKAGES} \
    -type f \
    -path "*/__pycache__/*" \
    -exec rm -f {} \;

# Set working directory
WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8000

# Start development server by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
