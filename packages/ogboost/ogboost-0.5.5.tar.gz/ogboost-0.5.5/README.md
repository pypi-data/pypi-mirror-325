# Ordinal Gradient Boosting (`OGBoost`)

## Overview

`OGBoost` is a scikit-learn-compatible, Python package for gradient boosting tailored to ordinal regression problems. It does so by alternating between:
1. Fitting a Machine Learning (ML) regression model - such as a decision tree - to predict a latent score that specifies the mean of a probability density function (PDF), and 
1. Fitting a set of thresholds that generate discrete outcomes from the PDF.

In other words, `OGBoost` implements coordinate-descent optimization that combines functional gradient descent - for updating the regression function - with ordinary gradient descent - for updating the threshold vector.

The main class of the package, `GradientBoostingOrdinal`, is designed to have the same look and feel as `scikit-learn`'s `GradientBoostingClassifier`. It includes many of the same features such as custom link functions, sample weighting, early stopping using a validation set, and staged predictions.

There are, however, important differences as well.

## Unique Features of `OGBoost`

### Latent-Score Prediction

The `decision_function` method of the `GradientBoostingOrdinal` behaves differently from `scikit-learn`'s classifiers. Assuming the target variable has `K` distinct classes, a nominal classifier's decision function would return `K` values for each sample. On the other hand, `decision_function` in `ogboost` would return the latent score for each sample, which is a single value. This latent score can be considered a high-resolution alternative to class labels, and thus may have superior ranking performance.

### Early Stopping using Cross-Validation (CV)

In addition to using a single validation set for early stopping, similar to `GradientBoostingClassifier`, `ogboost` early stopping using CV, which means error/performance over the entire data is used for calculating out-of-sample performance. This can improve the robustness of the early-stopping strategy, especially for small and/or imbalanced datasets.

### Heterogeneous Ensemble

While most gradient-boosting software packages exclusively use decision trees with a predetermined set of hyperparameters as the base learner in all boosting iterations, `ogboost` offers significantly more flexibility.

1. Users can pass in a `base_learner` parameter to the class initializer to override the default choice of a `DecisionTreeRegressor`. This can be any regression algorithm such as a feed-forward neural network (`MLPRegressor`), or a K-nearest-neighbor regressor (`KNeighborsRegressor`), etc.
1. Rather than a single base learner, users can specify a list of base learners, which will be drawn from in that order in each boosting iteration. This amounts to creating a *heterogeneous* ensemble as opposed to a *homogeneous* ensemble.

## Installation
```bash
pip install ogboost
```

## Quick Start
### Load the Wine Quality Dataset
The package includes a utility to load the wine quality dataset (red and white) from the UCI repository. Note that `load_wine_quality` shifts the target variable (`quality`) to start from `0`. (This is required by the `GradientBoostingOrdinal` class.)

```python
from ogboost import load_wine_quality
red_wine, white_wine = load_wine_quality()
X, y = red_wine.drop(columns="quality"), red_wine["quality"]
```

### Training, Prediction and Evaluation
```python
from ogboost import GradientBoostingOrdinal

## training ##
model = GradientBoostingOrdinal(n_estimators=100, link_function='logit', verbose=1)
model.fit(X, y)

## prediction ##
# class labels
predicted_labels = model.predict(X)
# class probabilities
predicted_probabilities = model.predict_proba(X)
# latent score
predicted_latent = model.decision_function(X)

# evaluation
concordance_latent = model.score(X, y) # concordance using latent scores
concordance_label = model.score(X, y, pred_type = 'labels') # concordance using class labels
print(f"Concordance - class labels: {concordance_label:.3f}")
print(f"Concordance - latent scores: {concordance_latent:.3f}")
```

### Early-Stopping using Cross-Validation

```python
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
import time

n_splits = 10
n_repeats = 10
kf = RepeatedKFold(n_splits=n_splits, n_repeats=n_repeats)

# early-stopping using a simple holdout set
model_earlystop_simple = GradientBoostingOrdinal(n_iter_no_change=10, validation_fraction=0.2)
start = time.time()
c_index_simple = cross_val_score(model_earlystop_simple, X, y, cv=kf, n_jobs=-1)
end = time.time()
print(f'Simple early stopping: {c_index_simple.mean():.3f} ({end - start:.1f} seconds)')

# early-stopping using cross-validation
model_earlystop_cv = GradientBoostingOrdinal(n_iter_no_change=10, cv_early_stopping_splits=5)
start = time.time()
c_index_cv = cross_val_score(model_earlystop_cv, X, y, cv=kf, n_jobs=-1)
end = time.time()
print(f'CV early stopping: {c_index_cv.mean():.3f} ({end - start:.1f} seconds)')

# statistical comparison of the two methods
from scipy.stats import ttest_rel
t_stat, p_value = ttest_rel(c_index_simple, c_index_cv)
print(f't-statistic: {t_stat}, p-value: {p_value}')
```

### Heterogeneous Ensemble

Generating a random set of hyperparameter combinations for `DecisionTreeRegressor`:

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor

# Number of samples to generate
n_samples = 10

max_depth_choices = [3, 6, 9, None]
max_depths = np.random.choice(max_depth_choices, size=n_samples, replace=True)
max_leaf_nodes_choices = [10, 20, 30, None]
max_leaf_nodes = np.random.choice(max_leaf_nodes_choices, size=n_samples, replace=True)

params = list(zip(max_depths, max_leaf_nodes))

# Create list of DecisionTreeRegressor models with sampled parameters
models = [
    DecisionTreeRegressor(
        max_depth=max_depth,
        max_leaf_nodes=max_leaf_nodes
    )
    for max_depth, max_leaf_nodes in params
]
```

Quantifying the performance of the heterogeneous ensemble:
```python
learning_rate = 0.1

model_heter = GradientBoostingOrdinal(
    base_learner=models,
    n_estimators=n_samples
)
cv_heter = cross_val_score(model_heter, X, y, cv=kf, n_jobs=-1)
print(f'average cv score of heteogeneous ensemble: {np.mean(cv_heter):.3f}')
```

## License
This package is licensed under the [MIT License](./LICENSE).