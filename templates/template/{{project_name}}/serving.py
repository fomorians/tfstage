"""
Serving input function definition.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import tensorflow as tf

def generate_serving_input_fn():
    "Return InputFnOps for use with TensorFlow Serving."
    def _serving_input_fn():
        # TODO: define feature placeholders
        feature_placeholders = {}
        features = {
            key: tf.expand_dims(tensor, axis=-1)
            for key, tensor in feature_placeholders.items()
        }
        input_fn_ops = tf.contrib.learn.InputFnOps(
            features=features,
            labels=None,
            default_inputs=feature_placeholders)
        return input_fn_ops
    return _serving_input_fn
