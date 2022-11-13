def restricao(f,h):
    cont4=0
    cont5=0
    for m in (vetor3): # restricao para substituiçao do item
     if m==f:
      cont4=cont4+1
      if cont4>1:
        vetor3.pop()
        vetor4.pop()
        for n in (vetor3): # substituindo o item
          if n==f:
            cont5=cont5+1
            if cont5==1:
              vetor4[vetor3.index(n)]=h
              print('\no produto antigo (de mesmo modelo) foi substituido pelo atual!\n') # aviso
def restricao2(b):
    cont6=0
    for o in (vetor1): # restricao para remover repeticoes
     if o==b:
      cont6=cont6+1
      if cont6>1:
        vetor1.pop()
        print('\npor favor, nao repita o mesmo item!\n')              
cont1=0 # contador
cont2=0 # contador
cont3=0 # contador
vetor1=['ps5','headset'] # vetor auxiliar com itens pre-selecionados
vetor2=[] # vetor auxiliar
vetor3=[] # vetor auxiliar
vetor4=[] # vetor auxiliar
print('veja abaixo o menu de produtos que estao disponiveis!')
print('\n\n**************************************************************************************')
print('menu de produtos')
print('**************************************************************************************')
for i in range(0,(len(vetor1))):
  print('item: ',vetor1[i])  # imprimindo itens
print('**************************************************************************************\n\n')
a=str(input('\ndeseja cadastrar um produto? escreva "sim" ou "nao" \n')) # cadastrando itens
if(a=='sim'):
  while(cont1!=1):
      b=str(input('\nqual e o produto (nao repita o mesmo item)? \n')) #escolhendo itens
      vetor1.append(b)
      restricao2(b)
      d=str(input('\ndeseja pular? escreva "sim" ou "nao" \n'))
      if (d=='sim'):
        cont1=cont1+1
  print('\n\n**************************************************************************************')
  print('itens cadastrados')
  print('**************************************************************************************')
  for i in range(0,(len(vetor1))):
    print('item cadastrado: ',vetor1[i]) # imprimindo itens cadastrados
print('**************************************************************************************\n\n\n')
print('\n\n**************************************************************************************')
print('menu de produtos')
print('**************************************************************************************')
for i in range(0,(len(vetor1))):
  print('item: ',vetor1[i])
print('**************************************************************************************\n\n')
p=str(input('\ndeseja listar algum produto? escreva "sim" ou "nao" \n')) # cadastrando itens
if(p=='sim'):
  print('\nagora, voce deve selecionar os itens que irao para o carrinho de compras!\n')
  while(cont2!=1):
    f=str(input('\nescolha um item: \n')) # listando itens
    h=int(input('\nquantos? \n')) # quantidade de itens escolhidos
    if ((f in vetor1)==True): # restricao que associa o 'cadastro' com a 'listagem'
      vetor3.append(f)
      vetor4.append(h)
      restricao(f,h)
    else:
      print('\nitem nao-adicionado! indique apenas um item que foi cadastrado!\n')
    g=str(input('\nmais algum produto? escreva "sim" ou "nao" \n'))
    if (g=='nao'):
      for i in range(0,len(vetor3)):
        print('\nitem escolhido: ',vetor3[i],'; quantidade depois da escolha:', vetor4[i])  
      cont2=cont2+1
  j=str(input('\ndeseja remover algum produto? escreva "sim" ou "nao" \n')) # removendo algum item da lista de compras
  if (j=='sim'):
    while(cont3!=1):
      n=str(input('\nainda quer remover? escreva "sim" ou "nao" \n'))
      if (n=='sim'):
          k=str(input('\nqual item? \n'))
          vetor4.remove(vetor4[vetor3.index(k)])
          vetor3.remove(k)
          print('\no item ',k,'foi removido!\n')
      else:
        cont3=cont3+1    
  if vetor3!=[]:
    l=str(input('\ndeseja efetuar a compra? escreva "sim" ou "nao"\n')) # finalizando a compra
    if (l=='sim'):
      print('\n\n**************************************************************************************')
      print('itens selecionados para uma possivel compra')
      print('**************************************************************************************')
      for i in range(0,len(vetor3)):
        print('item escolhido: ',vetor3[i],'; quantidade depois da escolha:', vetor4[i])
      print('**************************************************************************************\n\n')
      print('\ncompra efetuada!\nobrigado pela visita!')
    else:
      print('\ncompra nao-finalizada!\n')
else:
  print('\nobrigado pela visita!')
  