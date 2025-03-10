# TFFS

Feature selection based on top frequency
## Installation

```bash
pip install tffs
```
## 🔥 Functionality

The library provides a feature selection function using **Random Forest**:

### 🏷 Function:
```python
get_frequency_of_feature_by_percent(df, number_of_runs, percent, n_estimators)
```
## 📌 Parameters

The function `get_frequency_of_feature_by_percent()` accepts the following parameters:

| Parameter          | Type               | Description |
|--------------------|--------------------|-------------|
| **`df`**          | `pandas.DataFrame`  | The input dataset containing features and target variables. |
| **`number_of_runs`** | `int`             | The number of times a Random Forest model is built to compute feature importance. |
| **`percent`**     | `float`             | The percentage of top important features to retain (e.g., `percent=20` keeps the top 20% most important features). |
| **`n_estimators`** | `int`              | The number of decision trees in the Random Forest model. |

## 📤 Return

The function returns:

- A **NumPy array** containing the **indices** of the selected features that are among the top `percent%` most important features across multiple Random Forest runs.

### 🔄 Example Return:
```python
array([0, 2, 4, 7, 9])