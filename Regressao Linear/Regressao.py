
#load file base.csv 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv('base.csv')

dados.head()
X = dados['X'].values
Y = dados['Y'].values
#plt.scatter(X,Y,label='Y(X)');
#plt.xlabel('X');
#plt.ylabel('Y');
#plt.legend();
#plt.show();
media_X = np.mean(X)
media_Y = np.mean(Y)
erro_x = X-media_X
erro_y = Y-media_Y
soma_erro_xy = np.sum(erro_x*erro_y)
erro_x_quadratico = (X-media_X)**2.0
soma_erro_x_quadratico = np.sum(erro_x_quadratico)
m = soma_erro_xy / soma_erro_x_quadratico
print("Coeficiente angular = {:0.2f}".format(m))
c = media_Y - m*media_X
print("Coeficiente linear = {:0.2f}".format(c))
reta = m*X+c
plt.scatter(X,Y,label='Salario X Idade');
plt.plot(X,reta,label='Ajuste linear',color='red');
plt.xlabel('Salario');
plt.ylabel('Idade');
plt.legend();
plt.show();

from sklearn.metrics import mean_absolute_error,mean_squared_error
MAE = mean_absolute_error(Y,reta)
RMSE = np.sqrt(mean_squared_error(Y,reta))
print("MAE = {:0.2f}".format(MAE))
print("RMSE = {:0.2f}".format(RMSE))


print("Finalizado");


















