# Use debian:slim as the base image
FROM debian:stable-slim

# Install nginx-extras
RUN apt-get update && \
    apt-get install -y nginx-extras && \
    rm -rf /var/lib/apt/lists/*

# Remove the default Nginx configuration file
RUN rm /etc/nginx/sites-enabled/default

# Add a new configuration file for Nginx as a reverse proxy
COPY nginx.conf /etc/nginx/sites-available/default.conf

# Create a symbolic link to enable the configuration
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf

# TLS material. For a TLS pot, ennorm's cert_forge writes the look-alike cert/key into ./ssl
# at deploy time (NginxHoneypot.download_repo) and nginx.conf points ssl_certificate at these
# paths. For a plain-HTTP pot the directory is empty. Baked in at build, so it stays valid
# under the container's read-only root filesystem.
COPY ssl/ /etc/nginx/ssl/

# Use the exec form of CMD to run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
