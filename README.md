# Slack Integration for Django Applications

A lightweight Django-based integration that enables sending real-time notifications from Django applications directly to Slack channels using Incoming Webhooks.

This project is designed to help developers connect business events (like user actions, system alerts, or background jobs) to Slack in a simple and scalable way.

---

## Features

- Send real-time notifications from Django to Slack
- Support for multiple Slack webhook configurations
- Easy integration with Django views, signals, or background tasks
- Simple configuration using environment variables or admin settings
- Test endpoint for verifying Slack connectivity
- Lightweight and production-ready design

---

## How It Works

The integration uses Slack Incoming Webhooks to send HTTP POST requests from Django.

Flow:

1. Django event is triggered (e.g. user signup, order created)
2. Message is formatted in Django
3. HTTP request is sent to Slack webhook URL
4. Message appears in selected Slack channel

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Briankiboi/Slack-Integration-Django.git
cd Slack-Integration-Django
