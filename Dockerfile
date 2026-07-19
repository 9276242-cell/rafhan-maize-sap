FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY sap.html /usr/share/nginx/html/sap.html
EXPOSE 8080
CMD ["sh", "-c", "sed -i 's/listen  *80;/listen '$PORT';/g' /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
