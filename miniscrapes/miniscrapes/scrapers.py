import requests


def weather(zip_code, state):
    return {}


def covid(zip_code, state):
    response = requests.get(
        f'https://api.covidtracking.com/v1/states/{state}/current.json')
    results = response.json()
    positive = results.get('positiveIncrease', 0) * 1.0
    total = results.get('totalTestResultsIncrease', 0) * 1.0
    results['dayPositiveRate'] = (
        positive / total if positive and total else 'n/a')
    return results
