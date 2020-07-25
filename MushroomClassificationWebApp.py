#export PATH="$HOME/.local/bin:$PATH"

import streamlit as st
import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score

#importing local modules
import user_inputs as ui
import SVC as svm
import LogisticRrgression as lr
import RandomForestClassifier as rf


def main():
    #Front view of the main page and sidebar
    st.markdown("""<h1 align="center" style="color:Brown;">
            🍄 Mushroom Classification Web App 🍄</h1>""", 
            unsafe_allow_html=True)
    st.sidebar.markdown("""<h1 align="center" style="color:Brown;">
                    🍄 Mushroom Classification Web App 🍄</h1>""", 
                    unsafe_allow_html=True)
    st.image('Decorator/front.jpeg', use_column_width=True)
    st.sidebar.image('Decorator/front.jpeg', use_column_width=True)
    #st.title('Mushroom Classification Web App')
    #st.sidebar.title('Mushroom Classification Web App')
    st.subheader('Want to know your mushrooms are edible or poisonous? ')
    st.sidebar.subheader('Want to know your mushrooms are edible or poisonous? ')
    
    
    @st.cache(persist = True)
    def load_data():
        data = pd.read_csv('Datasets/agaricus-lepiota.data')
        label = LabelEncoder()
        for col in data.columns:
            data[col] = label.fit_transform(data[col])
        return data

    @st.cache(persist = True)
    def split(df):
        y = df.type
        X = df.drop(columns=['type'])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=0)
        return X_train, X_test, y_train, y_test
        
    def plot_metrics(metrics_list, model):
        if 'Confusion Matrix' in metrics_list:
            st.subheader('Confusion Metrix')
            plot_confusion_matrix(model, X_test, y_test, display_labels=class_names)
            st.pyplot()
        
        if 'ROC Curve' in metrics_list:
            st.subheader('ROC Curve')
            plot_roc_curve(model, X_test, y_test)
            st.pyplot()

        if 'Precision-Recall Curve' in metrics_list:
            st.subheader('Precision-Recall Curve')
            plot_precision_recall_curve(model, X_test, y_test)
            st.pyplot()

    def result(y_pred):
        if y_pred == 0:
            st.markdown("""<h3 align="center" style="color:Green;">Result: The Murshroom is <b><u>Edible</u></b>.</h3>""", unsafe_allow_html=True)
            #st.markdown('Result: The Murshroom is **_edible_**.')

        if y_pred == 1:
            st.markdown("""<h3 align="center" style="color:Red;">Result: The Murshroom is <b><u>Poisonous</u></b>.</h3>""", unsafe_allow_html=True)
            #st.markdown('Result: The Murshroom is **_poisonous_**.')



 
                        


    st.subheader('Choose Mode')
    mode = st.selectbox('Mode: ', 
                       [0,1,2], 
                       index=0, 
                       format_func=lambda x:['Select','See Analysis of training Dataset','Evaluate Your Murshroom'][x])


    st.sidebar.subheader('Choose Classifier')
    classifier = st.sidebar.selectbox('Classifier', ('Support Vector Machine (SVM)', 'Logistic Regression', 'Random Forest'))
    

    if mode == 0:
        st.warning('Please Choose an Option.')


    elif mode == 2:
        st.markdown('Please Choose Parameters from Sidebar and Click Proceed.')   
        df = load_data()
        y = df.type
        X = df.drop(columns=['type'])
        X_test = ui.inputs()
        try:
            if classifier == 'Support Vector Machine (SVM)':
                if st.sidebar.button('Proceed', key='proceed'):
                    y_pred = svm.evaluate(X, y, X_test)
                    result(y_pred)

            if classifier == 'Logistic Regression':
                if st.sidebar.button('Proceed', key='proceed'):
                    y_pred = lr.evaluate(X, y, X_test)
                    result(y_pred)

            if classifier == 'Random Forest':
                if st.sidebar.button('Proceed', key='proceed'):
                    y_pred = rf.evaluate(X, y, X_test)
                    result(y_pred)
        except ValueError:
            st.write('')
            st.write('')
            st.write("Sorry I can't proceed with incorrect data!")
            st.write("Please check your inputs.")


    elif mode == 1:
        st.markdown('Please Choose Parameters from Sidebar and Click Proceed.')
        df = load_data()
        X_train, X_test, y_train, y_test = split(df)
        class_names = ['edible', 'poisonous']
        if classifier == 'Support Vector Machine (SVM)':
            svm.analyse(X_train,X_test,y_train,y_test,class_names,plot_metrics)

        if classifier == 'Logistic Regression':
            lr.analyse(X_train,X_test,y_train,y_test,class_names,plot_metrics)

        if classifier == 'Random Forest':
            rf.analyse(X_train,X_test,y_train,y_test,class_names,plot_metrics)


    if st.sidebar.checkbox('Show raw data', False):
        st.subheader('Mushroom Data Set (Classification)')
        st.write(df)



    if mode==0:
        for i in range(1):
            st.sidebar.text(' ')

    st.sidebar.text('©nilotpal')

    #Social connections
    st.sidebar.markdown("""
                    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <center><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
    .fa {
      width: 15px;
      height: 15px;
      display: inline-block;
      padding: 20px;
      font-size: 20px;
      cursor: pointer;
      text-align: center;
      text-decoration: none;  
      border: none;
      border-radius: 50%
    }

    </style>
    </head>
    <body><center>

    <!--<h2>Style Social Media Buttons</h2>-->

    <!-- Add font awesome icons -->


    <!-- <h2>Image Links</h2>

    <p>The image is a link. You can click on it.</p> -->


    <!--
    <a href="https://wa.me/+918159853451" target="_blank">
      <img src="https://cdn0.iconfinder.com/data/icons/tuts/256/whatsapp.png" 
      alt="Whatsapp" style="width:25px;height:25px;border:0">
    </a> -->

    <a href="https://www.facebook.com/nilu.kapri/" target="_blank">
      <img src="https://cdn4.iconfinder.com/data/icons/free-social-media-icons/512/Facebook.png" 
      alt="Facebook" style="width:22px;height:22px;border:0">
    </a>

    <a href="https://instagram.com/Nilotpal__Kapri" target="_blank">
      <img src="https://cdn4.iconfinder.com/data/icons/social-media-2146/512/25_social-256.png" 
      alt="Instagram" style="width:22px;height:22px;border:0">
    </a> 

    <a href="https://m.me/106286494269703" target="_blank">
      <img src="https://cdn3.iconfinder.com/data/icons/social-media-2068/64/_Facebook_Messenger-512.png" 
      alt="Messenger" style="width:22px;height:22px;border:0">
    </a>

    <a href="https://twitter.com/nilotpalkapri" target="_blank">
      <img src="https://cdn3.iconfinder.com/data/icons/social-media-2068/64/_Twitter-256.png" 
      alt="Twitter" style="width:23px;height:23px;border:0">
    </a>

    <a href="https://www.youtube.com/channel/UCe_4uLTNbOvhJGHRVqqbHeQ" target="_blank">
      <img src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Youtube_colored_svg-512.png" 
      alt="YouTube" style="width:22px;height:25px;border:0">
    </a>

    <a href="mailto:nilotpal623401@gmail.com" target="_blank">
      <img src="https://cdn2.iconfinder.com/data/icons/once-again/48/Gmail.png" 
      alt="Mail" style="width:25px;height:25px;border:0">
    </a>

    <a href="https://www.linkedin.com/in/nilotpalkapri" target="_blank">
      <img src="https://cdn4.iconfinder.com/data/icons/free-social-media-icons/256/LinkedIn.png" 
      alt="Linkedin" style="width:22px;height:22px;border:0">
    </a>

    <a href="https://github.com/nilotpalkapri/" target="_blank">
      <img src="https://cdn4.iconfinder.com/data/icons/miu-hexagon-shadow-social/60/github-hexagon-shadow-social-media-256.png" 
      alt="Whatsapp" style="width:25px;height:25px;border:0">
    </a>

    <a href="https://independent.academia.edu/nilotpalkapri" target="_blank">
      <img src="https://image.flaticon.com/icons/png/512/25/25645.png" 
      alt="Academia" style="width:22px;height:22px;border:0">
    </a>
    <a href="https://orcid.org/0000-0001-7803-5957" target="_blank">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/ORCID_iD.svg/768px-ORCID_iD.svg.png" 
      alt="Orcid" style="width:23px;height:23px;border:0">
    </a>
    <a href="https://www.mendeley.com/profiles/nilotpal-kapri/" target="_blank">
      <img src="https://www.pinclipart.com/picdir/middle/568-5689345_2048-black-logo-mendeley-kecil-png-clipart.png" 
      alt="Mendeley" style="width:22px;height:21px;border:0">
    </a>

    <!-- <p>We have added "border:0" to prevent IE9 (and earlier) from displaying a border around the image.</p> </p> -->


     </center>     
    </body>
    </html>

                    """, unsafe_allow_html=True
                    )

if __name__ == '__main__':
    main()
