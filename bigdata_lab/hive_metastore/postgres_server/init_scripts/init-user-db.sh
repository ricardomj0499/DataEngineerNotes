#!/usr/bin/env bash
set -e

echo "[INFO] Creating Hive user and metastore database..."

# 1. Create hive user if not exists
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  DO
  \$\$
  BEGIN
    IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles WHERE rolname = 'hive'
    ) THEN
      CREATE ROLE hive LOGIN PASSWORD '${HIVE_DB_PASSWORD}';
    END IF;
  END
  \$\$;
EOSQL

# 2. Create metastore DB if not exists
if ! psql -U "$POSTGRES_USER" -tAc "SELECT 1 FROM pg_database WHERE datname = 'metastore'" | grep -q 1; then
  echo "[INFO] Creating 'metastore' database..."
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE metastore
      WITH ENCODING='UTF8'
      LC_COLLATE='C'
      LC_CTYPE='C'
      TEMPLATE=template0;
    GRANT ALL PRIVILEGES ON DATABASE metastore TO hive;
EOSQL
else
  echo "[INFO] Database 'metastore' already exists. Skipping creation."
fi

# 3. Always apply schema ownership and grants
# (safe even if schema exists and user already owns it)
echo "[INFO] Setting schema privileges..."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "metastore" <<-EOSQL
  GRANT ALL ON SCHEMA public TO hive;
  ALTER SCHEMA public OWNER TO hive;
  ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO hive;
EOSQL

echo "[INFO] Hive metastore initialization complete."