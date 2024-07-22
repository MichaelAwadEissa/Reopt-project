import requests
import json

# Replace with your API key
API_KEY = 'cIMiU6Y47EsYM3q8UZ6VGKo7feFvudK65UgWmPMh'

# Define the URL for the REopt API
url = 'https://developer.nrel.gov/api/reopt/dev/jobs'

# Example data for the optimization job (replace with your own data)
payload = {
    "Scenario": {
        "webtool_uuid": "test",
        "Site": {
            "latitude": 39.7555,
            "longitude": -105.2211,
            "ElectricTariff": {
                "urdb_label": "5c8f9ef776fee04d89d3e116",
                "blended_annual_rates_us_dollars_per_kwh": 0.13,
                "blended_annual_demand_charges_us_dollars_per_kw": 20.0
            },
            "LoadProfile": {
                "doe_reference_name": "MidriseApartment",
                "annual_kwh": 400000,
                "monthly_totals_kwh": [
                    30000,
                    28000,
                    32000,
                    30000,
                    31000,
                    29000,
                    27000,
                    26000,
                    29000,
                    32000,
                    31000,
                    31000
                ]
            },
            "Financial": {
                "om_cost_escalation_pct": 0.025,
                "escalation_pct": 0.023,
                "offtaker_discount_pct": 0.07,
                "analysis_years": 20,
                "offtaker_tax_pct": 0.26
            },
            "Storage": {
                "min_kw": 0,
                "max_kw": 1000,
                "min_kwh": 0,
                "max_kwh": 4000
            },
            "PV": {
                "min_kw": 0,
                "max_kw": 1000,
                "installed_cost_us_dollars_per_kw": 1600
            }
        }
    }
}

headers = {
    'Content-Type': 'application/json',
    'x-api-key': API_KEY
}

# Print the URL and headers for debugging
print("URL:", url)
print("Headers:", headers)

# Print the payload for debugging
print("Payload:", json.dumps(payload, indent=2))

# Send the request to the REopt API
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 200:
    # Parse the response
    response_data = response.json()
    print(json.dumps(response_data, indent=2))
else:
    print(f'Error: {response.status_code}')
    print(response.text)
