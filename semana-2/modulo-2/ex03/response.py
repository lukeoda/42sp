import httpx
import json
import sys

def do_GET(url: str) -> json:
    try:
        result = httpx.get(url)
        return result
    except httpx.ConnectError:
        print('Error: ConnectError')
        sys.exit(1)
        

def main():
    url = sys.argv[1]
    r_get = do_GET(url)
    print(f'{r_get.status_code} {r_get.reason_phrase}')


if __name__ == '__main__':
	main()