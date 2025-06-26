import httpx
import json

def do_GET(url: str) -> json:
    result = httpx.get(url)
    return result.json()

def main() -> None:
    r_get = do_GET('https://assets.breatheco.de/apis/fake/sample/project1.php')

    print(
        f"Projeto: '{r_get.get('name', 'Projeto não encontrado')}', Imagem:'{r_get.get('images', 'Projeto não encontrado')[0]}'"
        ) 
    
		
if __name__ == '__main__':
	main()