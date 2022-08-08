# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

def verifica_escolha(numero):
	try:
		if(type(int(numero)) == int):
			if(int(numero) >= 1 and int(numero) <= 4):
				return True
			else:
				return False
		else:
			return False
	except Exception:
		return False
		
def verifica_numero(numero, posicao, operacao):
	if(type(float(numero)) != float):
		return "Digite apenas números!"
	elif(posicao == 2 and operacao == 4):
		return "Não é possível dividir por zero!"
	else:
		return "0"
		
def calcula(priNum, secNum, operacao):
	resultado = 0
	if(int(operacao) == 1):
		resultado = float(priNum) + float(secNum)
	elif(int(operacao) == 2):
		resultado = float(priNum) - float(secNum)
	elif(int(operacao) == 3):
		resultado = float(priNum) * float(secNum)
	elif(int(operacao) == 4):
		resultado = float(priNum) / float(secNum)
	return resultado

print("\n******************* Python Calculator *******************\n\n")

print("Selecione o número da opção desejada:\n\n")

print("1 - Soma\n")
print("2 - Subtração\n")
print("3 - Multiplicação\n")
print("4 - Divisão\n\n")

opcaoValida = False
while(opcaoValida == False):
	operacao = input("Digite sua opção: (1/2/3/4):")
	opcaoValida = verifica_escolha(operacao)
	if(opcaoValida == False):
		print("OPÇÃO INVÁLIDA!")

verifNum = "1"
while(verifNum != "0"):
	priNum = input("\n\nDigite o primeiro número:")
	verifNum = verifica_numero(priNum, 1, operacao)
	if(verifNum != "0"):
		print(verifNum)

verifNum = "1"
while(verifNum != "0"):
	secNum = input("\n\nDigite o segundo número:")
	verifNum = verifica_numero(secNum, 2, operacao)
	if(verifNum != "0"):
		print(verifNum)
		
if(int(operacao) == 1):
	sinal = " + "
elif(int(operacao) == 2):
	sinal = " - "
elif(int(operacao) == 3):
	sinal = " * "
else:
	sinal = " / "

print(priNum + sinal + secNum + " = " + str(calcula(priNum, secNum, operacao)))