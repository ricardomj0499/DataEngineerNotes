---
# 🐘 PostgreSQL Metastore for Hive (Docker)

This project sets up a **PostgreSQL container** pre-configured to serve as the **Hive Metastore** backend, commonly used in data lake architectures with tools like Hive, Spark, or Presto.

> ⚠️ **Note:** This setup is for **learning and local development only**. Credentials and security should be improved before using in any production-like environment.
---

## 📦 Features

- Based on official [`postgres:17.5`](https://hub.docker.com/_/postgres) image.
- Initializes:

  - A `metastore` database.
  - A `hive` user with full privileges on the metastore.

- Easy to integrate into containerized Big Data environments.

---

## 🛠️ Setup Instructions

### 1. Create a Docker Volume (to persist data)

```bash
docker volume create pgdata_volume
```

### 2. Create a Docker Network (for communication with Hive or other services)

```bash
docker network create hive-net
```

### 3. Build the Image

Make sure you're in the root of this project (where the `Dockerfile` and `init_scripts/` folder are located):

```bash
docker build -t postgres:metastore ./postgres_server/
```

### 4. Run the Container

```bash
docker run -d \
  -p 5432:5432 \
  --network hive-net \
  --volume pgdata_volume:/var/lib/postgresql/data \
  --name postgres_hms \
  -e POSTGRES_PASSWORD=postgres \
  postgres:metastore
```

---

## 📁 File Structure

```
.
├── postgres_server/
│   ├── Dockerfile
│   └── init_scripts/
│       └── init-user-db.sh
```

- `init-user-db.sh`: Shell script automatically executed on container initialization to create the `hive` user and `metastore` database with the correct permissions.

---

## 🔒 Security Notes

This is a basic setup meant for development only:

- The `POSTGRES_PASSWORD` is hardcoded as `postgres`.
- The `hive` user password is also hardcoded as `hive`.
- Consider using Docker secrets, environment files, or Vault in real deployments.

---

## 🧪 Testing Connection (optional)

You can connect to the PostgreSQL instance using any client, for example:

```bash
psql -h localhost -U hive -d metastore
# Password: hive
```

Or from another container on the `hive-net` network.

---

## 📚 References

- Official PostgreSQL Docker Image: [https://hub.docker.com/\_/postgres](https://hub.docker.com/_/postgres)
- Hive Metastore Configuration: [Apache Hive Documentation](https://hive.apache.org/docs/latest/adminmanual-metastore-3-0-administration_75978150/)

---
