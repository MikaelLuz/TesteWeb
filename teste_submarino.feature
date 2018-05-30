Feature: Teste navegacao

	Scenario: Navegar ate viagem
		Given estou na tela main
		When vou para tela de viagens
		Then aparece o titulo de viagem
		
	Scenario: Escolher viagem
		Given estou na pagina de viagens
		When preencho o formulario de busca
		Then aparece o resultado da busca		