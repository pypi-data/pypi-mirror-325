# Frappe Setup

A Python package to automate Frappe Framework setup with Docker for local development. This tool simplifies the process of setting up Frappe/ERPNext development environment using Docker containers.

## System Requirements

Before installation, ensure your system meets these requirements:

### Software Requirements
- Python 3.6 or higher
- pip (Python package manager)
- Docker Engine
- Docker Compose
- Visual Studio Code
- Git

### Hardware Requirements
- Minimum 4GB RAM (8GB recommended)
- 20GB free disk space
- x86_64 processor architecture

### Operating System
- Ubuntu 20.04 or higher (primary support)
- Other Linux distributions (may work but not officially supported)

## Pre-Installation Steps

1. Install Docker (if not already installed):

## Installation

Access your site at: http://development.localhost:8000

Default credentials:
- Username: Administrator
- Password: admin

## Uninstallation

### Method 1: Using CLI (Recommended)

1. Run the uninstall command: 


## Development Notes

- The development environment runs in a Docker container
- Code changes are synchronized in real-time
- Use VS Code's integrated terminal for bench commands
- Development site uses .localhost domain for local development

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details

## Support

- GitHub Issues: [Create an issue](https://github.com/yourusername/frappe-setup/issues)
- Documentation: [Frappe Framework Documentation](https://frappeframework.com/docs)
- Community Forum: [Frappe Forum](https://discuss.erpnext.com/)

## Acknowledgments

- Frappe Framework Team
- Docker Community
- VS Code Remote Containers Team


# Frappe Setup Tool

A Python package to automate Frappe Framework setup with Docker.

## Table of Contents
- [Installation Guide](#installation-guide)
- [Usage Guide](#usage-guide)
- [Uninstallation Guide](#uninstallation-guide)
- [Troubleshooting](#troubleshooting)
- [System Requirements](#system-requirements)
- [Directory Structure](#directory-structure)
- [Common Issues](#common-issues)

## System Requirements

### Software Requirements
- Python 3.6+
- Docker
- Docker Compose
- Visual Studio Code
- Git

### Hardware Requirements
- Minimum 5GB disk space
- 4GB RAM recommended
- Stable internet connection

## Installation Guide

### 1. Install Package

This command will:
- Clone the frappe_docker repository
- Set up development container configurations
- Install VS Code Remote Container extension

### 4. Setup Bench and ERPNext

This command will:
- Initialize the development container
- Set up Frappe Bench
- Configure database and Redis
- Create a new site
- Install ERPNext

### 5. Access Your Site
- URL: http://development.localhost:8000
- Username: Administrator
- Password: admin

## Usage Guide

### Development Environment
1. Navigate to your project directory
2. Open VS Code: `code .`
3. Click "Reopen in Container" when prompted
4. Wait for container setup to complete

### Container Management

Verify frappe-setup installation
which frappe-setup
Check Python version
python --version
Check Docker status
sudo systemctl status docker
bash
Fix directory permissions
sudo chown -R $USER:$USER my_frappe_project
bash
Restart Docker service
sudo systemctl restart docker


## Common Issues

### 1. Port Conflicts
Default ports used:
- 8000 (Web)
- 9000 (Developer)
- 3306 (Database)

Solution: Ensure these ports are available or modify docker-compose.yml

### 2. Container Access Issues
If unable to access containers:
Check container status
docker ps
View container logs
docker logs [container_name]
Restart containers
docker-compose restart


### 3. VS Code Integration
- Install "Remote - Containers" extension
- Use "Reopen in Container" when prompted
- Wait for container setup to complete

### 4. Database Issues
- Default MariaDB root password: 123
- Default site: development.localhost
- Default admin password: admin

## Important Notes

### Before Installation
- Ensure Docker is running
- Close VS Code
- Check system requirements
- Verify internet connection

### During Installation
- Don't interrupt the process
- Keep internet connection stable
- Monitor Docker logs for issues

### After Installation
- First site access might be slow
- Development mode is enabled by default
- Check all services are running

### Before Uninstallation
- Backup important data
- Stop all containers
- Close VS Code

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Support

For support, please create an issue in the GitHub repository.


This README.md provides:
Clear installation instructions
Usage guidelines
Troubleshooting steps
Common issues and solutions
System requirements
Directory structure
7. Important notes for users