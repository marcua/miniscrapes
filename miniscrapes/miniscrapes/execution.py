from miniscrapes.scrapers import covid
from miniscrapes.scrapers import weather


SCRAPERS = {
    'covid': covid,
    'weather': weather
}


def run_scrapers(recipient, zip_code, state):
    results = {}
    for slug, scraper in SCRAPERS.items():
        results[slug] = scraper(zip_code, state)

    print(results)
