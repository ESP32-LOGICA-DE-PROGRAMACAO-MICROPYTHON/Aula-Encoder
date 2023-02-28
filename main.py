from machine import Pin
from time import sleep_us

pino_conectado_a_A = Pin(26, Pin.IN)
pino_conectado_a_B = Pin(27, Pin.IN)

contador_de_posicao = 0

valor_de_A_em_t = pino_conectado_a_A.value()

while True:
  valor_de_A_em_t_mais_um = pino_conectado_a_A.value()

  if valor_de_A_em_t_mais_um != valor_de_A_em_t:
    valor_de_B_em_t_mais_um = pino_conectado_a_B.value()

    if valor_de_A_em_t_mais_um == 0 and valor_de_B_em_t_mais_um == 1:
      contador_de_posicao+=1
      print("Sentido horário ->")
      print("Contador de posição:",contador_de_posicao)
      
    elif valor_de_A_em_t_mais_um == 0 and valor_de_B_em_t_mais_um == 0:
      contador_de_posicao-=1
      print("Sentido anti horário <-")
      print("Contador de posição:",contador_de_posicao)
    
    valor_de_A_em_t = valor_de_A_em_t_mais_um
    sleep_us(100)
