# neurolab-mongo-python

![image](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```
### Training Pipeline
Training pipelines let you perform custom machine learning (ML) training and automatically create a Model resource based on your training output.
![](https://camo.githubusercontent.com/b13a2584be17b2bb9c65bdaef725aacb18bb66f109fc62c5595ffeac5bab8345/68747470733a2f2f69696c692e696f2f48424938396c322e706e67)

__Data Ingestion:__
Data ingestion is the process of obtaining and importing data for immediate use or storage in a database. To ingest something is to take something in or absorb something. Data can be streamed in real time or ingested in batches. In real-time data ingestion, each data item is imported as the source emits it.

In data ingestion we create three datasets:

1. training dataset
2. testing dataset
3. validation dataset

__Data Validation:__
Data validation refers to the process of ensuring the accuracy and quality of data. It is implemented by building several checks into a system or report to ensure the logical consistency of input and stored data. In automated systems, data is entered with minimal or no human supervision.

__Data Transformation:__
Data transformation is the process of converting data from one format to another, typically from the format of a source system into the required format of a destination system. Data transformation is a component of most data integration and data management tasks, such as data wrangling and data warehousing.

__Model Trainer:__
Model training is the phase in the data science development lifecycle where practitioners try to fit the best combination of weights and bias to a machine learning algorithm to minimize a loss function over the prediction range.

__Model Evaluation:__
Model evaluation is the process of using different evaluation metrics to understand a machine learning model's performance, as well as its strengths and weaknesses. Model evaluation is important to assess the efficacy of a model during initial research phases, and it also plays a role in model monitoring.

__Model Pusher:__
The Pusher component is used to push a validated model to a deployment target during model training or re-training. Before the deployment, Pusher relies on one or more blessings from other validation components to decide whether to push the model or not.

Evaluator blesses the model if the new trained model is "good enough" to be pushed to production.
(Optional but recommended) InfraValidator blesses the model if the model is mechanically servable in a production environment.
A Pusher component consumes a trained model in SavedModel format, and produces the same SavedModel, along with versioning metadata.

> ML pipilenes can be made totally by scratch or some available services/softwares can be used such as:
>* [TFX](https://www.tensorflow.org/tfx)
>* [Apache Spark ML](https://spark.apache.org/docs/1.6.1/ml-guide.html)
>* [Amazon Sagemaker Pipelines](https://aws.amazon.com/sagemaker/pipelines/?tag=mochaglobal20-20)
>* [Azure ML Pipelines](https://learn.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines)

### ML Component:
every stage of the ML pipeline is called a component.

### Artifact:
An artifact is a machine learning term that is used to describe the output created by the training process. Output could be a fully trained model, a model checkpoint, or a file created during the training process. AI Artifacts describe all digital products that are used in an AI Tool. They can be the input, the output, or an intermediate result that is processed by tools. We mainly specify six types of artifacts(corresponding to the steps in the pipeline): Data, Knowledge, Model, Application, Algorithm, and Benchmark.

### ML Entity:
An ML entity is an entity type that is based on a training utterances, similar to the way intents are. For ML entities, these utterances are annotated to show where entity values appear in the utterance.