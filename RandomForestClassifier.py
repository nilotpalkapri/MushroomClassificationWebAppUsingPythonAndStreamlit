import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score


def evaluate(X, y, X_test):
    st.subheader('Evaluting Data with Random Forest')
    model = RandomForestClassifier(n_estimators = 200, max_depth=15, bootstrap=True, n_jobs=-1)
    model.fit(X, y)
    return model.predict(X_test)


def analyse(X_train, X_test, y_train, y_test, class_names, plot_metrics):
    st.sidebar.subheader('Model Hyperparameters')
    n_estimators = st.sidebar.number_input('The number of trees in the forest', 100, 5000, step=10, key='n_estimators')
    max_depth = st.sidebar.number_input('The maximum depth of the tree', 1, 20, step=1, key='max_depth')
    bootstrap = st.sidebar.radio('Bootstrap samples when building trees', ('True', 'False'), key='bootstrap')


    metrics = st.sidebar.multiselect('What metrics to plot?', 
                                    ('Select All', 'Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'), default=['Select All'])
    if 'Select All' in metrics:
        metrics = ['Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve']
            
            
    if st.sidebar.button('Classify', key='classify'):
        st.subheader('Random Forest Result')
        model = RandomForestClassifier(n_estimators = n_estimators, max_depth=max_depth, bootstrap=bootstrap, n_jobs=-1)
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)
        y_pred = model.predict(X_test)
        st.write('Accuracy: ', accuracy.round(2))
        st.write('Precision: ', precision_score(y_test, y_pred, labels=class_names).round(2))
        st.write('Recall: ', recall_score(y_test, y_pred, labels=class_names).round(2))
        plot_metrics(metrics,model)


