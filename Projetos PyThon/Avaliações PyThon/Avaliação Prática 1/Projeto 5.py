sexo=input('digite seu sexo:')
altura=float(input('digite sua altura:'))
if sexo=='masculino':
    masculino=(72.7*altura)-58
    print("se voce for homem, seu peso ideial seria {:.2f}".format(masculino))
elif sexo=="feminino":
    mulher=(62.1*altura)-44.7
    print("se voce for mulher, seu peso ideal {:.2f}".format(mulher))