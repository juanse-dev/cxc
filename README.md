# ETL de Gestión de Empleados

## Requisitos

- Python 3.11
- PostgreSQL
- Virtualenv

## Instalación

1. Clona este repositorio
2. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` en el directorio raíz del proyecto y añade las siguientes variables de entorno:

   ```dotenv
   DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_bd
   SCHEMA=test
   ```

## Uso

### Migraciones de Base de Datos

Para crear las tablas necesarias corre las migraciones usando:

```bash
alembic upgrade head
```

### Carga de Datos

1. Asegúrate de tener los archivos CSV (`employees.csv` y `catalogos.csv`) en el directorio `src/data`.
2. Ejecuta el script de carga de catálogos:

   ```bash
   python src/catalog_loader.py
   ```

3. Ejecuta el script de carga de empleados:

   ```bash
   python src/load_employees.py
   ```
