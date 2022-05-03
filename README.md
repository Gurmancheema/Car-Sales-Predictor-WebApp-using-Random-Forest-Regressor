# Car-Sales-Predictor-using-Random-Forest-Regressor
This is a machine learning based Web App built using Python. The model is trained on a historical dataset of cars based on 8 attributes. Car Sales predictor web app allows the user to predict the reselling price of their car by just entering few common details of their car in the app.
1. The dataset is vehicle data from Kaggle. This dataset is best to practice any regression algorithm as the dataset is small, easy to understand and without any missing values.
2. Data cleansing , visualisation, Feature engineering and Model building is done in jupyter notebook and can be accessed from the .ipynb file in the repository.
3. After model training and tuning the model is saved using pickle library in order to use it in our web app.
4. The web app and the front-end is built using Stream lit framework. The link to the documentation of Stream list is given: https://docs.streamlit.io/
5. In order to run the web app in your machine, install all the libraries used in this project mentioned in "requirements.txt" file and download the "Car_sales_predictor.py" file along with pickle file into the same folder. 
6. Fire up anaconda prompt and type the following command to run the web app in your browser.
                          "streamlit run Car_sales_predictor.py"
