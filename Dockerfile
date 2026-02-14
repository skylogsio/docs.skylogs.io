# Build stage
FROM node:lts-alpine AS build

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm ci --only=production=false || npm install

# Copy project files
COPY . .

# Build the project
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy custom nginx config (optional)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy built files from build stage
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
