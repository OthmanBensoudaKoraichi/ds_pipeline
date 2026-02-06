### YOU WILL NOT USE THIS FILE BUT IT IS GOOD PRACTICE TO STRUCTURE AND DIVIDE YOUR PROJECT ###


"""
Machine learning logic.

This module is responsible for:
- preparing features
- training models
- saving / loading models
- generating predictions

NO Flask, NO Streamlit, NO database code here.
"""

import pandas as pd


def prepare_features(df: pd.DataFrame):
    """
    Prepare features for modeling.

    This function should:
    - select relevant columns
    - encode categorical variables
    - scale / transform features if needed

    Parameters
    ----------
    df : pd.DataFrame
        Raw input data.

    Returns
    -------
    X : pd.DataFrame or np.ndarray
        Feature matrix.
    y : pd.Series or np.ndarray
        Target variable.
    """
    pass


def train_model(X, y):
    """
    Train a machine learning model.

    Parameters
    ----------
    X : pd.DataFrame or np.ndarray
        Feature matrix.
    y : pd.Series or np.ndarray
        Target variable.

    Returns
    -------
    model : object
        Trained model.
    """
    pass


def save_model(model, path: str):
    """
    Save a trained model to disk.

    Parameters
    ----------
    model : object
        Trained model.
    path : str
        File path where the model should be saved.
    """
    pass


def load_model(path: str):
    """
    Load a trained model from disk.

    Parameters
    ----------
    path : str
        Path to the saved model.

    Returns
    -------
    model : object
        Loaded model.
    """
    pass


def predict(model, X):
    """
    Generate predictions using a trained model.

    Parameters
    ----------
    model : object
        Trained model.
    X : pd.DataFrame or np.ndarray
        Feature matrix.

    Returns
    -------
    predictions : object
        Model predictions in a clean, serializable format.
    """
    pass
