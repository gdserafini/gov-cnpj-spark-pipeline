from src.utils.args_parser import get_args
from src.request.request_data import request, get_url
from src.utils.unzip import unzip_to_csv


def main() -> None:
    args = get_args()
    
    response = request(get_url(args.y, args.m))
    unzip_to_csv(response, './data/raw/cnpjs.full.csv')


if __name__ == '__main__':
    main()