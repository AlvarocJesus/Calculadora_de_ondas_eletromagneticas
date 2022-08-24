from math import pi, sqrt
from time import sleep

print("""
Integrantes do grupo:

* Álvaro Coelho Jesus | RA: 22.221.002-3
* Fernando Shiraishi | RA: 22.221.014-8
* Vinicius Alves Pedro | RA: 22.221.031-1
""")

# Constantes:
u0 = 4*pi*(10**(-7)) # permeabilidade magnética do vácuo [H/m]
c = 3e8 # velocidade da luz [m/s]

# Funções de impressão:
def message():
  input("""
--------------------------------
Pressione 'Enter' para continuar
--------------------------------
""")
  
# Funções para os cálculos:
def calculateFromCampoEletrico(value):
	campoMagnetico = value / (c)
	intensidadeCampo = value**2/(2*u0*c)
	print(
		f"Amplitude do Campo Magnético: {campoMagnetico:.2e} T\nIntensidade da onda eletromagnética: {intensidadeCampo:.2e} W/m^2")


def calculateFromCampoMagnetico(value):
	campoEletrico = value * (c)
	intensidadeCampo = c*(value**2)/(2*u0)
	print(
		f"Amplitude do Campo Elétrico: {campoEletrico:.2e} V/m\nIntensidade da onda eletromagnética: {intensidadeCampo:.2e} W/m^2")


def calculateFromIntensidadeDaOonda(value):
	campoMagnetico = sqrt(value*2*u0/c)
	campoEletrico = campoMagnetico*c
	print(
		f"Amplitude do Campo Elétrico: {campoEletrico:.2e} V/m\nAmplitude do Campo Magnético: {campoMagnetico:.2e} T")


def calculateFromComprimentoDaOnda(value):
	frequencia = c/value
	numeroOnda = 2*pi/value
	frequenciaAngular = 2*pi*frequencia
	print(
		f"Frequencia: {frequencia:.2e} Hz\nNumero de onda: {numeroOnda:.2e} rad/m\nFrequencia Angular: {frequenciaAngular:.2e} rad/s")


def calculateFromFrequency(value):
	frequenciaAngular = 2*pi*value
	comprimentoOnda = ((c)/value)
	numeroOnda = (2*pi)/comprimentoOnda
	print(
		f"Comprimento de onda: {comprimentoOnda:.2e} m\nNumero de onda: {numeroOnda:.2e} rad/m\nFrequência Angular: {frequenciaAngular:.2e} rad/s")


def calculateFromFrequencyAngular(value):
	frequencia = value/(2*pi)
	comprimentoOnda = c/frequencia
	numeroOnda = 2*pi/comprimentoOnda
	print(
		f"Frequência: {frequencia:.2e} Hz\nComprimento de onda: {comprimentoOnda:.2e} m\nNumero de onda: {numeroOnda:.2e} rad/m")


def calculateFromNumeroDeOnda(value):
	comprimentoOnda = 2*pi/value
	frequencia = c/comprimentoOnda
	frequenciaAngular = 2*pi*frequencia
	print(
		f"Frequência: {frequencia:.2e} Hz\nComprimento de onda: {comprimentoOnda:.2e} m\nFrequência Angular: {frequenciaAngular:.2e} rad/s")


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
      option = (input('Digite uma opção: '))
      if(option == '0'):
        sleep(1)
        print('Até a proxima...(^.^)')
        sleep(1)
        break
      elif(option == '1'):
        value = float(input('Digite o valor [V/m]: '))
        print()
        calculateFromCampoEletrico(value)
        message()
      elif(option == '2'):
        value = float(input('Digite o valor [T]: '))
        print()
        calculateFromCampoMagnetico(value)
        message()
      elif(option == '3'):
        value = float(input('Digite o valor [W/m^2]: '))
        print()
        calculateFromIntensidadeDaOonda(value)
        message()
      elif(option == '4'):
        value = float(input('Digite o valor [m]: '))
        print()
        calculateFromComprimentoDaOnda(value)
        message()
      elif(option == '5'):
        value = float(input('Digite o valor [Hz]: '))
        print()
        calculateFromFrequency(value)
        message()
      elif(option == '6'):
        value = float(input('Digite o valor [rad/s]: '))
        print()
        calculateFromFrequencyAngular(value)
        message()
      elif(option == '7'):
        value = float(input('Digite o valor [rad/m]: '))
        print()
        calculateFromNumeroDeOnda(value)
        message()
      else:
        print("\nComando inválido! Por favor, tente novamente.")
        message()

main()
