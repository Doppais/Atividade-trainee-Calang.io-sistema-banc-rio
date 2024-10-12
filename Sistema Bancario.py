class Conta:
    titular=""
    saldo=0
    def __init__(self, titular) -> None:
        self.titular=titular
        self.saldo=0

    def depositar(self,deposito):
        self.saldo+=deposito

    def retirar(self,retirada):
        if self.saldo<retirada:
            return False
        else:
            self.saldo-=retirada
            return True

    def getSaldo(self):
        return self.saldo

class Repositorio:
    contas=[Conta]
    def busca(self,titular):
        if self.contas.count==0:
            return None
        for conta in self.contas:
            if conta.titular==titular:
                return conta
                break
        return None
    def add(self,titular):
        conta=self.busca(titular)
        if conta==None:
            self.contas.append(Conta(titular))
            return True
        return False

repositorio=Repositorio()

while True:
    print("Escolha uma opção")
    print("1. Criar nova conta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Verificar saldo")
    print("5. Sair")

    entrada=input("Digite o numero da sua escolha:")
    
    if entrada=="1":
        titular=input("Digite o nome do titular da nova conta:")
        if repositorio.add(titular):
            print(f"Conta criada com o titular {titular} com sucesso.")
        else:
            print("Esse titular já possui uma conta.")
            
    elif entrada=="2":
        titular=input("Digite o nome do titular da conta a receber o deposito:")
        contaAtual=repositorio.busca(titular)
        if contaAtual==None:
            print("Não existe titular com esse nome.")
        else:
            quantia=float(input("Digite a quantia a ser depositada: "))
            if quantia>0:
                contaAtual.depositar(quantia)
                print(f"Deposito de R${quantia:.2f} na conta de {titular} realizado com sucesso.")
            else:
                print("Valor de deposito invalido.")
    
    elif entrada=="3":
        titular=input("Digite o nome do titular a fazer o saque:")
        contaAtual=repositorio.busca(titular)
        if contaAtual==None:
            print("Não existe titular com esse nome")
        else:
            quantia=float(input("Digite a quantia a ser saquado: "))
            if quantia>0:
                if contaAtual.retirar(quantia):
                    print(f"Saque de R${quantia:.2f} na conta de {titular} realizado com sucesso.")
                else:
                    print("Valor de saque invalido. Consulte seu saldo.")
            else:
                print("Valor de saque invalido.")

    elif entrada=="4":
        titular=input("Digite o nome do titular a ser consultado:")
        contaAtual=repositorio.busca(titular)
        if contaAtual==None:
            print("Não existe titular com esse nome.")
        else:
            print(f"A conta de {titular} possui R${contaAtual.getSaldo():.2f} de saldo.")

    elif entrada=="5":
        print("Obrigado por usar o sistema bancário.")
        break
    else:
        print("Entrada invalida")
    
