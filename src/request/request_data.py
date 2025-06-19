import requests


BASE_URL = 'https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj'


def get_url(year: int, month: int, chunk: int = 0) -> str:
    return f'{BASE_URL}/{year}-{month:02}/Estabelecimentos{chunk}.zip'


def request(url: str) -> bytes:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except Exception as e:
        print(e)
