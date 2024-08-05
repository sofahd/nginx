# Use debian:slim as the base image
FROM debian:stable-slim

ARG CREATE_CERT
ENV CREATE_CERT=${CREATE_CERT}
ARG CN
ENV CN=${CN}
ARG C
ENV C=${C}
ARG ST
ENV ST=${ST}
ARG L
ENV L=${L}
ARG O
ENV O=${O}
ARG OU
ENV OU=${OU}

# Install nginx-extras
RUN apt-get update && \
    apt-get install -y nginx-extras \
    python3 \
    python3-pip \
    python3-dev \
    python3-requests && \
    rm -rf /var/lib/apt/lists/*

# Remove the default Nginx configuration file
RUN rm /etc/nginx/sites-enabled/default

# Add a new configuration file for Nginx as a reverse proxy
COPY nginx.conf /etc/nginx/sites-available/default.conf

# Create a symbolic link to enable the configuration
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf

COPY cert_script.py /cert_script.py

RUN mkdir /etc/nginx/ssl

RUN python3 /cert_script.py ${CREATE_CERT} ${CN} ${OU} ${O} ${L} ${ST} ${C}

# Use the exec form of CMD to run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]