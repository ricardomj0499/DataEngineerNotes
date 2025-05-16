FROM postgres:17.5

COPY init_scripts/init-user-db.sh /docker-entrypoint-initdb.d/

RUN chmod 755 /docker-entrypoint-initdb.d/init-user-db.sh

EXPOSE 5432
