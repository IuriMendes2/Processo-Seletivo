# Nessa parte de cima eu declaro as variaveis que vão receber os inputs no caso anos, meses e dias 
print("Escreva sua idade em anos, meses e dias: ")

anos = int(input("Sua idade em anos: "))
meses = int(input("Sua idade em meses: "))
dias = int(input("Sua idade em dias: "))

# Agora e fazer a conta para conveter para dias

idade_em_dias = (anos*365)+(meses*30)+dias

print ("Sua idade em dias e de {} !".format(idade_em_dias))

