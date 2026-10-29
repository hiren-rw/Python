# QUESTION 3: Unified Machine Learning Model Interface (Polymorphism)

from abc import ABC, abstractmethod


class MLModel(ABC):

    @abstractmethod
    def train(self,data):
        pass

    @abstractmethod
    def predict(self,new_data):
        pass

class LinearRegressionModel(MLModel):
    def train(self, data):
        print(f"Finding the best-fit line using: {data}")
        
    def predict(self, new_data):
        return f"Linear prediction for {new_data}"

class DecisionTreeModel(MLModel):
    def train(self, data):
        print(f"Splitting data into tree nodes using: {data}")
        
    def predict(self, new_data):
        return f"Decision Tree prediction for {new_data}"

# --- Demonstration of Shared Interface ---

l1 = LinearRegressionModel()
d1 = DecisionTreeModel()

# Store them in a list to show they share the same interface
models = [l1, d1]
sample_dataset = "[X_train, y_train]"
test_point = "[X_test]"

print("--- Running models through the same uniform interface ---")
for m in models:
    # We can call .train() and .predict() safely on any model in the list
    print(f"\nEvaluating: {m.__class__.__name__}")
    m.train(sample_dataset)
    result = m.predict(test_point)
    print(f"Result: {result}")