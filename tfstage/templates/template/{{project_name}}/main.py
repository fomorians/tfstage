"""
Main training and prediction task.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import sys
import random
import argparse
import numpy as np
import tensorflow as tf

from tensorflow.contrib.learn.python.learn import learn_runner

from {{project_name}}.experiment import generate_experiment_fn

def main():
    """
    Main entrypoint for the training and prediction. Defines command-line
    arguments and sets up [`learn_runner`](https://goo.gl/I6TwxA).
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--data-dir',
        help='Location for data')
    parser.add_argument(
        '--job-dir',
        help='Location to write checkpoints, summaries, and export models',
        required=True)
    parser.add_argument(
        '--num-epochs',
        help='Maximum number of epochs on which to train',
        type=int,
        default=1000)
    parser.add_argument(
        '--batch-size',
        help='Batch size for steps',
        type=int,
        default=32)
    parser.add_argument(
        '--seed',
        help='Random seed',
        type=int,
        default=random.randint(0, 2**32))

    args = parser.parse_args()

    # NOTE: set random seed if specified
    if args.seed is not None:
        random.seed(args.seed)
        np.random.seed(args.seed)

    tf.logging.set_verbosity(tf.logging.INFO)

    experiment_fn = generate_experiment_fn(
        data_dir=args.data_dir,
        batch_size=args.batch_size,
        num_epochs=args.num_epochs,
        seed=args.seed)

    learn_runner.run(experiment_fn, args.job_dir)

if __name__ == '__main__':
    main()
