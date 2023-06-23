import streamlit as st
import pandas as pd
import numpy as np
import joblib
import warnings
from sklearn.preprocessing import  LabelEncoder







model = joblib.load("dctCV_obj.pkl")

def predict(model, df_input):
  predictions_df = model.predict(df_input)
  predictions = predictions_df[0]
  return predictions

def encoder(df):
  le = LabelEncoder()
  for col in df.columns:
      if df[col].dtype == "object" or df[col].dtype == "category":
          df[col] = le.fit_transform(df[col])
  return df

def main():

  st.title(":Portugese Bank Instution: Bank Marketing Prediction App")
  st.write("Please input the data for prediction:")
  st.write("Note there is no option to select duration as the duration is not known before a call is performed")
  st.write("As its also stated in the source of the data and notepad of the project duration needs to be removed for realistic prediction")

  age = st.number_input("Select age", min_value=0, max_value=100,step=1)
  job = st.selectbox("Select Job", options = ["admin.","blue-collar","entrepreneur","housemaid","management","retired","self-employed","services","student","technician","unemployed","unknown"])
  marital = st.selectbox("Select Marital Status", options = ["divorced","married","single"])
  education = st.selectbox("Select Education Level", options = ["basic.4y","basic.6y","basic.9y","high.school","illiterate","professional.course","university.degree"])
  default = st.selectbox("Select Whether The Person Has Credit In Default", options = ["no","yes"])
  housing = st.selectbox("Select Whether The Person Has Housing Loan", options = ["no","yes"])
  loan = st.selectbox("Select Whether The Person Has Personal Loan", options = ["no","yes"])
  contact = st.selectbox("Select Contact Communication Type", options = ["cellular","telephone"])
  
  month = st.selectbox("Select Last Contact Month Of The Year", options = ['may', 'jun', 'jul', 'aug', 'oct', 'nov', 'dec', 'mar', 'apr','sep'])
  
  day_of_week = st.selectbox("Select Last Contact Day Of The Week", options = ["mon","tue","wed","thu","fri"])
  
  campaign = st.number_input("Number of contacts performed during this campaign and for this client", min_value=0)
  #contacted_before = st.number_input("Enter 1 If The Person Was Not Contacted before i.e pdays Is 999 Else Enter 0",)
  pdays = st.number_input("Number of days that passed by after the client was last contacted from a previous campaign", min_value=0, max_value=999)
  previous = st.number_input("number of contacts performed before this campaign and for this client", min_value=0)
  
  poutcome = st.selectbox("outcome of the previous marketing campaign", options = ["failure","success"])
  
  emp_var_rate = st.number_input("employment variation rate - quarterly indicator")
  cons_price_idx = st.number_input("consumer price index - monthly indicator")
  cons_conf_idx = st.number_input("consumer confidence index - monthly indicator")
  euribor3m = st.number_input("euribor 3 month rate - daily indicator")
  nr_employed = st.number_input("number of employees - quarterly indicator")

  cols = {
    "age" : age,
    "job":job,
    "marital":marital,
    "education":education,
    "default":default,
    "housing":housing,
    "loan":loan,
    "contact":contact,
    "month":month,
    "day_of_week":day_of_week,
    "campaign":campaign,
    "pdays":pdays,
    "previous":previous,
    "poutcome":poutcome,
    "emp.var.rate":emp_var_rate,
    "cons.price.idx":cons_price_idx,
    "cons.conf.idx":cons_conf_idx,
    "euribor3m":euribor3m,
    "nr.employed":nr_employed
  }
  
  df = pd.DataFrame(cols,index=[0])


  

  if st.button("Predict"):
    df = encoder(df)
    prediction = predict(model, df)
  
    if prediction >= 0.725455:
      prediction ="Yes"
    else:
      prediction = "No"
    st.success(f"Prediction : {prediction}")

if __name__ == "__main__":
  main()
