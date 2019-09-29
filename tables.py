tables = {
    'Canteen': 
    [
        {
            'name': 'id',
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        {
            'name': 'title',
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        {
            'name': 'workingHours',
            'type': 'DATE',
            'info': {'notNull'}
        },
        {
            'name': 'title',
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        {
            'name': 'phoneNumber',
            'type': 'INTEGER',
            'len': '11'
        }
    ],
    'CanteenWorker': 
    [
        {
            'name': 'id',
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        {
            'name': 'fullName',
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        {
            'name': 'canteenId',
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': {'Canteen', 'Id'}
        },
    ],
    'Courier': 
    [
        {
            'name': 'id',
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        {
            'name': 'title',
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        {
            'name': 'description',
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        {
            'name': 'phoneNumber',
            'type': 'INTEGER',
            'len': '11',
        }
    ],
    'Order': 
    [
        {
            'name': 'id',
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        {
            'name': 'orderNumber',
            'type': 'INTEGER',
            'info': {'notNull'}
        },
        {
            'name': 'orderTime',
            'type': 'TIME',
            'info': {'notNull'}
        },
        {
            'name': 'quantityDishes',
            'type': 'INTEGER',
            'info': {'notNull'}
        },
        {
            'name': 'status',
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        {
            'name': 'amountPayable',
            'type': 'INTEGER',
            'info': {'notNull'}
        },
        {
            'name': 'canteenWorkerId',
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': {'Canteen', 'Id'}
        },
        {
            'name': 'courierId',
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': {'Courier', 'Id'}
        },
        {
            'name': 'clientId',
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': {'Client', 'Id'}
        },
    ]
}