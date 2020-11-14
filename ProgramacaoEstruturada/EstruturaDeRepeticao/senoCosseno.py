from math import sin, cos

for angulo in range(0,360,15):
  print()
  print("Cosseno de %d: %.2f"%(angulo, sin(angulo)))
  print("Seno de %d: %.2f"%(angulo, cos(angulo)))
