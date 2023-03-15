from sklearn.linear_model import LinearRegression

# Definimos nuestros datos de entrenamiento
X_train = [[1], [2], [3], [4], [5]]
y_train = [2, 4, 6, 8, 10]

# Creamos el modelo de regresión lineal
regression_model = LinearRegression()

# Entrenamos el modelo con nuestros datos de entrenamiento
regression_model.fit(X_train, y_train)

# Hacemos una predicción utilizando el modelo entrenado
X_test = [[7]]
predicted_value = regression_model.predict(X_test)

print(predicted_value)  # Salida: [12]
