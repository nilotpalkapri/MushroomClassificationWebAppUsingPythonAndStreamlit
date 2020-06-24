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
    st.title('Mushroom Classification Web App')
    st.sidebar.title('Mushroom Classification Web App')
    st.markdown('Are  your mushrooms edible or poisonous? 🍄')
    st.sidebar.markdown('Are  your mushrooms edible or poisonous? 🍄')
    
    @st.cache(persist = True)
    def load_data():
        data = pd.read_csv('/home/nilotpalkapri/Desktop/Project/agaricus-lepiota.data')
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
            st.markdown('Result: The Murshroom is **_edible_**.')
        if y_pred == 1:
            st.markdown('Result: The Murshroom is **_poisonous_**.')






    st.sidebar.subheader('Choose Mode')
    mode = st.sidebar.selectbox('Mode', ('See Analysis of training Dataset', 'Evaluate Your Data'))

    st.sidebar.subheader('Choose Classifier')
    classifier = st.sidebar.selectbox('Classifier', ('Support Vector Machine (SVM)', 'Logistic Regression', 'Random Forest'))


    if mode == 'Evaluate Your Data':   
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


    if mode == 'See Analysis of training Dataset':
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


if __name__ == '__main__':
    main()
