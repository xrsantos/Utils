import pandas as pd
from datetime import datetime
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
 
DIR = '/Users/noronha/Documents/Fazenda/Leite4.0'
df = pd.read_csv(DIR+'/dados.csv', sep=';', header=0)

X = df.iloc[:, 4:5] # Pegar somente descargas (variáveis independentes)
y = df.iloc[:, 0:1] # Pegar somente Producao Real (variável dependente)
print(X)            # Imprimindo as variáveis independentes

# Fitting Multiple Linear Regression to the Training set
regressor = LinearRegression()
regressor.fit(X, y)

# Predicting the Test set results
y_pred = regressor.predict(X)

from sklearn.metrics import r2_score
score=r2_score(y,y_pred)
print('Score: '+str(score))
print('Coefficients: \n', regressor.coef_)
print('intercept_: \n', regressor.intercept_)
print('Mean squared error: %.2f' % mean_squared_error(y, y_pred))
print('Coefficient of determination: %.2f' % r2_score(y, y_pred))

