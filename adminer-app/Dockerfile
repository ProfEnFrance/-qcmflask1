FROM php:8.2-apache
COPY index.php /var/www/html/
RUN docker-php-ext-install pdo pdo_pgsql
EXPOSE 80