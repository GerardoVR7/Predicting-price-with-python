from sqlalchemy import Column, Float, Table, ForeignKey, Date
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

stock_prices = Table(
    "stock_prices",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("date", Date),
    Column("open", Float),
    Column("high", Float),
    Column("low", Float),
    Column("close", Float),
    Column("adj_close", Float),
    Column("volume", Integer),
)

meta.create_all(engine)