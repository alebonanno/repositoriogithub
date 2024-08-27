# 1.b. Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y cuando las letras que componen dicha palabra estén en orden alfabético, y False en caso contrario

def es_abc(palabra):
  for i in range(1, len(palabra)):
    if palabra[i - 1] > palabra[i]:
      return False
  return True

print (es_abc('agbc'))