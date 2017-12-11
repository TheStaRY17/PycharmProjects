import numpy as np
import matplotlib as plt
la = np.linalg
words = ["I","like","enjoy","deep","learing","NLP","flying","."]
x = np.array([[0,2,1,0,0,0,0,0],
              [2,0,0,1,0,1,0,0],
              [1,0,0,0,0,0,1,0],
              [0,1,0,0,1,0,0,0],
              [0,0,0,1,0,0,0,1],
              [0,1,0,0,0,0,0,1],
              [0,0,1,0,0,0,0,1],
              [0,0,0,0,1,1,1,0]])
U , s ,Vh =la.svd(x,full_matrices=False)
for i in x (len(words)):
    plt.text(U[i,0],U[i,1],words[i])
