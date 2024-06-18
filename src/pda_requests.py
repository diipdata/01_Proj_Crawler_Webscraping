import requests

class PaoDeAcucarScraper:

    def __init__(self):
        self.origin = "https://www.paodeacucar.com"
        self.products = []
        self.api_key = 'paodeacucar'
        self.page = 1
        self.results_per_page = 12
        self.keyword = ''
        self.http = 

        def start(self, keyword):
            self.keyword = keyword
            self.search_products

    def __configure_session(self):
        retry_strategy = Retry(
            total=3,
            status_forcelist=[403, 429, 500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        return session


    def search_products(self, keyword):
        url = f'https://www.paodeacucar.com/busca?terms=yogurte'

    headers = {

    }

    try:
        content = self.http.get(url, headers=headers)
        if content.status_code == 200:
            return content.json()
        else
            raise(content.status_code)

    except:
        raise(content.status_code)

    def get_product_data(self):
        if self.content:
            product = self.content["products"]
            return products

keyword = 'sabonete'
scraper = PaoDeAcucarScraper()
data = scraper.start(keyword)
print(content.json())