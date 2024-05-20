# Crie uma classe Televisao e uma classe ControleRemoto que pode controlar o volume e trocar os canais da
# televisão. O controle de volume permite: aumentar ou diminuir a potência do volume de som em uma unidade
# de cada vez; aumentar e diminuir o número do canal em uma unidade, trocar para um canal indicado; consultar
# o valor do volume de som e o canal selecionado. A classe controle remoto deve possuir um menu iterativo para
# o usuário escolher as opções desejadas.

class Televisao:
    def __init__(self):
        self._volume = 0
        self._canal = 0
    
    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self, input_volume):
        self._volume = input_volume
    
    @property
    def canal(self):
        return self._canal
    
    @canal.setter
    def canal(self, input_canal):
        self._canal = input_canal
        
    def aumenta_volume(self):
        if self.volume < 100: # Eu suponho que o volume máximo seja 100, pelo menos no geral das televisões.
            self.volume += 1
        else:
            print("Volume já está no máximo.")
    
    def diminui_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume já está no mínimo.")
            
    def aumenta_canal(self):
        self.canal += 1
        
    def diminui_canal(self):
        if self.canal > 0:
            self.canal -= 1
        else:
            print("Canal já está no mínimo.")
            
    def troca_canal(self, input_canal):
        if input_canal >= 0:
            self.canal = input_canal
        else:
            print("Canal inválido.")
            
    def consulta_volume(self):
        print(f"Volume: {self.volume}")
    
    def consulta_canal(self):
        print(f"Canal: {self.canal}")
        
        
class ControleRemoto:
    def __init__(self, televisao):
        self._televisao = televisao
        
    def menu(self):
        while True:
            print("1. Aumentar volume")
            print("2. Diminuir volume")
            print("3. Aumentar canal")
            print("4. Diminuir canal")
            print("5. Trocar canal")
            print("6. Consultar volume")
            print("7. Consultar canal")
            print("0. Sair")
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                self._televisao.aumenta_volume()
            elif opcao == 2:
                self._televisao.diminui_volume()
            elif opcao == 3:
                self._televisao.aumenta_canal()
            elif opcao == 4:
                self._televisao.diminui_canal()
            elif opcao == 5:
                canal = int(input("Digite o canal: "))
                self._televisao.troca_canal(canal)
            elif opcao == 6:
                self._televisao.consulta_volume()
            elif opcao == 7:
                self._televisao.consulta_canal()
            elif opcao == 0:
                break
            else:
                print("Opção inválida.")
                
televisao = Televisao()
controle = ControleRemoto(televisao)
controle.menu()