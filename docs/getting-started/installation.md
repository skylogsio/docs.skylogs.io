---
sidebar_position: 2
title: Installation
description: Installing Skylogs using Docker and Docker Compose.
---

# Installation

This guide will walk you through installing Skylogs using Docker, the recommended and simplest installation method.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Docker**: Version 20.10 or higher
- **Docker Compose**: Version 2.0 or higher
- **Git**: For cloning the repository

## Quick Start

### Step 1: Clone the Repository

```bash
# Clone the Skylogs repository
git clone https://github.com/skylogsio/skylogs.git

# Navigate to the project directory
cd skylogs
```

### Step 2: Start Docker Containers

#### Using Stable Release (Recommended)

```bash
# Pull and start all services
docker compose up -d
```

This command will:

- Download all required Docker images
- Create and start all containers (application, database, Redis)
- Set up the network between services

#### Using Latest Version (Development)

If you want to use the latest version of Skylogs with the most recent features:

```bash
# Build and start all services from source
docker compose -f docker-compose-build.yml up -d
```

:::caution
The latest version may contain experimental features and is recommended for development or testing environments.
:::

### Step 3: Access Skylogs

Open your web browser and navigate to:

```
http://localhost:8080
```

Login with the default credentials:

- **Username**: `admin`
- **Password**: `123456`

:::warning
For security reasons, please change the default password immediately after your first login.
:::

## Next Steps

After successful installation:

1. **Change the default admin password**
2. Configure integrations with your monitoring tools
3. Set up notification channels (email, SMS, Slack, etc.)
4. Create teams and assign users
5. Configure on-call schedules
6. Set up alert routing rules

Refer to the [Configuration Guide](./configuration.md) for detailed setup instructions.

## Getting Help

If you encounter issues:

- Visit [GitHub Issues](https://github.com/skylogsio/skylogs/issues)
- Email: [support@skylogs.io](mailto:support@skylogs.io)
