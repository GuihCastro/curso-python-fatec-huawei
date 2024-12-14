"""
Responda a seguinte questão. A inicialização das listas foi feita da seguinte forma:
LstNeg = []
LstPos = []
por quê a solução 7.4 ficaria errada se a inicialização das listas fosse feita assim?
LstNeg = LstPos = []
Justifique sua resposta.
Dicas: a) altere o programa do exercício resolvido 7.4 e teste para ver o que acontece;
b) releia as seções 2.3, 2.4 e 7.2.5
"""

# Porque, neste caso, ambos os objetos apontariam para a mesma lista na memória, fazendo com que a alteração de um
# objeto afetasse o outro.