"""
Feature engineering function generator.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

def generate_feature_engineering_fn():
    """
    Define `_feature_engineering_fn` to use as a `feature_engineering_fn`
    with [`tf.contrib.learn.Estimator`](https://goo.gl/Ez2AgV).
    """

    def _feature_engineering_fn(features, labels):
        """
        Takes features and labels, which are the output of `input_fn`, and returns
        features and labels which will be fed into `model_fn`.
        """
        return features, labels

    return _feature_engineering_fn
