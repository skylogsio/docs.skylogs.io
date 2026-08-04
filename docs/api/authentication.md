---
id: authentication
title: Authentication
sidebar_position: 2
slug: /api/authentication
---

# Authentication

The Skylogs API uses **JWT bearer tokens** for all management endpoints. (Inbound alert webhooks use per-alert-rule tokens instead — see [Alert ingestion](/api/ingestion).)

## Login

```
POST /api/v1/auth/login
```

```json
{ "username": "your-username", "password": "your-password" }
```

**Response `200`:**

```json
{
  "accessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJI...",
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5...",
  "tokenType": "bearer",
  "roles": ["admin", "user"],
  "expiresIn": 3600,
  "refreshExpiresIn": 10800
}
```

Send the access token on every subsequent request:

```
Authorization: Bearer <accessToken>
```

Access tokens expire after **1 hour** (`expiresIn: 3600`); refresh tokens after **3 hours** (`refreshExpiresIn: 10800`). Invalid credentials return `401`.

## Refreshing

```
POST /api/v1/auth/refresh
Authorization: Bearer <refreshToken or accessToken>
```

Returns a fresh token pair with the same shape as login. Call it before `expiresIn` elapses; an expired/invalid token returns `401`, after which you must log in again. {/* TODO: confirm whether refresh expects the refreshToken or the accessToken in the Authorization header */}

## Current user, password, logout

```
POST /api/v1/auth/me      # get authenticated user info
POST /api/v1/auth/pass    # change the authenticated user's password
POST /api/v1/auth/logout  # invalidate the token
```

## Roles

The token response includes the user's `roles` (e.g. `admin`, `user`, `owner`), which determine access to management endpoints. {/* TODO: document the full role list and what each grants */}

## Automation advice

For scripts and CI, create a dedicated service user with the minimum role needed, log in at the start of the job, and treat the token pair as short-lived — re-login is cheap. Never embed a human user's credentials in automation.

:::caution
The interactive Swagger examples show `admin` / `123456` — make sure your production instance does not retain default credentials, and consider removing real-looking example credentials from the public spec.
:::
