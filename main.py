import argparse

def process(args):
    pass



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t', 
        '--ticker', 
        help='pass a single ticker symbol', 
        type=str, 
        default='AAPL'
    )

    args = parser.parse_args()
    process(*args)

