from absl import*
from absn import*
from absi import*

l = lancamento ('CREED 3',10)
print('Diaria: R${:.2f}'.format(l.r_diaria()))

n = Comum ('Avatar 2',7)
print('Diaria: R${:.2f}'.format(n.r_diaria()))

i = infantil ('patas em furia',5)
print('Diaria: R${:.2f}'.format(i.r_diaria()))