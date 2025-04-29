# Stage 1: Build frontend
FROM python:3.11-slim as builder

WORKDIR /app

# Install system dependencies for Reflex build
RUN apt-get update && apt-get install -y unzip curl

# Copy source code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Generate the static frontend assets 
# RUN reflex export --frontend-only --no-zip

RUN reflex export --frontend-only --no-zip && \
    echo "Exported files:" && \
    find /app/.web/_static


# Stage 2: Serve static files with nginx
FROM nginx:alpine

COPY --from=builder /app/.web/_static /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
