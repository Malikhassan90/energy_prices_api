from flask import render_template, jsonify, request, abort, Blueprint
from app import db
from app.models import OilPrice, GasPrice

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.htm')

@bp.route('/api/oil-prices', methods=['GET'])
def get_oil_prices():
    try:
        oil_prices = OilPrice.query.all()
        return jsonify([
        price.serialize() for price in oil_prices])
    except Exception as e:
        bp.logger.error(f"Error fetching oil prices: {str(e)}")
        abort(500)

@bp.route('/api/gas-prices', methods=['GET'])
def get_gas_prices():
    try:
        gas_prices = GasPrice.query.all()
        return jsonify([price.serialize() for price in gas_prices])
    except Exception as e:
        bp.logger.error(f"Error fetching gas prices: {str(e)}")
        abort(500)

@bp.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@bp.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
