def list_of_names(dicionario: dict[str, str]) -> list[str]:
	'''
	para rodar esse projeto basta abrir o terminal
	digite 'python3'
	e rode o comando 'from your_namebook import list_of_names'
	crie um dicionario com os nomes
	persons = {
		"jean": "valjean",
		"grace": "hopper",
		"xavier": "niel",
		"fifi": "brindacier"
	}
	e chame a funcao 'list_of_names(persons)'

	
	
	'''	
	return [
		f"{nome.title()} {sobrenome.title()}" for nome, sobrenome in dicionario.items()
	]
