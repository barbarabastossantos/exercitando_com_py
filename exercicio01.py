# Crie um programa que peça ao usuario para criar uma senha  e depois digitar a senha novamnete para confirmar
# Se a senha estiver errada o programa deve pedir para tentar novamnete
# So pode sair quando a senha estiver correta


senha = int(input(" Crie uma senha numerica : "))

nova_senha = int(input(" Confirme sua senha : "))

while nova_senha != senha:
  print("SENHA INCORRETA")
  nova_senha = int(input(" Confirme sua senha : "))
  if nova_senha == senha:
   print("entrando")