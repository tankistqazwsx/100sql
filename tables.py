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