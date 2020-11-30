texto = 'Vamos para a festa'
d = dict()
for i in texto:
  if i not in d:
    d[i] = 1
  else:
    d[i] = d[i] + 1

print(d)
