To make the most of the state-of-art AI/ML model advancements in the recent
months, Machine Learning Engineers must empower app developers to use these
models as easily as possible. There are several gaps to making this happen at
the moment.

Most modern software development has moved to the cloud native stack containing
kubernetes, containerised applications and microservices. Machine Learning
models continue to lie in Jupyter Notebooks in research mode and teams face
significant hurdles in moving models to the production/scaling stage. At
Nautical, our vision is to ease the deployment and integration of machine
learning models in modern software stacks.

To do this, we must first provide easy deployment options for models on
kubernetes and we plan to provide support for this through Helm and Tanka. Once
users are able to deploy these models on their kubernetes clusters, these models
can be trated like external APIs that the application will interact with. The
next step is to provide SDKs for application developers to interact with these
ML models with ease. Here lies another problem - some models take images as
input, some take time series and others take audio input. Serializing &
deserializing is an unnecessary pain that developers face while writing home
grown SDKs to ineract with models. Finally, ML models can be slow, lack any
telemetry out of the box and require special configuration options for better
performance. To solve for these use cases, Nautical will provide SDKs in popular
languages like Python and Java so app developers can focus on the business parts
of the app rather than worry about model integration.