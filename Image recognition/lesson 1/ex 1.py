# Describe in writing why cross entropy performs better as a loss function then mean squared error.

Cross-entropy performs better than mean squared error as a loss function in classification problems because it considers
the probability distribution of the predicted values and penalizes incorrect predictions more heavily.
MSE only measures the difference between the predicted and actual values themselves without considering the probability
distribution, which may not be sensitive to small changes in the predicted probabilities, and treats all errors equally.
However, the choice of loss function ultimately depends on the specific problem and the nature of the target variable.