# User Management Application

This project provides a basic user management platform using **FastAPI** for the backend, **Vue 3** for the frontend and **MySQL** for data storage. All components are orchestrated with **Docker Compose**.

## Docker composition

The `docker-compose.yml` file defines four services:

- **mysql**: MySQL database that stores user data.
- **adminer**: a lightweight database administration tool.
- **backend**: FastAPI server exposing the API.
- **frontend**: Vue 3 application serving the user interface.

Start every service with:

```bash
docker compose up --build
```

The exposed ports are:

- Backend: [http://localhost:5001](http://localhost:5001)
- Frontend: [http://localhost:5173](http://localhost:5173)
- Adminer: [http://localhost:8080](http://localhost:8080)

## Starting the backend

The backend lives in the `backend/` directory. It needs connection details to MySQL which are provided via environment variables. By default Docker Compose sets:

- `DB_HOST=mysql`
- `DB_USER=root`
- `DB_PASSWORD=root`
- `DB_NAME=appdb`
- `DB_PORT=3306`

To run the server outside Docker, install the requirements and start Uvicorn:

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```

Ensure a MySQL instance is accessible with the same credentials.

## Starting the frontend

The frontend is located in the `frontend/` directory. Launch it with Node:

```bash
cd frontend
npm install
npm run dev
```

The development server runs on [http://localhost:5173](http://localhost:5173).

### Frontend environment variables

Create a `.env` file inside `frontend/` and provide the API endpoint base URL:

```bash
VITE_API_BASE_URL=http://localhost:5001/api
```

For production deployments replace the value with your hosted backend, for
example:

```bash
VITE_API_BASE_URL=https://user-management-1d430k7vg-yanldxs-projects.vercel.app/api
```

## Accessing Adminer

Adminer allows you to browse the database easily. After the Docker stack starts, open [http://localhost:8080](http://localhost:8080) and log in using the MySQL credentials.

### Database admin environment variables

The MySQL service uses the following variables for the administrator account:

```yaml
MYSQL_ROOT_PASSWORD: root
MYSQL_DATABASE: appdb
```

Use these credentials when signing into Adminer (System: `MySQL`, Server: `mysql`, Username: `root`, Password: `root`, Database: `appdb`). Adjust the values in `docker-compose.yml` if you need different credentials before launching the containers.

## Hosted MySQL setup

You can deploy the application with a hosted MySQL instance (for example
with [Aiven](https://aiven.io/) or [AlwaysData](https://www.alwaysdata.com/)).
Set the following environment variables before starting Docker Compose:

```
DB_HOST=<remote host>
DB_PORT=<remote port>
DB_USER=<remote user>
DB_PASSWORD=<remote password>
DB_NAME=<database name>
INIT_ADMIN=First,Last,email@example.com,password
```

`INIT_ADMIN` should contain the initial administrator credentials separated by
commas. During application startup the backend will automatically create this
user if it does not already exist.
