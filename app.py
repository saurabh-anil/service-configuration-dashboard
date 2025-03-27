from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "http://qa-configs.internal.netomi.com/v1/service/configuration/get"
API_URL2 = "http://configmanager-dev1.internal.netomi.com/v1/service/configuration/get"
HEADERS = {"Content-Type": "application/json"}

@app.route('/', methods=['GET', 'POST'])
def index():
    service_name = "ds-gateway-app"  # Default service name
    data = {}

    if request.method == 'POST':
        service_name = request.form.get('service_name', service_name)  # Get user input

    payload = {
        "serviceName": service_name,
        "env": "qa",
        "region": "us-east-1"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.Timeout:
        return "Error: The API request timed out. Please try again later.", 500
    except requests.RequestException as e:
        return f"Error: Unable to fetch data from API. {e}", 500

    return render_template('index.html', data=data, service_name=service_name)

@app.route('/home', methods=['GET', 'POST'])
def home():
    service_name = "ds-gateway-app"  # Default service name
    data = {}

    if request.method == 'POST':
        service_name = request.form.get('service_name', service_name)  # Get user input

    payload = {
        "serviceName": service_name,
        "env": "dev1",
        "region": "us-east-1"
    }

    try:
        response = requests.post(API_URL2, json=payload, headers=HEADERS, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.Timeout:
        return "Error: The API request timed out. Please try again later.", 500
    except requests.RequestException as e:
        return f"Error: Unable to fetch data from API. {e}", 500

    return render_template('index.html', data=data, service_name=service_name)

if __name__ == '__main__':
    app.run(debug=True)