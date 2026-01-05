---
sidebar_position: 1
title: Overview
description: Introduction to Skylogs - An all-in-one alert and incident management platform.
---

# Overview

Welcome to **Skylogs** - an open-source, end-to-end alert and incident management platform designed to bridge the gap between observability tools and incident response.

## What is Skylogs?

Skylogs is a unified platform that consolidates alerts from multiple observability systems, applies intelligent routing and escalation, and ensures the right people are notified through their preferred communication channels.

Built with **shared responsibility** and **personalization** at its core, Skylogs is flexible enough to serve all teams within your organization - from DevOps and SRE to Security and Development teams.

## Our Mission

> **Incident response is not only an infrastructure concern — it's an organizational responsibility.**

Skylogs empowers every team with the tools they need to respond quickly and effectively to incidents, ensuring seamless collaboration across your entire organization.

## Key Capabilities

### 🔗 Universal Integration

Skylogs works seamlessly with popular monitoring tools including Prometheus, Grafana, New Relic, Datadog, Zabbix, and more. Its technology-agnostic design allows you to integrate with any observability solution through REST API and webhook support.

### 📊 Intelligent Alert Management

- Collect alerts from multiple observability systems in one place
- Smart correlation and deduplication to reduce alert noise
- Flexible routing based on severity, source, and custom tags
- Alert suppression and maintenance windows

### 🚨 Incident Management

- Transform alerts into actionable incidents
- Incident analysis to reduce troubleshooting time
- AI-generated incident reports and postmortems
- Track key metrics: MTTR, MTTA, and SLA compliance

### 👥 On-Call Management

- Customizable on-call rotations and schedules
- Automated escalations with configurable timeouts
- Easy handoff management and shift swapping

### 📱 Multi-Channel Notifications

- SMS, phone calls, email, Slack, Microsoft Teams, Telegram, and more
- Rich email formatting with detailed context
- Endpoint verification to ensure critical alerts are delivered

### 📈 Status Pages

- Public or private branded status pages
- Real-time incident updates
- Historical uptime reporting
- Subscriber notifications

### 🛠 Advanced Features

- Full incident lifecycle tracking
- Alert analytics and trend reporting
- Custom dashboards and widgets
- Role-Based Access Control (RBAC)
- SLA reports for each service
- Service issue reports

## Who Should Use Skylogs?

### Network & Datacenter Teams

Strong integration with Zabbix and similar tools, with endpoint assurance for reliable critical alert delivery.

### DevOps Engineers

Centralize alerts from multiple monitoring platforms, reduce alert fatigue, and simplify on-call scheduling.

### Site Reliability Engineers (SREs)

Improve MTTD and MTTR, enforce reliable alerting strategies, and track SLOs with detailed analytics.

### Development Teams

Get real-time notifications on application issues with team-specific alert preferences and workflow integrations.

### Security Teams

Integrate with Splunk, ELK stack, and SIEMs to manage security alerts and coordinate SOC response efforts.

### Engineering Managers

Gain visibility into team workload, track incident response metrics, and generate executive-ready reports.

## Why Choose Skylogs?

### Open Source & Community-Driven

Skylogs is built by the community, for the community. Contribute, customize, and extend it to fit your needs.

### Technology-Agnostic

No vendor lock-in. Integrate with any monitoring tool or observability platform you already use.

### Built for Scale

From small teams to enterprise organizations, Skylogs scales with your infrastructure and team size.

### Smart & Efficient

Intelligent alert correlation and routing reduces noise and ensures the right people get notified at the right time.

### Enterprise-Ready

RBAC, audit logs, and compliance features make Skylogs suitable for organizations of any size.

## Architecture Overview

Skylogs is built using modern technologies:

- **Backend**: Laravel (PHP 8.1+)
- **Frontend**: TypeScript-based modern UI
- **Database**: MySQL 8.0+ / PostgreSQL 13+
- **Cache & Queues**: Redis 6.0+
- **Deployment**: Docker & Docker Compose support

The platform is designed to be cloud-native and can be deployed on-premises or in any cloud environment.

## Getting Started

Ready to try Skylogs? Here's what you need to do:

1. **[Install Skylogs](./installation.md)** - Get up and running in minutes with Docker
2. **[Configure Your First Integration](../integrations/overview.md)** - Connect your monitoring tools
3. **[Set Up Notifications](../guides/notifications.md)** - Configure alert channels
4. **[Create On-Call Schedules](../guides/on-call.md)** - Define who gets notified and when

## Community & Support

Join our growing community:

- **GitHub**: [github.com/skylogsio/skylogs](https://github.com/skylogsio/skylogs)
- **Issues**: Report bugs or request features on [GitHub Issues](https://github.com/skylogsio/skylogs/issues)
- **Discussions**: Join conversations on [GitHub Discussions](https://github.com/skylogsio/skylogs/discussions)
- **Email**: Reach out at [support@skylogs.io](mailto:support@skylogs.io)

## License

Skylogs is open-source software licensed under the [MIT License](https://github.com/skylogsio/skylogs/blob/main/LICENSE).

---

Ready to get started? Head over to the [Installation Guide](./installation.md) to set up Skylogs in your environment.
