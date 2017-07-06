"""
Define an experiment responsible for containing all information needed to train a model.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import tensorflow as tf

from {{project_name}}.inputs import generate_input_fn
from {{project_name}}.serve import generate_serving_input_fn
from {{project_name}}.augment import generate_feature_engineering_fn
from {{project_name}}.model import model_fn

def generate_experiment_fn(data_dir, batch_size, num_epochs, seed):
    """
    Define an `_experiment_fn` to use with [`learn_runner.run`](https://goo.gl/I6TwxA).
    """

    # TODO: define hyperparameters
    params = {
        'learning_rate': 1e-2
    }

    def _experiment_fn(output_dir):
        train_input_fn = generate_input_fn(
            data_dir=data_dir,
            batch_size=batch_size,
            num_epochs=num_epochs,
            shuffle=True)

        eval_input_fn = generate_input_fn(
            data_dir=data_dir,
            batch_size=batch_size,
            num_epochs=1,
            shuffle=False)

        feature_engineering_fn = generate_feature_engineering_fn()

        run_config = tf.contrib.learn.RunConfig(
            tf_random_seed=seed)

        estimator = tf.contrib.learn.Estimator(
            model_dir=output_dir,
            model_fn=model_fn,
            config=run_config,
            params=params,
            feature_engineering_fn=feature_engineering_fn)

        # TODO: define evaluation metrics
        eval_metrics = {
            'accuracy': tf.contrib.learn.MetricSpec(
                metric_fn=tf.metrics.accuracy,
                prediction_key='prediction',
                label_key='label')
        }

        serving_input_fn = generate_serving_input_fn()

        export_strategy = tf.contrib.learn.utils.make_export_strategy(
            serving_input_fn=serving_input_fn,
            exports_to_keep=1)

        experiment = tf.contrib.learn.Experiment(
            estimator=estimator,
            train_input_fn=train_input_fn,
            eval_input_fn=eval_input_fn,
            eval_metrics=eval_metrics,
            eval_steps=None,
            export_strategies=[export_strategy])
        return experiment

    return _experiment_fn
