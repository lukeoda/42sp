from process import process_image
from PIL import Image

def test_process_image():
    process_image('42.jpg')
    im = Image.open('42_processed.jpg')
    
    assert im.mode == 'L'
    assert im.size == (500, 500)