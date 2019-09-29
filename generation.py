import enum
import random

from bunch import generateRandomBunch

from tables import tables

insertUpdateData = ["Александроус", "Андреев", "Леха", "Колян"]


def generateColumns(tableName: str) -> str:
    table_keys = list(tables[tableName].keys())
    bunch_of_keys = generateRandomBunch(table_keys)
    columns_str = ""
    for i in range(len(bunch_of_keys)):
        columns_str += singleQuote(bunch_of_keys[i])
        if i != len(bunch_of_keys) - 1:
            columns_str += ','

    return columns_str


def singleQuote(word):
    return f"'{word}'"


def generateWhereStatements():
    whereArrays = []
    for table in tables.values():
        for column in table:
            if column != "*":
                columnType = table[column]["type"]
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
    return random.choice(whereArrays)


def abstractComand(command, table='', selectStatement='') -> str:
    stringCommand = random.choice(command.value)

    if not table:
        table = random.choice(list(tables.keys()))
        # пока допустим что только один оператор

    where = generateWhereStatements()

    if command == sql.DELETE:
        return f"{stringCommand} from {table}{selectStatement} WHERE {where};"
    elif command == sql.INSERT:
        return f"{stringCommand} INTO {table} VALUES ({where});"
    elif command == sql.UPDATE:
        return f"{stringCommand} {table} SET {{ }};"


def updateTemplate():
    return abstractComand(sql.UPDATE)


def deleteTemplate():
    return abstractComand(sql.DELETE)


def insertTemplate():
    return abstractComand(sql.INSERT)


class sql(enum.Enum):
    SELECT = "SELECT",
    UPDATE = "UPDATE",
    DELETE = "DELETE",
    INSERT = "INSERT",


def generateCreatingTable(table_name):
    res = f"CREATE TABLE IF NOT EXISTS {table_name} ("
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


def generateSelect(table_name):
    selectStatement = ''
    columns = generateColumns(table_name)
    where = generateWhereStatements()
    return f"SELECT {columns} from {table_name}{selectStatement} WHERE {where};"


def generate_sql_requests():
    for table_name in tables:
        yield generateCreatingTable(table_name)

    for i in range(50):
        funarray = [updateTemplate(), generateSelect(random.choice(list(tables.keys()))),
                    deleteTemplate(), insertTemplate()]
        yield random.choice(funarray)
