import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

# Fix the random state seed for reproducibility
np.random.seed(1234)

"""
1.a The arguments to the distribution function are saved into variables
    to facilitate amendments
"""
N = 500
dist_args = { 'x1':[-2.5, 1], 'x2':[2, 1.5], 'x3':[2, 6], 'x4':[14, 20] }

""" 
1.b Generate each series with its functional form as string;
    Each named argument of the generating function was assigned to show the relation to the mathematical form.
""" 
x1 = np.random.normal( loc=dist_args['x1'][0], scale=dist_args['x1'][1], size=N )
px1 = r'$ ( \frac{ 1 }{ \sqrt{ 2 \pi \sigma^2 } } )e^ - \frac{ (x-\mu)^2 } {2\sigma^2}$' + \
      '\n' + r'$\mu=' + str( np.round(x1.mean(), 1) ) +'$' + \
      '\n' + r'$\sigma=' + str( np.round(x1.std(), 1) ) + '$'   

k = dist_args['x2'][0]
theta = dist_args['x2'][1]
x2 = np.random.gamma( shape=k, scale=theta, size=N )
# shape/scale form:
px2 = r'$ \frac{ 1 }{ \theta^k \Gamma(k) } x^{(k-1)}e^{-\frac{x}{\theta}}$' + \
      '\n' + r'$k=' + str(k) + r'; \theta=' + str(theta) + '$' + \
      '\n' + r'$\mu=' + str( np.round(x2.mean(),1) ) +'$' + \
      '\n' + r'$\sigma=' + str( np.round(x2.std(), 1) ) + '$'

"""
# shape/rate=(alpha/beta) form of the G-dist:
px2 = r'$ \frac{ \theta^k }{ \Gamma(k) } x^{(k-1)}e^{ -\theta x } $' + \
      '\n' + r'$k=' + str(k) + r'; \theta=' + str(theta) + '$' + \
      '\n' + r'$\mu=' + str( np.round(x2.mean(),1) ) +'$' + \
      '\n' + r'$\sigma=' + str( np.round(x2.std(), 1) ) + '$'
"""        
x3_shift = dist_args['x3'][1]
x3_beta = dist_args['x3'][0]
x3 = np.random.exponential( scale=x3_beta, size=N ) + x3_shift
px3 = r'$ \frac{1}{\beta} e^{ (\frac{-x}{\beta}) } + shift$' + \
      '\n' + r'$\beta=' + str(x3_beta) + r'; shift=' + str(x3_shift) + '$' + \
      '\n' + r'$\mu=' + str( np.round(x3.mean(),1) ) + '$' + \
      '\n' + r'$\sigma=' + str( np.round(x3.std(), 1) ) + '$'

b = dist_args['x4'][1]
a = dist_args['x4'][0]
x4 = np.random.uniform( low=a, high=b, size=N)
px4 = r'$ \frac{1}{b - a} $' + '\n' + r'$b=' + str(b) + r'; a=' + str(a) + '$' + \
      '\n' + r'$\mu=' + str( np.round(x4.mean(),1) ) + '$' + \
      '\n' + r'$\sigma=' + str( np.round(x4.std(), 1) ) + '$'
        

### Plot the histograms
fig = plt.figure(figsize=(12,6))

nbins = 20
transpcy=0.5
plt.hist(x1, normed=True, bins=nbins, alpha=transpcy)
plt.hist(x2, normed=True, bins=nbins, alpha=transpcy)
plt.hist(x3, normed=True, bins=nbins, alpha=transpcy)
plt.hist(x4, normed=True, bins=nbins, alpha=transpcy)

### Set current axes limits to fit all 4 dist on same scale
minX = round(dist_args['x1'][0], 1) - x3.var()
maxX = round(dist_args['x4'][0], 1) + x4.var()*2.5
minY = 0
maxY = 0.6
plt.axis( [minX, maxX, minY, maxY] )

offset=1.85
ypos=0.63

fsize=16
hal, val = 'left', 'top'

plt.text(x1.mean()-offset, ypos, 'x1: Normal\n' + px1 , fontsize=fsize, horizontalalignment=hal, verticalalignment=val)
plt.text(x2.mean()-offset, ypos, 'x2: Gamma\n' + px2, fontsize=fsize, horizontalalignment=hal, verticalalignment=val)
plt.text(x3.mean()-offset, ypos, 'x3: Exp\'l (shifted)\n' + px3, fontsize=fsize, horizontalalignment=hal, verticalalignment=val)
plt.text(x4.mean()-offset, ypos, 'x4: Uniform\n' + px4, fontsize=fsize, horizontalalignment=hal, verticalalignment=val)

ax = plt.gca()
ax.tick_params(top='off')
ax.spines['top'].set_color('none')
  
plt.subplots_adjust( wspace=5, hspace=13)
# subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)

txt = '$ \Gamma(k)=\int^{\infty}_{0}x^{(k-1)}e^{-x}dx$' 
ax.text( x=2, y=-0.08, s= 'Note: '+ txt, fontsize=14, ha='center')

plt.show()

fig.savefig( filename='img/Four distributions.svg', dpi=512, 
             orientation='landscape', transparent=True, frameon=None, bbox_inches='tight')