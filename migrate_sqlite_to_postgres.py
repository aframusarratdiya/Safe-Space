import os
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# --- CONFIGURATION ---
SQLITE_PATH = 'instance/safe_space.db'  # Path to your SQLite DB
POSTGRES_URL = 'postgresql://username:password@localhost:5432/safe_space'  # CHANGE THIS!

# --- SETUP ENGINES ---
sqlite_engine = create_engine(f'sqlite:///{SQLITE_PATH}')
postgres_engine = create_engine(POSTGRES_URL)

sqlite_meta = MetaData()
postgres_meta = MetaData()

sqlite_meta.reflect(bind=sqlite_engine)
postgres_meta.reflect(bind=postgres_engine)

SqliteSession = sessionmaker(bind=sqlite_engine)
PostgresSession = sessionmaker(bind=postgres_engine)
sqlite_session = SqliteSession()
postgres_session = PostgresSession()

# --- MIGRATION ---
def migrate_table(table_name):
    print(f'Migrating table: {table_name}')
    sqlite_table = Table(table_name, sqlite_meta, autoload_with=sqlite_engine)
    postgres_table = Table(table_name, postgres_meta, autoload_with=postgres_engine)
    rows = sqlite_session.execute(sqlite_table.select()).fetchall()
    for row in rows:
        data = dict(row)
        try:
            postgres_session.execute(postgres_table.insert().values(**data))
        except IntegrityError:
            print(f'IntegrityError on row: {data}')
            postgres_session.rollback()
        except Exception as e:
            print(f'Error: {e} on row: {data}')
            postgres_session.rollback()
    postgres_session.commit()
    print(f'Table {table_name} migrated.')

if __name__ == '__main__':
    for table_name in sqlite_meta.tables:
        if table_name in postgres_meta.tables:
            migrate_table(table_name)
        else:
            print(f'Table {table_name} not found in PostgreSQL schema. Skipping.')
    print('Migration complete!')
