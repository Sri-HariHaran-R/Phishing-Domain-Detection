import numpy as np
import streamlit as st
import pickle

#loading the saved model
loaded_model=pickle.load(open("D:/Courses/iNeuron/ML_webapp/trained_model.sav","rb"))

#creating a function for prediction
def phishing(input_data):

    # change the input_data to numpy array
    input_data_numpy = np.asarray(input_data)

    # reshape the array
    input_data_reshaped = input_data_numpy.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return "Not Phishing Website"
    else:
        return "Phishing Website"

def main():

    #giving a title
    st.title("Phishing Domain Detection")

    #getting the input data from user

    ttl_hostname=st.text_input("ttl_hostname")
    qty_nameservers=st.text_input("qty_nameservers")
    time_domain_activation=st.text_input("time_domain_activation")
    qty_hyphen_file=st.text_input("qty_hyphen_file")
    directory_length=st.text_input("directory_length")
    qty_dot_domain=st.text_input("qty_dot_domain")
    length_url=st.text_input("length_url")
    qty_slash_url=st.text_input("qty_slash_url")

    #code for prediction
    result=""

    #create a button for prediction
    if st.button("Test"):
        result=phishing([ttl_hostname,qty_nameservers,time_domain_activation,qty_hyphen_file,directory_length,qty_dot_domain,length_url,qty_slash_url])

    st.success(result)

if __name__=='__main__':
    main()