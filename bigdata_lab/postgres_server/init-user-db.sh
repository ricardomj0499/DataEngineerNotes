#!/usr/bin/env bash
set -e

# Create the user and the database
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER hive WITH PASSWORD 'hive';
	CREATE DATABASE metastore;
	GRANT ALL PRIVILEGES ON DATABASE metastore TO hive;
EOSQL

# Connect to the new database and set schema privileges
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "metastore" <<-EOSQL
	GRANT ALL ON SCHEMA public TO hive;
	ALTER SCHEMA public OWNER TO hive;
	ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO hive;
EOSQL
