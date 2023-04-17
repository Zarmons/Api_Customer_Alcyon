from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

customers = Table("customers", meta_data,
                Column("id", Integer, primary_key=True),
                Column("name", String(255), nullable=False),
                Column("email", String(255), nullable=False),
                Column("password", String(120), nullable=False),
                Column("apiKey", String(44), nullable=False),
                Column("clientId", String(36), nullable=False),
                Column("status", String(10), nullable=False))

meta_data.create_all(engine)