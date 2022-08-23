from math import pi
from time import sleep

print("""
Integrantes do grupo:
* Álvaro Coelho Jesus
* Fernando Shiraishi
* Vinicius Alves Pedro
""")

# Constantes:
u0 = 4*pi*(10**(-7)) # permeabilidade magnética do vácuo [H/m]
c = 3e8 # velocidade da luz [m/s]

# Funções de impressão:
def message():
  input("""\n--------------------------------
Pressione 'Enter' para continuar
--------------------------------
        """)
  
# Funções para os cálculos:
def calculateFromCampoEletrico(value):
	campoMagnetico = value / (c)
	intensidadeCampo = 0

	print(
		f"Amplitude do Campo Magnético: {campoMagnetico:.2e}\nIntensidade da onda eletromagnética: {intensidadeCampo:.2e}")


def calculateFromCampoMagnetico(value):
	campoEletrico = value * (c)
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
	comprimentoOnda = ((3*(10**8))/value)
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
      option = (input('Digite uma opção:'))
      if(option == '0'):
        sleep(1)
        print('Até a proxima...(^.^)')
        sleep(1)
        break
      elif(option == '1'):
        value = float(input('Digite o valor [V/m]:'))
        print()
        calculateFromCampoEletrico(value)
        message()
      elif(option == '2'):
        value = float(input('Digite o valor [T]:'))
        print()
        calculateFromCampoMagnetico(value)
        message()
      elif(option == '3'):
        value = float(input('Digite o valor [W/m]:'))
        print()
        calculateFromIntensidadeDaOonda(value)
        message()
      elif(option == '4'):
        value = float(input('Digite o valor [m]:'))
        print()
        calculateFromComprimentoDaOnda(value)
        message()
      elif(option == '5'):
        value = float(input('Digite o valor [Hz]:'))
        print()
        calculateFromFrequency(value)
        message()
      elif(option == '6'):
        value = float(input('Digite o valor [rad/s]:'))
        print()
        calculateFromFrequencyAngular(value)
        message()
      elif(option == '7'):
        value = float(input('Digite o valor [rad/m]:'))
        print()
        calculateFromNumeroDeOnda(value)
        message()
      else:
        print("\nComando inválido! Por favor, tente novamente.")
        message()


main()
