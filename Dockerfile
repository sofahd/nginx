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

# Use the exec form of CMD to run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]