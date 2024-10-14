import math
from math import sin, cos, tan

ang = float(input('Digite o ângulo que deseja saber o seno, cosseno e tangente: '))
ang1 = math.radians(ang)
seno = math.sin(ang1)
cose = math.cos(ang1)
tang = math.tan(ang1)

print(f'Com o ângulo de {ang1:.2f}º, o seno é {seno:.2f} e a tangente é {tang:.2f}.')
