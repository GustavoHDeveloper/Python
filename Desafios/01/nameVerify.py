def verify(nome):
  if nome.isnumeric() == True & len(nome) == 1:
    print("TEU NOME TEM 1 CARACTÉRE, E ELE É UM NÚMERO? KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
    exit()
  elif len(nome) == 1:
    print(f"Seu nome tem {len(nome)} letra? Sério isso?")
    exit()
  elif any(char.isdigit() for char in nome) == True:
    print("Teu nome tem número? KKKKKKKKKKKKKKKKK")
    exit()
  else:
    pass