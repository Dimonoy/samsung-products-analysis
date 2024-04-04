FROM mysql:8.3.0

WORKDIR /src
COPY database-init.sql /src/.
EXPOSE 3306

RUN mysql -u root -p < database-init.sql
