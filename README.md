# immo-eliza-ml
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![vsCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-333?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-000000?style=for-the-badge&logo=fastapi&logoColor=white)




## 📖 Description
This project is a follow up on the Immoweb ML project in https://github.com/semdeleer/immo-eliza-ml.git.

In this project phase, our primary goal is to deploy a machine learning model that accurately predicts housing prices. We implemented this by establishing a FastAPI application, which was subsequently deployed on Render. Leveraging the Render link, we extended its deployment to a Streamlit website. Additionally, we explored an alternative approach by deploying the machine learning model directly through Streamlit and then encapsulating it within a Dockerfile for deployment.

The input properties required in the Streamlit interface for predicting the price include:


* property_id
* locality_name
* postal_code
* street_name
* house_number
* latitude
* longitude
* property_type (house or apartment)
* property_subtype (bungalow, chalet, mansion, ...)
* price
* type_of_sale (note: exclude life sales)
* number_of_rooms (Number of rooms)
* living_area (Living area (area in m²))
* kitchen_type
* fully_equipped_kitchen (0/1)
* furnished (0/1)
* open_fire (0/1)
* terrace
* terrace_area (area in m² or null if no terrace)
* garden
* garden_area (area in m² or null if no garden)
* surface_of_good
* number_of_facades
* swimming_pool (0/1)
* state_of_building (new, to be renovated, ...)


## 🛠 Installation

* clone the repo
```bash
git git@github.com:semdeleer/immo-eliza-deployment.git
```

* Install all the libraries in requirements.txt
```bash
pip install -r requirements.txt
```

* Run the script
```bash
$ python3 streamlitapi.py
```
* Run the command in terminal
```bash
$ streamlit run c:/Users/semde/BeCodeH/Projects/Project6/immo-eliza-deployment/streamlitt/streamlitapi.py
```
* Enter the criteria of your house.

* Click on the price result button

* You wil get the price result of your house

## 👾 Cleaning steps

Before utilizing the raw data in the machine learning model, it undergoes several preprocessing steps to enhance its quality and suitability for analysis. The following are the sequential cleaning steps employed:

* Replace Outliers: Identify and substitute outliers with appropriate values.

* Drop Columns: Remove irrelevant or redundant columns from the dataset.

* Drop Null Values: Eliminate rows containing missing data.

* Transform Categorical Variables (One-Hot Encoding): Convert categorical variables into numerical format using One-Hot Encoding.

* Transform Label Encoder: Encode categorical variables using LabelEncoder.

* Create X and y: Separate the dataset into feature matrix (X) and target variable (y).

* Replace NaN in Categorical Variables: Replace missing values in categorical variables with suitable representations.

* Change to Integer: Convert data types to integer where appropriate.

* Replace Null Values with Median: Substitute missing numerical values with the median of respective columns.

* Replace Null Values with Minimum minus One: Replace missing numerical values with (minimum value - 1) of respective columns.

* Replace Null Values with Mean: Fill missing numerical values with the mean of respective columns.

* Replace Null Values with Zero: Replace missing numerical values with zero.


## 🤖 Project File structure
```
C:.
│   .dockerignore
│   .gitattributes
│   .gitignore
│   app.py
│   README.md
│   requirements.txt
│   testdata.txt
│
├───predict
│   └───__pycache__
│           predict.cpython-312.pyc
│
├───streamlitt
│     Dockerfile
│     model_pickle_b
│     predict.py
│     requirements.txt
│     steamlit.py
│     streamlitapi.py
```


## 🔍 Contributors
- [Sem Deleersnijder](https://github.com/semdeleer)

## 📜 Timeline

This project was created in 5 days.