"""
Serving input function definition.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import tensorflow as tf

def serving_input_fn():
    "Return InputFnOps for use with TensorFlow Serving."
    # TODO: fill in features:
    # feature_placeholders = {
    #     'image': tf.placeholder(shape=[32, 128, 128, 3], dtype=tf.uint8)
    # }
    feature_placeholders = {}
    features = {
        key: tf.expand_dims(tensor, axis=-1)
        for key, tensor in feature_placeholders.items()
    }
    input_fn_ops = tf.contrib.learn.InputFnOps(
        features=features,
        labels=None,
        default_inputs=features)
    return input_fn_ops
