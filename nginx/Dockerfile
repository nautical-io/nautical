# Use the official nginx base image
FROM nginx:1.24

# Remove the default nginx configuration
RUN rm /etc/nginx/nginx.conf

# Copy the custom nginx configuration file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for incoming HTTP traffic
EXPOSE 80

# Start nginx in the foreground when the container is run
CMD ["nginx", "-g", "daemon off;"]
