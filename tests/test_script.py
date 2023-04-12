import json
from datetime import date
from app.models import OilPrice, GasPrice

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_get_oil_prices(client, _db):
    oil_price = OilPrice(date=date(2023, 1, 1), price=70.0)
    _db.session.add(oil_price)
    _db.session.commit()

    response = client.get('/api/oil-prices')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['date'] == '2023-01-01'
    assert data[0]['price'] == 70.0

def test_get_gas_prices(client, _db):
    gas_price = GasPrice(date=date(2023, 1, 1), price=3.0)
    _db.session.add(gas_price)
    _db.session.commit()

    response = client.get('/api/gas-prices')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['date'] == '2023-01-01'
    assert data[0]['price'] == 3.0

def test_oil_prices_date_range(client, _db):
    oil_price1 = OilPrice(date=date(2023, 1, 1), price=70.0)
    oil_price2 = OilPrice(date=date(2023, 1, 15), price=75.0)
    _db.session.add_all([oil_price1, oil_price2])
    _db.session.commit()

    response = client.get('/api/oil-prices?start_date=2023-01-01&end_date=2023-01-15')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert data[0]['date'] == '2023-01-01'
    assert data[0]['price'] == 70.0
    assert data[1]['date'] == '2023-01-15'
    assert data[1]['price'] == 75.0

def test_gas_prices_date_range(client, _db):
    gas_price1 = GasPrice(date=date(2023, 1, 1), price=3.0)
    gas_price2 = GasPrice(date=date(2023, 1, 15), price=3.5)
    _db.session.add_all([gas_price1, gas_price2])
    _db.session.commit()

    response = client.get('/api/gas-prices?start_date=2023-01-01&end_date=2023-01-15')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert data[0]['date'] == '2023-01-01'
    assert data[0]['price'] == 3.0
    assert data[1]['date'] == '2023-01-15'
    assert data[1]['price'] == 3.5