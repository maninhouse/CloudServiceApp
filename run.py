from app import app

stores = [
    {
        'name': 'Cool Store',
        'items': [
                {'name': 'Cool Item', 'price': 10}
            ]
    }
]

if __name__ == '__main__':
    app.run()
