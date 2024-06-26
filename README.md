# SOFAH Nginx Service

The SOFAH (Speedy Open Framework for Automated Honeypot-development) project simplifies the creation and deployment of honeypots, with a particular focus on IoT devices. This README provides details on the Nginx service component of SOFAH, which is configured and managed automatically by the ENNORM module to act as a reverse proxy.

## Overview

Within the SOFAH framework, the Nginx service is deployed as a reverse proxy to manage traffic to various honeypot services. Leveraging the ENNORM module, it automatically configures the Nginx service based on the generated datasets, streamlining the setup process and enhancing the honeypots' realism and effectiveness.

## Getting Started

### Prerequisites

- Docker installed on your system.
- The SOFAH framework set up, including the ENNORM module.

### Automated Setup by ENNORM

The ENNORM module automatically handles the configuration and deployment of the Nginx service, based on the analysis and normalization of honeypot data. This section outlines the general flow, assuming you have SOFAH and its components ready:

1. **ENNORM Module**: Processes the collected data, preparing configurations for various services, including Nginx.
2. **Nginx Configuration**: Automatically generated by ENNORM, tailored to route traffic efficiently to the simulated services.
3. **Deployment**: The Dockerfile provided in the SOFAH Nginx service directory is utilized by ENNORM to build and run the Nginx container, applying the generated configuration.

### Manual Adjustments (If Necessary)

While ENNORM automates the setup, manual adjustments to the Nginx configuration might be necessary for specific scenarios or advanced customizations:

- **Custom Configuration**: Modifications to `nginx.conf` can be made before initiating the ENNORM process or directly within the generated Docker container for runtime adjustments.
- **Advanced Routing**: For complex traffic routing or additional reverse proxy features, manual edits to the Nginx configuration files may be required.

## Features

- **Automated Configuration**: Seamlessly integrated with the ENNORM module for data-driven setup.
- **Reverse Proxy Functionality**: Directs incoming traffic to the appropriate honeypot services, simulating a realistic network environment.
- **Efficient and Secure**: Builds upon `debian:stable-slim`, ensuring a minimal footprint and reduced security vulnerabilities.
