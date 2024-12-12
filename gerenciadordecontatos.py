class NoB:
    def __init__(self, ordem):
        self.ordem = ordem
        self.chaves = []
        self.filhos = []
        self.folha = True

    def inserir_na_folha(self, chave):
        i = len(self.chaves) - 1
        while i >= 0 and chave < self.chaves[i]:
            i -= 1
        self.chaves.insert(i + 1, chave)

    def dividir(self):
        meio = self.ordem // 2
        novo_no = NoB(self.ordem)
        novo_no.chaves = self.chaves[meio:]
        self.chaves = self.chaves[:meio]
        if not self.folha:
            novo_no.filhos = self.filhos[meio:]
            self.filhos = self.filhos[:meio]
            novo_no.folha = False
        return novo_no, self.chaves[meio - 1]

class ArvoreB:
    def __init__(self, ordem):
        self.raiz = NoB(ordem)
        self.ordem = ordem

    def inserir(self, chave):
        raiz = self.raiz
        if len(raiz.chaves) == (self.ordem - 1):
            novo_no = NoB(self.ordem)
            novo_no.folha = False
            novo_no.filhos.append(raiz)
            novo_no, chave_promovida = raiz.dividir()
            novo_no.chaves.insert(0, chave_promovida)
            novo_no.filhos.append(novo_no)
            self.raiz = novo_no
            self._inserir_no(novo_no, chave)
        else:
            self._inserir_no(raiz, chave)

    def _inserir_no(self, no, chave):
        if no.folha:
            no.inserir_na_folha(chave)
        else:
            i = len(no.chaves) - 1
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1
            if len(no.filhos[i].chaves) == (self.ordem - 1):
                novo_no, chave_promovida = no.filhos[i].dividir()
                no.chaves.insert(i, chave_promovida)
                no.filhos.insert(i + 1, novo_no)
                if chave < no.chaves[i]:
                    self._inserir_no(no.filhos[i], chave)
                else:
                    self._inserir_no(no.filhos[i + 1], chave)
            else:
                self._inserir_no(no.filhos[i], chave)

    def buscar(self, chave):
        return self._buscar(self.raiz, chave)

    def _buscar(self, no, chave):
        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1
        if i < len(no.chaves) and chave == no.chaves[i]:
            return True
        elif no.folha:
            return False
        else:
            return self._buscar(no.filhos[i], chave)

    def listar(self):
        return self._listar(self.raiz)

    def _listar(self, no):
        resultado = []
        for i in range(len(no.chaves)):
            if not no.folha:
                resultado.extend(self._listar(no.filhos[i]))
            resultado.append(no.chaves[i])
        if not no.folha:
            resultado.extend(self._listar(no.filhos[len(no.chaves)]))
        return resultado

# Exemplo de uso
arvore_b = ArvoreB(ordem=3)


arvore_b.inserir("Alice: 1234-5678")
arvore_b.inserir("Bob: 2345-6789")
arvore_b.inserir("Charlie: 3456-7890")
arvore_b.inserir("David: 4567-8901")


print(arvore_b.buscar("Bob: 2345-6789"))  # Saída: True
print(arvore_b.buscar("Eve: 5678-9012"))  # Saída: False


print(arvore_b.listar())