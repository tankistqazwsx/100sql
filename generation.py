import random

from bunch import generateRandomBunch

from tables import tables

insertUpdateData = ["Александроус", "Андреев", "Леха", "Колян"]


def generateColumns(tableName: str) -> list:
    table_keys = list(tables[tableName].keys())
    bunch_of_keys: list = generateRandomBunch(table_keys)
    return bunch_of_keys


def singleQuote(word: str):
    return f"'{word}'"


def randomBoolean() -> bool:
    return bool(random.getrandbits(1))


def toStr(listok: list):
    columns_str = ""
    for field in listok:
        columns_str += field
        if field != listok[-1]:
            columns_str += ', '
    return columns_str


def generateWhereStatements(table):
    whereArrays = []
    columns = generateColumns(table)
    for column in columns:
        columnType = tables[table][column]['type']
        if columnType == "VARCHAR":
            whereElements = f"{random.choice(insertUpdateData)}"
            whereElements = singleQuote(whereElements)
        elif columnType == "INTEGER":
            whereElements = random.randint(0, 1000)
        elif columnType == "FLOAT":
            whereElements = random.random()
        else:
            whereElements = None
        whereArrays.append(f"{column}={whereElements}")
    return toStr(whereArrays)


def generateCreatingTable(table_name):
    res = "CREATE TABLE "
    if randomBoolean():
        res += "IF NOT EXISTS "
    res += f"{table_name} ("
    table = tables[table_name]
    for column_name in table:
        column_type = table[column_name]["type"]
        try:
            column_type += "(" + table[column_name]["len"] + ")"
        except KeyError as identifier:
            pass
        # <col_name1> <col_type1>
        name_and_type = f"{column_name} {column_type}"
        res += name_and_type + ", "
    res += ");"
    return res


def generateDropTable(table_name):
    res = "DROP TABLE "
    if randomBoolean():
        res += "IF EXISTS "
    res += f"{table_name};"
    return res


def generateDatabase(database_name):
    return f"CREATE DATABASE {database_name}"


def updateTemplate(table, where):
    return f"UPDATE {table} SET {{{where}}};"


def deleteTemplate(table, where):
    return f"DELETE FROM {table} WHERE {where};"


def insertTemplate(table, where):
    return f"INSERT INTO {table} VALUES ({where});"


def selectTemplate(table, where):
    columns = toStr(generateColumns(table))
    return f"SELECT {columns} FROM {table} WHERE {where};"


def generate_sql_requests():
    for table_name in tables:
        yield generateCreatingTable(table_name)

    for table_name in tables:
        yield generateDropTable(table_name)

    for i in range(10):
        table = random.choice(list(tables.keys()))
        where = generateWhereStatements(table)
        yield selectTemplate(table, where)


