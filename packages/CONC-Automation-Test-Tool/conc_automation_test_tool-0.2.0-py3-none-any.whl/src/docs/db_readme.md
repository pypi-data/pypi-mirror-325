# Database Setup and Usage Guide

## Table of Contents
1. [Install PostgreSQL](#install-postgresql)
2. [Create Database and User](#create-database-and-user)
3. [Generate Schema from XLSX](#generate-schema-from-xlsx)
4. [Create Tables](#create-tables)
5. [Insert Dummy Data](#insert-dummy-data)
6. [Delete a Table](#delete-a-table)
7. [Update a Table](#update-a-table)
8. [Example Usage](#example-usage)

## Install PostgreSQL

### On macOS
1. **Install PostgreSQL using Homebrew**:
    ```sh
    brew install postgresql
    ```

2. **Start PostgreSQL service**:
    ```sh
    brew services start postgresql
    ```

3. **Verify installation**:
    ```sh
    psql --version
    ```

### On Ubuntu
1. **Update the package list**:
    ```sh
    sudo apt update
    ```

2. **Install PostgreSQL**:
    ```sh
    sudo apt install postgresql postgresql-contrib
    ```

3. **Start PostgreSQL service**:
    ```sh
    sudo systemctl start postgresql
    ```

4. **Enable PostgreSQL service to start on boot**:
    ```sh
    sudo systemctl enable postgresql
    ```

5. **Verify installation**:
    ```sh
    psql --version
    ```

## Create Database and User

1. **Access PostgreSQL**:
    ```sh
    sudo -i -u postgres
    psql
    ```

2. **Create a new database**:
    ```sql
    CREATE DATABASE mydatabase;
    ```

3. **Create a new user**:
    ```sql
    CREATE USER myuser WITH PASSWORD 'mypassword';
    ```

4. **Grant privileges to the user**:
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
    ```

5. **Exit PostgreSQL**:
    ```sql
    \q
    exit
    ```

## Generate Schema from XLSX

1. **Ensure your XLSX file is in the correct location**:
    Place your XLSX file in the desired directory, for example: `/path/to/your/xlsxfile.xlsx`.

2. **Run the schema generation script**:
    ```sh
    python -m src.my_project.db.generate_schema /path/to/your/xlsxfile.xlsx /path/to/your/schema.py
    ```

3. **Verify the generated `schema.py` file**:
    The `schema.py` file should be generated at the specified location, for example: `/path/to/your/schema.py`.

## Create Tables

1. **Run the table creation script**:
    ```sh
    python -m src.my_project.db.create_tables
    ```

2. **Verify the tables in the database**:
    ```sh
    psql -U myuser -d mydatabase
    \dt
    ```

## Insert Dummy Data

1. **Run the data insertion script**:
    ```sh
    python -m src.my_project.db.insert_data
    ```

2. **Verify the inserted data**:
    ```sh
    psql -U myuser -d mydatabase
    SELECT * FROM test1_conc;
    ```

## Delete a Table

1. **Run the table deletion script**:
    ```sh
    python -m src.my_project.db.delete_table <table_name>
    ```

    Example:
    ```sh
    python -m src.my_project.db.delete_table test1_conc
    ```

2. **Verify the table deletion**:
    ```sh
    psql -U myuser -d mydatabase
    \dt
    ```

## Update a Table

1. **Run the table update script**:
    ```sh
    python -m src.my_project.db.update_table <table_name> <update_data> <condition>
    ```

    Example:
    ```sh
    python -m src.my_project.db.update_table test1_conc "{'fname': 'UpdatedName'}" "table.c.id == 1"
    ```

2. **Verify the updated data**:
    ```sh
    psql -U myuser -d mydatabase
    SELECT * FROM test1_conc WHERE id = 1;
    ```

## Example Usage

### Generate Schema from XLSX
```sh
python -m src.my_project.db.generate_schema /path/to/your/xlsxfile.xlsx /path/to/your/schema.py