# TensorFlow Scaffold Generator

```
$ scaffold my_project
Project created: ./my_project
```

## TODO

- [-] Setup CLI with argparse
- [] Test with Recurrent Entity Networks
- [] Setup deploy with Cloud ML
- [] Setup deploy script with generic interface
- [] Figure out Sacred?
    Create ex in main with add_config using argparse arguments?
    Won't work b/c logging requires wrapping main.
    Want:
    - config saving
    - stdout/stderr capture
    - code capture
    - hooks: Slack / file

## Ideas

- Add flag to enable sample code generation
- Add additional generators for common tasks such as a TFRecords conversion generator

## Environment

```
PROJECT_ID=$(gcloud config list project --format "value(core.project)")
BUCKET_NAME=${PROJECT_ID}-data

JOB_NAME=$JOB_NAME
JOB_DIR=$JOB_DIR
MODULE_NAME=trainer.task
PACKAGE_PATH=trainer/
REGION=us-east1
```

## Training

### Generic

```
deploy [remote|cloud|local] \
  --module-name {{project-name}}.main \
  --package-path . \
  -- \
  --job-dir $JOB_DIR \
  with [args]
```

### Local

```
gcloud ml-engine local train \
    --module-name $MODULE_NAME \
    --package-path $PACKAGE_PATH \
    -- \
    --job-dir $JOB_DIR \
    with [args]
```

### Cloud

```
gcloud ml-engine jobs submit training $JOB_NAME \
  --job-dir $OUTPUT_PATH \
  --runtime-version 1.0 \
  --module-name $MODULE_NAME \
  --package-path $PACKAGE_PATH \
  --region $REGION \
  -- \
  with [args]
```

## References

### Cloud ML Engine

- [Cloud ML Engine Getting Started](https://cloud.google.com/ml-engine/docs/how-tos/getting-started-training-prediction)
- [Cloud ML Engine REST API](https://cloud.google.com/ml-engine/reference/rest/)
- [Cloud ML Engine Trainer Sample](https://github.com/GoogleCloudPlatform/cloudml-samples/tree/master/census/estimator/trainer)

### Python Packaging

- [Python Packaging](http://python-packaging.readthedocs.io/en/latest/index.html): How To Package Your Python Code
- [Python Packaging User Guide](https://packaging.python.org/distributing/): Packaging and Distributing Projects

### Python Scaffolding Examples:

- [https://github.com/Aaronontheweb/scaffold-py](scaffold-py) (includes virtualenvwrapper mkproject)
- [https://github.com/MinweiShen/scaffolding](scaffolding) (uses Django template format)
