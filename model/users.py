from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

users = Table("users", meta_data,
                Column("user_id", Integer, primary_key=True),
                Column("user_name", String(10), nullable=False),
                Column("user_email", String(100), nullable=False),
                Column("user_password", String(120), nullable=False),
                Column("user_apiKey", String(44), nullable=False),
                Column("user_clientId", String(36), nullable=False),
                Column("user_status", String(10), nullable=False),
                Column("user_role", String(10), nullable=False))

meta_data.create_all(engine)