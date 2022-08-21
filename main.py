from math import pi
from time import sleep

print("""
Integrantes do grupo:
Álvaro Coelho Jesus
Fernando Shiraishi
Vinícius Nanaki
""")


def calculateFromCampoEletrico(value):
	campoMagnetico = value / (3e8)
	intensidadeCampo = 0

	print(
		f"Amplitude do Campo Magnético: {campoMagnetico:.2e}\nIntensidade da onda eletromagnética: {intensidadeCampo:.2e}")


def calculateFromCampoMagnetico(value):
	campoEletrico = value * (3e8)
	intensidadeCampo = 0
	print(
		f"Amplitude do Campo Magnético: {campoEletrico:.2e}\nIntensidade da onda eletromagnética: {intensidadeCampo:.2e}")


def calculateFromIntensidadeDaOonda(option):
	campoMagnetico = 0
	campoEletrico = 0
	print(
		f"Amplitude do Campo Magnético: {campoMagnetico:.2e}\nAmplitude do Campo Elétrico: {campoEletrico:.2e}")


def calculateFromComprimentoDaOnda(option):
	frequencia = 0
	numeroOnda = 0
	frequenciaAngular = 0
	print(
		f"Frequencia: {frequencia:.2e}\nNumero de onda: {numeroOnda:.2e}\nFrequencia Angular: {frequenciaAngular:.2e}")


def calculateFromFrequency(value):
	frequenciaAngular = 2*pi*value
	comprimentoOnda = 2*pi*((3*10**8)/frequenciaAngular)
	numeroOnda = (2*pi)/comprimentoOnda
	print(
		f"Comprimento de onda: {comprimentoOnda:.2e}\nNumero de onda: {numeroOnda:.2e}\nFrequência Angular: {frequenciaAngular:.2e}")


def calculateFromFrequencyAngular(option):
	frequencia = 0
	numeroOnda = 0
	comprimentoOnda = 0
	print(
		f"Frequência: {frequencia:.2e}\nComprimento de onda: {comprimentoOnda:.2e}\nNumero de onda: {numeroOnda:.2e}")


def calculateFromNumeroDeOnda(option):
	frequencia = 0
	comprimentoOnda = 0
	frequenciaAngular = 0
	print(
		f"Frequência: {frequencia:.2e}\nComprimento de onda: {comprimentoOnda:.2e}\nFrequência Angular: {frequenciaAngular:.2e}")


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
		option = int(input('Digite uma opção:'))
		if(option == 0):
			sleep(1)
			print('Ate a proxima...')
			sleep(1)
			break
		elif(option == 1):
			value = float(input())
			calculateFromCampoEletrico(value)
			sleep(1)
		elif(option == 2):
			value = float(input())
			calculateFromCampoMagnetico(value)
			sleep(1)
		elif(option == 3):
			value = float(input())
			calculateFromIntensidadeDaOonda(value)
			sleep(1)
		elif(option == 4):
			value = float(input())
			calculateFromComprimentoDaOnda(value)
			sleep(1)
		elif(option == 5):
			value = float(input())
			calculateFromFrequency(value)
			sleep(1)
		elif(option == 6):
			value = float(input())
			calculateFromFrequencyAngular(value)
			sleep(1)
		elif(option == 7):
			value = float(input())
			calculateFromNumeroDeOnda(value)
			sleep(1)


main()
