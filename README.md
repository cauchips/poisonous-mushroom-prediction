# Mushroom Poisonous or Edible Prediction

This repository contains a data science project aimed at predicting whether a mushroom is **poisonous** or **edible** based on its physical characteristics. The project follows the CRISP-DM methodology (Cross Industry Standard Process for Data Mining) and was primarily developed using Python and Streamlit for deployment.

The application is deployed at: [mushroom-prediction.streamlit.app](https://mushroom-prediction.streamlit.app)

## Project Overview

Mushrooms are diverse, and while some are safe to consume, others can be dangerous. This project uses a machine learning model trained on mushroom data to predict the likelihood of a mushroom being poisonous or edible based on 22 categorical features such as:

- Cap shape, cap surface, cap color
- Gill attachment, gill spacing, gill size, gill color
- Stalk shape, stalk surface, stalk color
- Odor, bruises, habitat, etc.

### Goal

The primary goal of this project is to classify mushrooms as either **poisonous** or **edible** based on a set of visual and morphological features provided by the user.

## How to Use the App

The project includes a web application built using [Streamlit](https://streamlit.io/), allowing users to input mushroom characteristics and get real-time predictions on whether the mushroom is poisonous or edible.

You can access the deployed app here: [mushroom-prediction.streamlit.app](https://mushroom-prediction.streamlit.app)

### Steps to Run Locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/mushroom-prediction.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. Enter the mushroom's physical characteristics in the web interface, and the model will predict whether the mushroom is poisonous or edible.

## Files in This Repository

- `scripts.ipynb`: Contains the data preprocessing, feature engineering, model training, and evaluation steps. This notebook explains the CRISP-DM process followed in the project.
- `model.pkl`: The trained machine learning model, serialized for use in the web application.
- `app.py`: The Streamlit web application script where users can input features and receive predictions.
- `requirements.txt`: List of dependencies needed to run the project.
- `README.md`: Project overview and instructions (this file).

## Dataset

The dataset used in this project is the **Mushroom Classification Dataset** from [Kaggle](https://www.kaggle.com/datasets/uciml/mushroom-classification/data?select=mushrooms.csv). It contains 22 categorical features and labels indicating whether the mushroom is poisonous or edible.

## Machine Learning Model

A Random Forest classifier was trained on the dataset after applying label encoding to the categorical features. The model was evaluated and tuned to provide accurate predictions. The details of the model training process can be found in the `scripts.ipynb` notebook.

## Future Work

- Add more feature engineering to improve the model’s performance.
- Allow users to upload datasets for batch predictions.
- Add additional models and compare their performance.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This project was developed by [Your Name](https://github.com/cauchips).
