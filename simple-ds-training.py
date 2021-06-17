import tensorflow as tf
import os
global_batch_size = 2

print(os.getenv("TF_CONFIG"))
# Passing the devices is optional.
strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
# Create a dataset
dataset = tf.data.Dataset.range(4).batch(global_batch_size)
# Distribute that dataset
dist_dataset = strategy.experimental_distribute_dataset(dataset)
@tf.function
def replica_fn(input):
  return input*2
result = []
# Iterate over the `tf.distribute.DistributedDataset`
for x in dist_dataset:
  # process dataset elements
  result.append(strategy.run(replica_fn, args=(x,)))
print(result)
