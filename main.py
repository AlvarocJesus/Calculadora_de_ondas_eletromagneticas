from time import sleep

print("""
Integrantes do grupo:
Álvaro Coelho Jesus
Fernando Shiraishi
Vinícius Nanaki
""")


def calculateFromCampoEletrico(option):
	campoMagnetico = 0
	intensidadeCampo = 0

	print(
		f"Amplitude do Campo Magnético: {campoMagnetico}\nIntensidade da onda eletromagnética: {intensidadeCampo}")


def calculateFromCampoMagnetico(option):
	campoEletrico = 0
	intensidadeCampo = 0
	print(
		f"Amplitude do Campo Magnético: {campoEletrico}\nIntensidade da onda eletromagnética: {intensidadeCampo}")


def calculateFromIntensidadeDaOonda(option):
	campoMagnetico = 0
	campoEletrico = 0
	print(
		f"Amplitude do Campo Magnético: {campoMagnetico}\nAmplitude do Campo Elétrico: {campoEletrico}")


def calculateFromComprimentoDaOnda(option):
	frequencia = 0
	numeroOnda = 0
	frequenciaAngular = 0
	print(
		f"Frequencia: {frequencia}\nNumero de onda: {numeroOnda}\nFrequencia Angular: {frequenciaAngular}")


def calculateFromFrequency(option):
	comprimentoOnda = 0
	numeroOnda = 0
	frequenciaAngular = 0
	print(
		f"Comprimento de onda: {comprimentoOnda}\nNumero de onda: {numeroOnda}\nFrequência Angular: {frequenciaAngular}")


def calculateFromFrequencyAngular(option):
	frequencia = 0
	numeroOnda = 0
	comprimentoOnda = 0
	print(
		f"Frequência: {frequencia}\nComprimento de onda: {comprimentoOnda}\nNumero de onda: {numeroOnda}")


def calculateFromNumeroDeOnda(option):
	frequencia = 0
	comprimentoOnda = 0
	frequenciaAngular = 0
	print(
		f"Frequência: {frequencia}\nComprimento de onda: {comprimentoOnda}\nFrequência Angular: {frequenciaAngular}")


def main():
	while(True):
		print("\n-----------------Menu-----------------")
		print("""Indique a sua entrada:
1 - Amplitude Campo Elétrico
2 - Amplitude Campo Magnético
3 - Intensidade da onda
4 - Comprimento de onda
5 - Frequência
6 - Frequência angular
7 - Número de onda

0 - Sair
		""")
		option = float(input('Digite uma opção:'))
		if(option == 0):
			sleep(1)
			print('Ate a proxima...')
			sleep(1)
			break
		elif(option == 1):
			calculateFromCampoEletrico(option)
			sleep(1)
		elif(option == 2):
			calculateFromCampoMagnetico(option)
			sleep(1)
		elif(option == 3):
			calculateFromIntensidadeDaOonda(option)
			sleep(1)
		elif(option == 4):
			calculateFromComprimentoDaOnda(option)
			sleep(1)
		elif(option == 5):
			calculateFromFrequency(option)
			sleep(1)
		elif(option == 6):
			calculateFromFrequencyAngular(option)
			sleep(1)
		elif(option == 7):
			calculateFromNumeroDeOnda(option)
			sleep(1)


main()
