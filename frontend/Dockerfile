# Use Nginx to serve the static files
FROM nginx:alpine

# Copy static files to Nginx's default directory
COPY index.html /usr/share/nginx/html
COPY styles.css /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d/default.conf


EXPOSE 80
