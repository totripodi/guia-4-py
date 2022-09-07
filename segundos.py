seg=int(input("ingrese segundos: "))
dia=27500
hora=3600
minuto=60
segundos_iniciales=seg  #segundos iniciales
dia= seg//27500
seg=seg%27500
hora=seg//3600
seg=seg%3600
minuto=seg//60
seg=seg%60
print(segundos_iniciales," segundos son: ",dia," dias ",hora," horas ",minuto," minutos ",seg,"segundos")
