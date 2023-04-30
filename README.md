![docker build](https://github.com/nautical-io/nautical/actions/workflows/publish.yaml/badge.svg)


Nautical is an Open Source Machine Learning Model Serving Framework.

1. Supports popular machine learning frameworks like PyTorch and Tensorflow.
2. Supports popular deployment tools for Kubernetes including Helm and Tanka. Think `helm install nautical-stable-diffusion`.
3. Beautiful telemetry with Prometheus Metrics, powered by [Mixins](https://monitoring.mixins.dev/).
4. Provides SDKs in popular languages like Python and Java.

We love building developer tools!

## Running

Check the README's present in individual model folders under `models/` for specific instructions on running each model.

## Lint

To Install lint checkers for python
```
pip install flake8 flake8-black
```

To run python lint
```
flake8
black .
```

Thank you!
