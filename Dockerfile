# syntax=docker/dockerfile:1

# ---------- Stage 1: build the static site ----------
FROM node:20-alpine AS builder

WORKDIR /app

# Install dependencies first (cached layer — only invalidated when deps change)
COPY package.json package-lock.json* ./
# npm ci if a lockfile exists (reproducible), otherwise fall back to npm install
RUN if [ -f package-lock.json ]; then npm ci; else npm install; fi

# Copy the rest of the site and build
COPY . .
RUN npm run build
# Output: /app/build (static HTML/CSS/JS)

# ---------- Stage 2: serve with nginx ----------
FROM nginx:1.27-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -q --spider http://127.0.0.1/ || exit 1
