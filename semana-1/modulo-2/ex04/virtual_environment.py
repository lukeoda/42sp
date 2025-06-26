import os

def is_venv_active() -> bool:
	return (os.environ.get('VIRTUAL_ENV') is not None)

def main():
	'''
	para ativar o ambiente virtual basta digitar 'source /nfs/homes/lkenji-o/Documents/venv/bin/activate'
	para desativar digite deactivate
	'''
	if is_venv_active():
		print('virtual environment active')
	else:
		print('virtual environment inactive')
		
		
if __name__ == '__main__':
	main()
	
