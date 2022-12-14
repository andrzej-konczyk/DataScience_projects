import numpy as np
import pandas as pd
import pickle 
import streamlit as st

import asyncio
import aiohttp

import xgboost as xgb

from sklearn.model_selection import train_test_split

import os


# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://httpbin.org/get') as resp:
#             print(resp.status)
#             print(await resp.text())

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# loop.run_until_complete(main())


# pickle_a=open('sqrt_xgb.pkl',"rb")
# model_v2=pickle.load(pickle_a) # our model
cwd = os.getcwd().replace('\\','/') #current working directory

file = pd.read_csv('C:/Users/andrz/Desktop/ISA/Projekt/jdszr6-grupa-bez-nazwy/ML_project/insurance.csv')

file['user_ID'] = pd.DataFrame(file.index).astype(int)
file = file[['user_ID', 'age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']]

file_dummies = pd.get_dummies(file[['sex', 'smoker', 'region']])
file_dummies['user_ID'] = file['user_ID']

file = pd.merge(file, file_dummies, on='user_ID')
file = file[['user_ID', 'age', 'sex_female', 'sex_male', 'bmi', 'children', 'smoker_yes', 'region_northeast', 'region_northwest', 'region_southeast', 'region_southwest', 'charges']]
file = file.sort_values(by='user_ID')
file = file[['age', 'sex_female', 'sex_male', 'bmi', 'children', 'smoker_yes', 'region_northeast', 'region_northwest', 'region_southeast', 'region_southwest', 'charges']]


X = file.drop(columns=['charges'], axis=1)
y = file['charges']

X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=42)
y_train_sqrt=np.sqrt(y_train)

model_v2=xgb.XGBRegressor( base_score=0.5, booster='gbtree', colsample_bylevel=1,
             colsample_bynode=1, colsample_bytree=0.7, enable_categorical=False,
             gamma=0.01, gpu_id=-1, importance_type=None,
             interaction_constraints='', learning_rate=0.05, max_delta_step=0,
             max_depth=3, min_child_weight=1,
             monotone_constraints='()', n_estimators=150, n_jobs=8,
             num_parallel_tree=1, predictor='auto', random_state=0, reg_alpha=0,
             reg_lambda=1, scale_pos_weight=1, subsample=1, tree_method='exact',
             validate_parameters=1, verbosity=None)

model_v2.fit(X_train,y_train_sqrt)


def predict_chance(df_pred):

    prediction=(model_v2.predict(df_pred))**2 #predictions using our model
    return prediction 


def main():
    # st.title("Health Insurance Prediction") #simple title for the app
    html_temp="""
        <div>
        <body bgcolor ='deepskyblue1'>
            <h1><font size ='10' color='green'><center>Health Insurance Prediction</center></p></center></font></h1>
        </body>
        <h2><font size ='6' color ='blue'><center>Calculation of health insurance charge value and potential offer for cost reduction</center></p></font></h2>
        </body>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True) #a simple html 
    age=st.selectbox("Enter your age", range(100))
    pass
    sex=st.selectbox("Select Your gender", ['male', 'female'])
    pass
    weight=st.selectbox("Enter Your weight", range(1,250))
    pass
    height=st.selectbox("Enter Your height", range(1,230))
    pass
    children = st.selectbox('Enter no of Your children', range(10))
    pass
    smoker=st.selectbox('Are You currently smoking?', ['yes', 'no']) 
    pass
    region=st.selectbox('Enter Your region', ['southeast', 'northeast', 'southwest', 'nothwest'])
    pass
    bmi = weight / (height**2)

    df_pred = pd.DataFrame(data=[[
                                age,
                                (lambda x: 1 if x == 'male' else 0)(sex),
                                (lambda x: 1 if x == 'female' else 0)(sex),
                                bmi,
                                children,
                                (lambda x: 1 if x == 'yes' else 0)(smoker),
                                (lambda x: 1 if x == 'northeast' else 0)(region),
                                (lambda x: 1 if x == 'northwest' else 0)(region),
                                (lambda x: 1 if x == 'southeast' else 0)(region),
                                (lambda x: 1 if x == 'southwest' else 0)(region)
                                ]],
                            columns = X.columns)

    result=""
    if st.button("Predict"):
        result=predict_chance(df_pred) #result will be displayed if button is pressed
    st.success("The predicted value of Your charge is{}".format(result))

    

if __name__=='__main__':
    main()
    pass
