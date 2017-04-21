"""
Feature engineering function definition.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

def generate_feature_engineering_fn():
    "Return _feature_engineering_fn for use with Estimator."
    def _feature_engineering_fn(inputs, labels):
        "Return inputs and labels after performing any augmentation or feature engineering."
        # TODO: define feature engineering / augmentation
        return inputs, labels
    return _feature_engineering_fn
