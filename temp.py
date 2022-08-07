import numpy as np
import pickle

#load the saved model
loaded_model=pickle.load(open("D:/Courses/iNeuron/ML_webapp/trained_model.sav","rb"))

input_data=(892,2 , -1, -1, 8, 2, 25,1)
#change the input_data to numpy array
input_data_numpy=np.asarray(input_data)

#reshape the array
input_data_reshaped=input_data_numpy.reshape(1,-1)

prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
  print("Not Phishing Website")
else:
  print("Phishing Website")
