import httpx
import json

def do_GET(url: str) -> json:
    result = httpx.get(url)
    return result

def do_POST(url: str) -> json:
    data = { "title": "foo", "body": "bar", "userId": 1 }
    result = httpx.post(url, data=data)
    return result

def main() -> None:
    r_get = do_GET('https://jsonplaceholder.typicode.com/posts/1')
    print(f'{r_get.status_code} {r_get.json()}')
    r_post = do_POST('https://jsonplaceholder.typicode.com/posts')
    print(f'{r_post.status_code} {r_post.json()}')
		
if __name__ == '__main__':
	main()