"""
Data input pipeline definition.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import tensorflow as tf

def generate_input_fn(data_dir, batch_size, num_epochs=None, shuffle=False):
    """
    Define `_input_fn` to use with [`tf.contrib.learn.Experiment`](https://goo.gl/ttzJ9M).

    See [Building Input Functions with tf.contrib.learn](https://goo.gl/Thdr6r) for more info.
    """

    def _input_fn():
        # NOTE: always place the input pipeline on the CPU
        with tf.device('/cpu:0'):

            # TODO: define features and labels
            truth_table = tf.constant([
                [0, 0, 0],
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0],
            ], dtype=tf.float32)

            all_inputs = truth_table[..., :2]
            all_labels = truth_table[..., 2:]

            inputs, label = tf.train.slice_input_producer(
                tensor_list=[all_inputs, all_labels],
                num_epochs=num_epochs,
                shuffle=shuffle)

            inputs_batch, labels_batch = tf.train.batch(
                tensors=[inputs, label],
                batch_size=batch_size,
                allow_smaller_final_batch=True)

            # NOTE: must be a dictionary for exporting
            features = {
                'inputs': inputs_batch
            }

            labels = {
                'label': labels_batch
            }

            return features, labels

    return _input_fn
