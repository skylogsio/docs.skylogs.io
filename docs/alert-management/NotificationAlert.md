---
id: notification-alert
title: Notification Alert
sidebar_position: 4
slug: /alert-management/notification-alert
---

# Notification Alert

## Overview

The **Notification Alert** is a type of alert rule in Skylogs that delivers a message for a specific name and instance. You can use this type of alert to send a notification straight from your codebase. Each accepted call delivers the message to the rule's endpoints and finishes. Send again whenever you need another notification.

You'll need:

* An API token (issued when creating a Notification alert rule)
* Your alert rule set up in the dashboard
* Endpoint configurations (SMS, Email, Telegram, Teams, etc.)

---

## 🔧 Creating a Notification Alert Rule

To begin, create an **Alert Rule** with type **Notification** via the Skylogs web dashboard. Once created, you'll receive an **API token** which authorizes notification API usage.

Copy that token from the alert rule (admin access required) and send it as a bearer token on every notification call. `POST /api/v1/notification-alert` accepts the token of a rule whose type is `notification`.

Field details for creating the rule through the API are in [Alert rules → Notification alert rule](/api/alert-rules).

---

## 🔔 Sending a Notification

Send a notification by posting to the following endpoint:

```
POST https://mydomain.com/api/v1/notification-alert
```

### Headers

```
Authorization: Bearer <API_TOKEN>
Content-Type: application/json
```

`<API_TOKEN>` is the notification alert rule's token. A missing, unknown, or other-type token returns `401`.

### Body

```json
{
  "instance": "server-001",
  "description": "High CPU usage detected on primary database server."
}
```

* `instance` (required): Identifier for this notification.
* `description` (optional): Any additional context included in the notification.

> 📝 Calling again with the same `instance` updates the description and sends another notification. Omit `instance` and the request is rejected.

A successful call returns:

```json
{
  "status": true,
  "message": "Done"
}
```

### Example

```bash
curl -X POST https://mydomain.com/api/v1/notification-alert \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
        "instance": "server-001",
        "description": "High CPU usage detected on primary database server."
      }'
```

---

## 📡 Endpoints for Notifications

You can set up various **notification endpoints** to be triggered when a notification is sent. Supported types:

* 📩 Email
* 📞 Call
* 📬 SMS
* 📢 Telegram
* 👥 Microsoft Teams

These can be configured in the dashboard and attached to specific alerts.

---

## 👥 Shared Access & Customization

Skylogs encourages **collaboration**. You can:

* Add other **users** to an alert.
* Allow them to **attach their own endpoints** to receive notifications.
* Maintain **custom responsibility** over alert behavior per user.

> 🔐 Each user needs appropriate permissions to modify or observe alerts.

---

## 🧪 Example Use Case

Let’s say a deploy pipeline should tell the team when a release finishes:

1. Create a notification alert rule called `deploy-finished`.
2. Send a notification when the deploy completes, with an `instance` such as the release id.
3. Attach:

    * Your email and SMS endpoints
    * Your teammate adds a Telegram endpoint
4. Call the same endpoint again for the next release. Each call sends a new notification.

---

## ✉️ Custom notification text

Attach a template behavior rule to change the message sent to specific endpoints. Notification alerts use the same placeholders as API alerts. See [Custom Notification Templates](/alert-management/notification-templates#api-and-notification).

## 📘 Best Practices

* Use meaningful `instance` names so repeated calls for the same event stay recognizable.
* Treat the API token as a secret. It authorizes sending notifications for this rule.
* Share alerts responsibly using Skylogs’ user-level control.
* `description` is optional and is the text most templates show beside the instance.

---

Built with ❤️ by the Skylogs Team
