"""
Main training procedure.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import tensorflow as tf

from {{project_name}}.inputs import generate_input_fn
from {{project_name}}.serving import serving_input_fn
from {{project_name}}.feature_engineering import feature_engineering_fn
from {{project_name}}.model import model_fn

def generate_experiment_fn(train_files, eval_files, train_batch_size, eval_batch_size,
                           num_epochs, train_steps, eval_steps):
    "Return _experiment_fn for use with learn_runner."
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

        # TODO: define hyperparameters, e.g. learning_rate
        params = {}

        estimator = tf.contrib.learn.Estimator(
            model_fn=model_fn,
            model_dir=model_dir,
            config=run_config,
            params=params,
            feature_engineering_fn=feature_engineering_fn)

        export_strategy = tf.contrib.learn.make_export_strategy(
            serving_input_fn=serving_input_fn)

        experiment = tf.contrib.learn.Experiment(
            estimator=estimator,
            train_input_fn=train_input_fn,
            eval_input_fn=eval_input_fn,
            export_strategies=[export_strategy])
    return _experiment_fn

def main():
    "Entrypoint for training."
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--train-files',
        help='Train files',
        nargs='+',
        required=True)
    parser.add_argument(
        '--eval-files',
        help='Evaluation files',
        nargs='+',
        required=True)
    parser.add_argument(
        '--num-epochs',
        help='Maximum number of epochs on which to train',
        default=1,
        type=int)
    parser.add_argument(
        '--train-batch-size',
        help='Batch size for training steps',
        type=int,
        default=32)
    parser.add_argument(
        '--eval-batch-size',
        help='Batch size for evaluation steps',
        type=int,
        default=32)
    parser.add_argument(
        '--train-steps',
        help='Number of steps to run training',
        type=int)
    parser.add_argument(
        '--eval-steps',
        help='Number of steps to run evaluation at each checkpoint',
        type=int)

    tf.logging.set_verbosity(tf.logging.INFO)

    experiment_fn = generate_experiment_fn(
        train_files=args.train_files,
        eval_files=args.eval_files,
        train_batch_size=train_batch_size,
        eval_batch_size=eval_batch_size,
        num_epochs=args.num_epochs,
        train_steps=args.train_steps,
        eval_steps=args.eval_steps)
    tf.contrib.learn.learn_runner.run(experiment_fn, job_dir)

if __name__ == '__main__':
    main()
