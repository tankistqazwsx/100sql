tables = {
    'Canteen': 
    {
        'id': {
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'title': {
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'workingHours': {
            'type': 'DATE',
            'info': {'notNull'}
        },
        'description':{
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'phoneNumber':{
            'type': 'INTEGER',
            'len': '11'
        }
    },
    'CanteenWorker': 
    {
        'id':{
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'fullName':{
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'canteenId':{
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': 'Canteen'
        },
    },
    'Courier': 
    {
        'id':{
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'title':{
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'description':{
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'phoneNumber':{
            'type': 'INTEGER',
            'len': '11',
        }
    },
    'Order': 
    {
        'id':{
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'orderNumber':{
            'type': 'INTEGER',
            'info': {'notNull'}
        },
        'orderTime':{
            'type': 'TIME',
            'info': {'notNull'}
        },
        'quantityDishes':{
            'type': 'INTEGER',
            'info': {'notNull'}
        },
        'status':{
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'amountPayable':{
            'type': 'INTEGER',
            'info': {'notNull'}
        },
        'canteenWorkerId':{
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': 'Canteen'
        },
        'courierId':{
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': 'Courier'
        },
        'clientId':{
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': 'Client'
        },
    }
}