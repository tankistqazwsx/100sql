import enum
import random
import datetime

from bunch import generateRandomBunch

tables = {
    'Canteen': {
        'id': int,
        'title': str,
        'workingHours': int,
        "description": str,
        "phoneNumber": int
    },
    'CanteenWorker': {
        'id': int,
        'fullName': str,
        'canteenId': int
    },
    'Courier': {
        'id': int,
        'title': str,
        'workingHours': int,
        "description": str,
        "phoneNumber": int
    },
    'Order': {
        'id': int,
        'orderNumber': int,
        'orderTime': int,
        "quantityDishes": int,
        "status": str,
        "amountPayable": int,
        "canteenWorkerId": int,
        "courierId": int,
        "clientId": int
    },
}

insertUpdateData = ["Александроус", "Андреев", "Леха", "Колян"]

    
def generateColumns(tableName : str) -> str:
    table_keys = list(tables[tableName].keys())
    bunch_of_keys = generateRandomBunch(table_keys)
    columns_str = ""
    for i in range(len(bunch_of_keys)):
        columns_str += '\'' + bunch_of_keys[i] + '\'' + ('' if i == len(bunch_of_keys)-1 else ',')
    return columns_str


def generateWhereStatements():
    whereArrays = []
    for table in tables.values():
        for column in table:
            if column != "*":
                columnType = table[column]
                if columnType == str:
                    whereElements = f"{random.choice(insertUpdateData)}"
                elif columnType == int:
                    whereElements = random.randint(0, 1000)
                elif columnType == float:
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
        operationsColumn = random.choice(list(tables[table].values()))
    
    where = generateWhereStatements()

    if command == sql.DELETE:
        return f"{stringCommand} from {table}{selectStatement} WHERE {where};"
    elif command == sql.INSERT:
        return f"{stringCommand} INTO {table} VALUES ({where});"
    elif command == sql.SELECT:
        columns = generateColumns(table)

        return f"{stringCommand} {columns} from {table}{selectStatement} WHERE {where};"
    elif command == sql.UPDATE:
        return f"{stringCommand} {table} SET {{ }};"


def updateTemplate():
    return abstractComand(sql.UPDATE)


def deleteTemplate():
    return abstractComand(sql.DELETE)


def insertTemplate():
    return abstractComand(sql.INSERT)


def selectTemplate():
    return abstractComand(sql.SELECT)


class sql(enum.Enum):
    SELECT = "SELECT",
    UPDATE = "UPDATE",
    DELETE = "DELETE",
    INSERT = "INSERT",
    ZATICHKA = ""


def generateCreatingTable(table_name):
    res = f"CREATE TABLE {table_name} ("
    table = tables[table_name]
    for column_name in table:
        column_type = str(table[column_name].__name__) # TODO нужны классы из sql
        # <col_name1> <col_type1>
        name_and_type = f"{column_name} {column_type}"
        res += name_and_type + ", "
    res += ");"
    return res

for table_name in tables:
    print(generateCreatingTable(table_name))


for i in range(50):
    funarray = [updateTemplate(), selectTemplate(),
            deleteTemplate(), insertTemplate()]
    print(random.choice(funarray))
