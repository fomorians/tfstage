"""
Main training task.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import argparse
import tensorflow as tf

from tensorflow.contrib.learn.python.learn import learn_runner

from {{project_name}}.experiment import generate_experiment_fn

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
        '--job-dir',
        help='Location to write checkpoints, summaries, and export models',
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

    args = parser.parse_args()

    tf.logging.set_verbosity(tf.logging.INFO)

    experiment_fn = generate_experiment_fn(
        train_files=args.train_files,
        eval_files=args.eval_files,
        train_batch_size=train_batch_size,
        eval_batch_size=eval_batch_size,
        num_epochs=args.num_epochs,
        train_steps=args.train_steps,
        eval_steps=args.eval_steps)

    tf.contrib.learn.learn_runner.run(experiment_fn, args.job_dir)

if __name__ == '__main__':
    main()
