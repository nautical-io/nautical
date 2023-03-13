![docker build](https://github.com/nautical-io/nautical/actions/workflows/ci.yaml/badge.svg)


Nautical is an Open Source Machine Learning Model Serving Framework.

1. Supports popular machine learning frameworks like PyTorch and Tensorflow.
2. Supports popular deployment tools for Kubernetes including Helm and Tanka. Think `helm install nautical-stable-diffusion`.
3. Beautiful telemetry with Prometheus Metrics, powered by [Mixins](https://monitoring.mixins.dev/).
4. Provides SDKs in popular languages like Python and Java.

We love building developer tools!

## Running

To start the server on local machine, run

```
NAUTICAL_MODEL=bert-base-uncased python3 main.py
```