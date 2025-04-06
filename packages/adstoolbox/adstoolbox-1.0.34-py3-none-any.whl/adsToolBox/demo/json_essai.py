from adsToolBox.global_config import set_timer
from adsToolBox.logger import Logger
from adsToolBox.loadEnv import env
from adsToolBox.dbMssql import dbMssql
import polars as pl
import uuid
import datetime
import random
import decimal

schema = 'data'
table = 'TestTypes'
batch_size = 10_000
set_timer(True)
logger = Logger(Logger.INFO, "AdsLogger")
env = env(logger, 'C:/Users/mvann/Desktop/ADS/Projects/adsGenericFunctions/adsToolBox/demo/.env')

connection = dbMssql({'database': env.HADDAD_DWH_SRC,
          'user': env.HADDAD_DWH_USER,
          'password': env.HADDAD_DWH_PWD,
          'host': env.HADDAD_DWH_HOST}, logger, batch_size)

connection.connect()
connection.sqlExec(f"DROP TABLE [{schema}].[{table}]")
connection.sqlExec(f"""
CREATE TABLE [{schema}].[{table}] (
    ID INT PRIMARY KEY, SmallIntColumn SMALLINT, BigIntColumn BIGINT,
    BitColumn BIT, DecimalColumn DECIMAL(10, 4), NumericColumn NUMERIC(10, 4),
    FloatColumn FLOAT, RealColumn REAL, MoneyColumn MONEY, 
    SmallMoneyColumn SMALLMONEY, CharColumn CHAR(10), 
    VarcharColumn VARCHAR(50), NCharColumn NCHAR(10), 
    NVarcharColumn NVARCHAR(50), TextColumn TEXT, NTextColumn NTEXT, 
    DateColumn DATE, TimeColumn TIME(3), DateTimeColumn DATETIME, 
    SmallDateTimeColumn SMALLDATETIME, DateTime2Column DATETIME2(3), 
    DateTimeOffsetColumn DATETIMEOFFSET(3), XmlColumn XML, 
    UniqueIdentifierColumn UNIQUEIDENTIFIER
);""")

cols = [
    "ID", "SmallIntColumn", "BigIntColumn", "BitColumn", "DecimalColumn",
    "NumericColumn", "FloatColumn", "RealColumn", "MoneyColumn",
    "SmallMoneyColumn", "CharColumn", "VarcharColumn", "NCharColumn",
    "NVarcharColumn", "TextColumn", "NTextColumn", "DateColumn", "TimeColumn",
    "DateTimeColumn", "SmallDateTimeColumn", "DateTime2Column",
    "DateTimeOffsetColumn", "XmlColumn",
    "UniqueIdentifierColumn"
]

n = 200_000

data = [
    {
        "ID": i + 1,
        "SmallIntColumn": random.randint(-32768, 32767),
        "BigIntColumn": random.randint(-9223372036854775808, 9223372036854775807),
        "BitColumn": random.randint(0, 1),
        "DecimalColumn": decimal.Decimal(f"{random.uniform(-9999.9999, 9999.9999):.4f}"),
        "NumericColumn": decimal.Decimal(f"{random.uniform(-9999.9999, 9999.9999):.4f}"),
        "FloatColumn": random.uniform(-1e6, 1e6),
        "RealColumn": random.uniform(-1e6, 1e6),
        "MoneyColumn": decimal.Decimal(f"{random.uniform(-1000000, 1000000):.2f}"),
        "SmallMoneyColumn": decimal.Decimal(f"{random.uniform(-10000, 10000):.2f}"),
        "CharColumn": random.choice(["ABC", "XYZ", "123", "HELLO", "WORLD"]).ljust(10),
        "VarcharColumn": random.choice(["Lorem", "Ipsum", "Dolor", "Sit", "Amet"]),
        "NCharColumn": random.choice(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).ljust(10),
        "NVarcharColumn": random.choice(["Polars", "Python", "SQL", "Data", "Test"]),
        "TextColumn": f"TextData {i}",
        "NTextColumn": f"NTextData {i}",
        "DateColumn": datetime.date.today() - datetime.timedelta(days=random.randint(0, 365)),
        "TimeColumn": datetime.time(random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)),
        "DateTimeColumn": datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365)),
        "SmallDateTimeColumn": datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365)),
        "DateTime2Column": datetime.datetime.now().isoformat(timespec='milliseconds'),
        "DateTimeOffsetColumn": datetime.datetime.now().isoformat(),
        "XmlColumn": f"<root><value>{random.randint(1, 100)}</value></root>",
        "UniqueIdentifierColumn": str(uuid.uuid4()),
    }
    for i in range(n)
]

df = pl.DataFrame(data)

rows = [list(d.values()) for d in data]

results = connection.insertBulk(schema, table, cols, rows)

print(results)
