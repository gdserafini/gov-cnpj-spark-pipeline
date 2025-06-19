import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', type=int, required=False)
    parser.add_argument('-m', type=int, required=False)
    return parser.parse_args()
