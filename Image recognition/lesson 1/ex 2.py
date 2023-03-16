# Describe in writing why dropout allows to reduce overfitting.

Dropout reduces overfitting in neural networks by randomly dropping out a fraction of neurons during training,
which reduces co-adaptation and makes the network more robust to variations in the input data.
This effectively reduces the capacity of the network, making it less likely to overfit the training data.
At test time, the entire network is used, but the activations of the dropped out neurons are scaled down
by the dropout rate.