from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import tensorflow as tf

def get_outputs(inputs, params, mode):
    "Return the outputs from the model which will be used in the loss function."
    # TODO: define outputs, typically the pre-activation outputs (logits) of neural network model
    outputs = None
    return outputs

def get_predictions(outputs):
    "Return the actual predictions for use with evaluation metrics or TF Serving."
    # TODO: define predictions, e.g. tf.argmax(outputs, axis=-1)
    predictions = None
    return predictions

def get_loss(outputs, labels, params, mode):
    "Return the loss function which will be used with an optimizer."

    loss = None
    if mode == tf.contrib.learn.ModeKeys.INFER:
        return loss

    # TODO: define loss, e.g. tf.losses.sparse_softmax_cross_entropy
    return loss

def get_train_op(loss, params, mode):
    "Return the trainining operation which will be used to train the model."

    train_op = None
    if mode != tf.contrib.learn.ModeKeys.TRAIN:
        return train_op

    global_step = tf.contrib.framework.get_or_create_global_step()

    learning_rate = params['learning_rate']

    train_op = optimize_loss(
        loss=loss,
        global_step=global_step,
        learning_rate=learning_rate,
        optimizer='Adam',
        gradient_noise_scale=None,
        gradient_multipliers=None,
        clip_gradients=None,
        learning_rate_decay_fn=None,
        name=None)

    return train_op

def model_fn(inputs, labels, params, mode):
    "Return ModelFnOps for use with Estimator."

    outputs = get_outputs(inputs, params, mode)
    predictions = get_predictions(outputs)
    loss = get_loss(outputs, labels, params, mode)
    train_op = get_train_op(loss, params, mode)

    return tf.contrib.learn.ModelFnOps(
        predictions=predictions,
        loss=loss,
        train_op=train_op)
