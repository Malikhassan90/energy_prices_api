import requests
from datetime import datetime
from .models import OilPrice, GasPrice, db

def fetch_data_from_url(url, columns):
    response = requests.get(url)
    data_package = response.json()
    resources = data_package['resources']
    for resource in resources:
        if resource['format'] == 'csv':
            csv_url = resource['path']
            csv_data = requests.get(csv_url).text
            csv_lines = csv_data.split('\n')[1:]  # Skip header
            for line in csv_lines:
                if line:
                    row = line.split(',')
                    try:
                        date = datetime.strptime(row[columns.index('Date')], '%Y-%m-%d').date()
                    except ValueError:
                        try:
                            date = datetime.strptime(row[columns.index('Date')], '%Y-%m').date()
                        except ValueError:
                            continue
                    price_string = row[columns.index('Price')].strip()
                    if price_string:
                        price = float(price_string)
                    else:
                        continue
                    yield date, price

def store_data_in_db(data, model):
    for date, price in data:
        db.session.add(model(date=date, price=price))
    db.session.commit()

def populate_data():
    # Check if there's already data in the database
    if OilPrice.query.first() is not None or GasPrice.query.first() is not None:
        print("Skipping Downloading Datasets again, the Database is already populated...")
        return
    
    print("Downloading Datasets and populating the database...")

    dataset_links = [
        ('https://datahub.io/core/oil-prices/datapackage.json', ['Date', 'Price']),
        ('https://datahub.io/core/natural-gas/datapackage.json', ['Date', 'Price'])
    ]

    for url, columns in dataset_links:
        data = fetch_data_from_url(url, columns)

        if 'Price' in columns:
            model = GasPrice if 'natural-gas' in url else OilPrice
            store_data_in_db(data, model)
