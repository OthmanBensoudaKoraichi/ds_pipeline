### YOU WILL NOT USE THIS FILE BUT IT IS GOOD PRACTICE TO STRUCTURE AND DIVIDE YOUR PROJECT ###

"""
Database utilities.

This module is responsible for:
- connecting to the database
- fetching raw data
- returning pandas DataFrames

NO ML logic should live here.
"""

import os
import pandas as pd


def get_connection():
    """
    Create and return a database connection or client.

    Reads credentials from environment variables (.env).

    Returns
    -------
    connection : object
        A database connection or client (e.g. psycopg2, SQLAlchemy, Supabase).
    """
    pass


def fetch_table(table_name: str) -> pd.DataFrame:
    """
    Fetch a full table from the database.

    Parameters
    ----------
    table_name : str
        Name of the table to fetch.

    Returns
    -------
    df : pd.DataFrame
        Raw table data.
    """
    pass


def fetch_training_data() -> pd.DataFrame:
    """
    Fetch and assemble the dataset used for training.

    This may involve:
    - joining multiple tables
    - filtering rows
    - basic cleaning (NOT feature engineering)

    Returns
    -------
    df : pd.DataFrame
        Raw but usable dataset for exploration and modeling.
    """
    pass
