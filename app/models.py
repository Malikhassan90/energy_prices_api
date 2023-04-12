from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class OilPrice(db.Model):
    __tablename__ = 'oil_prices'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, index=True)  # Removed the unique constraint
    price = db.Column(db.Float, nullable=False)

    # drop unique constraint on date column
    __table_args__ = (
        db.Index('ix_oil_price_date', 'date'),
    )

    def __repr__(self):
        return f'<OilPrice {self.date}: {self.price}>'

class GasPrice(db.Model):
    __tablename__ = 'gas_prices'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, index=True)  # Removed the unique constraint
    price = db.Column(db.Float, nullable=False)

    # drop unique constraint on date column
    __table_args__ = (
        db.Index('ix_gas_price_date', 'date'),
    )

    def __repr__(self):
        return f'<GasPrice {self.date}: {self.price}>'


def serialize(self):
    return {
        'id': self.id,
        'date': self.date.isoformat(),
        'price': self.price
    }

OilPrice.serialize = serialize
GasPrice.serialize = serialize
