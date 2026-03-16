"""
Lab 2 — Learner Test File

Write your own pytest tests here. You must implement at least 3 test functions:
  - test_load_data_returns_dataframe
  - test_clean_data_no_nulls
  - test_add_features_creates_revenue

The autograder will run your tests as part of the CI check.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import numpy as np
import pytest  
from pipeline import load_data, clean_data, add_features


# ─── Test 1 ───────────────────────────────────────────────────────────────────

def test_load_data_returns_dataframe():
    """load_data should return a DataFrame with expected columns and rows."""
    df = load_data('data/sales_records.csv')
    assert isinstance (df, pd.DataFrame), "load_data should return a pandas DataFrame"    
    assert len(df) > 0, "DataFrame should not be empty"
    assert all(col in df.columns for col in ['date', 'store_id', 'product_category', 'quantity', 'unit_price', 'payment_method']), "DataFrame is missing expected columns"
   
    pass


# ─── Test 2 ───────────────────────────────────────────────────────────────────

def test_clean_data_no_nulls():
    """After clean_data, quantity and unit_price should have no NaN values."""
    df = load_data('data/sales_records.csv')
    cleaned = clean_data(df)
    assert cleaned['unit_price'].isnull().sum() == 0, "unit_price should have no null values after cleaning"
    pass


# ─── Test 3 ───────────────────────────────────────────────────────────────────

def test_add_features_creates_revenue():
    """add_features should add a 'revenue' column equal to quantity * unit_price."""
    df = load_data('data/sales_records.csv')
    df = clean_data(df)
    df = add_features(df)
    assert 'revenue' in df.columns, "add_features should add a 'revenue' column"
    expected_revenue = df['quantity'] * df['unit_price']
    pd.testing.assert_series_equal(df['revenue'], expected_revenue, check_names=False, check_dtype=False, check_exact=False, rtol=1e-5, atol=1e-8)

    pass
