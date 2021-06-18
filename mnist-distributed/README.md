# DISTRIBUTED TRAINING MNIST EXAMPLE 

## Create code repo
- Name: distributed-training
- Project source: Git
- Git URL: https://github.com/pallavi-pannu-oc/distributed-training.git
- Branch: main

## Create dataset repo
- Name: mnist
- Dataset source: Other
- URL: https://s3.amazonaws.com/img-datasets/mnist.pkl.gz

## Create a model
- Name: distributed-model
- Keep default for others

## Run training job
 - Runs->+Training Run.
 - Code: distributed-training
 - Framework: Tensorflow
 - Version: 2.0.0-gpu
 - Start-up script: python mnist-distributed/mnist-distributed.py
 - Repos->Inputs->Datasets: select mnist dataset enter mountpath as /mnist
 - Repos->Outputs->Model: select distributed-model and enter mountpath as /model
 - **Allocate GPUS **
 - **Select Distributed workloads : Automatic Distribution**
 - Submit
