
import sys
from PIL import Image

def process_image(image: Image.Image) -> Image.Image:
    name = image.split('.')[0]
    img = Image.open(image)
    # Resize the image
    resized_img = img.resize((500, 500))
    resized_img.save(f'{name}_processed.jpg')
    grayscale_img = resized_img.convert("L")
    grayscale_img.save(f'{name}_processed.jpg')
    print(f'{name}_processed.jpg saved!')


def main() -> None:
    '''
	para rodar o programa basta digitar o comando
    'python3 process.py 42.jpg'

	'''
    filename = sys.argv[1]	
    process_image(filename)
		
if __name__ == '__main__':
	main()
	