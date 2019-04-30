import pylab as p, numpy as n

fig=p.figure(figsize=(6.,5.))
# p.subplots_adjust(left=0.09,bottom=0.15,right=0.95,top=0.81)
p.subplots_adjust(left=0.07, bottom=0.05, right=0.97, top=0.83, hspace=0.78)

N = 100.
y = n.ones(int(N))

yy = n.linspace(1,5,N)**-3

ax=p.subplot(211)
p.plot(y)
# p.ylabel(r'$y = p(k) * k^\alpha = C$')
p.ylabel(r'$p_U(k) = C$')
# p.yticks([1], [''])
p.yticks([], [])
p.xticks([], [])
p.xlabel(r'$k\;\;\;\rightarrow$')
p.title('Uniform distribution of resources', fontsize=10)
ax=p.subplot(212)
p.yticks([], [])
p.xticks([], [])
p.ylabel(r'$p(k) = C . k^{-\alpha}$')
p.xlabel(r'$k\;\;\;\rightarrow$')
p.title('Power-law distribution of resources', fontsize=10)
p.plot(yy)

p.text(25, 1.4, r'$\Downarrow\;\;p(k) . k^\alpha = C\;\;\Downarrow$', fontsize=18)

p.gcf().suptitle('From uniform to power-law', fontsize=22)

p.savefig("./uni2power.png")
# p.show()
