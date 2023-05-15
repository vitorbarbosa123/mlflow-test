import mlflow
logged_model = ''

loaded_model = mlflow.pyfunc.load_model(logged_model)

import panda as pd
data = pd.read_csv('../../data/processed/casas_X.csv')
predicted = loaded_model.predict(data)

data['predicted'] = predicted
data.to_csv('precos.csv')