# Stage 1: Build frontend
FROM python:3.11-slim as builder
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN reflex export --frontend-only --no-zip

# Stage 2: Serve with nginx
FROM nginx:alpine
COPY --from=builder /app/.web/_static /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
