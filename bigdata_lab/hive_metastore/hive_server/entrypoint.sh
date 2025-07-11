#!/bin/bash
set -x
 
DB_TYPE="postgres"

echo "🔍 Verificando estado del Hive Metastore..."

# Esperar a que la base de datos esté lista (opcional, pero recomendable)
#echo "⌛ Esperando a que PostgreSQL esté disponible..."
#until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  #sleep 2
#done

# Verifica si el esquema ya está inicializado
OUTPUT=$(schematool -dbType "$DB_TYPE" -info 2>&1) || true

if echo "$OUTPUT" | grep -qi "Metastore schema version"; then
    echo "Hive Metastore ya está inicializado."
    echo "$OUTPUT" | grep "Metastore schema version"
elif echo "$OUTPUT" | grep -qi "Failed to get schema version"; then
    echo "Hive Metastore no está inicializado. Procediendo a inicializar..."
    schematool -initSchema -dbType "$DB_TYPE" 
else
    echo "Error inesperado al verificar el Hive Metastore:"
    echo "$OUTPUT"
    exit 1
fi

# Arrancar el servicio Metastore (asumiendo Hive 3+)
start-metastore

/bin/bash 