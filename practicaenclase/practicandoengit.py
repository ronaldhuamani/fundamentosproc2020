def calcularcostopolisaFRHH():
    #datos de entrada
    tipoplan=str(input("ingrese el plan que desee el cliente:"))
    alcohol=bool(input("el cliente consume alcohol?:"))
    lentes=bool(input("el cliente usa lentes?:"))
    enfermedad=bool(input("tiene alguna enfermedad?:"))
    edad=int(input("que edad tiene?:"))
    #proceso


    if tipoplan=="A":
        costobase=1200
    else:
        costobase=950
    if alcohol==1:
        costobase=costobase+(costobase*0.10)
    if lentes==1:
        costobase=costobase+(costobase*0.5)
    if enfermedad==1:
        costobase=costobase+(costobase*0.5)
    print("VER:",enfermedad)
    if edad>40:
        costobase=costobase+(costobase*0.20)
    else:
        costobase=costobase+(costobase*0.10)
    #datos de salida
    print("el costo de la polisa es:", costobase)

calcularcostopolisaFRHH()