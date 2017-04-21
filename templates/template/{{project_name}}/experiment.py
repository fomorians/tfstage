from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import tensorflow as tf

from {{project_name}}.inputs import generate_input_fn
from {{project_name}}.serve import generate_serving_input_fn
from {{project_name}}.augment import generate_feature_engineering_fn
from {{project_name}}.model import model_fn

def generate_experiment_fn(train_files, eval_files, train_batch_size, eval_batch_size,
                           num_epochs, train_steps, eval_steps):
    "Define and return `_experiment_fn` for use with `learn_runner.run`."
    def _experiment_fn(model_dir):
        train_input_fn = generate_input_fn(
            filenames=train_files,
            batch_size=train_batch_size,
            num_epochs=num_epochs,
            shuffle=True)

        eval_input_fn = generate_input_fn(
            filenames=eval_files,
            batch_size=eval_batch_size,
            num_epochs=1,
            shuffle=False)

        run_config = tf.contrib.learn.RunConfig()

        # TODO: define hyperparameters, e.g. learning rate
        params = {}

        feature_engineering_fn = generate_feature_engineering_fn()
        estimator = tf.contrib.learn.Estimator(
            model_dir=model_dir,
            model_fn=model_fn,
            config=run_config,
            params=params,
            feature_engineering_fn=feature_engineering_fn)

        # TODO: define evaluation metrics, e.g. accuracy
        eval_metrics = {}

        serving_input_fn = generate_serving_input_fn()
        export_strategy = tf.contrib.learn.make_export_strategy(
            serving_input_fn=serving_input_fn,
            exports_to_keep=1)

        experiment = tf.contrib.learn.Experiment(
            estimator=estimator,
            train_input_fn=train_input_fn,
            eval_input_fn=eval_input_fn,
            export_strategies=[export_strategy],
            train_steps=train_steps,
            eval_steps=eval_steps)
        return experiment

    return _experiment_fn
