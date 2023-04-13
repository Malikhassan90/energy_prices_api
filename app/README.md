# README
To run the code, first set up the environment and install the required packages. Then, run the run.py script.

Create and activate a virtual environment (optional, but recommended):
# For Windows:

python -m venv venv
venv\Scripts\activate
# For macOS/Linux:

python3 -m venv venv
source venv/bin/activate

Install the required packages using the requirements.txt file:

pip install -r requirements.txt

Set the environment variables (you may also want to set the FLASK_ENV variable to development for development purposes):
# For Windows:

set FLASK_APP=run.py
set FLASK_ENV=development

# For macOS/Linux:

export FLASK_APP=run.py
export FLASK_ENV=development

Initialize the database by running the following commands:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Run
Run the Flask application:

flask run

This will start the Flask server. You can access the application by visiting http://127.0.0.1:5000/ in your browser. To access the API endpoints, visit http://127.0.0.1:5000/api/oil-prices and http://127.0.0.1:5000/api/gas-prices.

# Github link:
https://github.com/Malikhassan90/energy_prices_api.git
