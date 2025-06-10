# Import necessary libraries
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt

# 1. Load and preprocess the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values to [0, 1]
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Reshape images for 1D CNN: (samples, 784, 1)
# Original shape: (samples, 28, 28) -> Flatten to (samples, 784, 1)
x_train = x_train.reshape(-1, 28 * 28, 1)
x_test = x_test.reshape(-1, 28 * 28, 1)

# Convert labels to one-hot encoded format (e.g., 3 -> [0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Print shapes to confirm
print(f"Training data shape: {x_train.shape}")  # (60000, 784, 1)
print(f"Test data shape: {x_test.shape}")      # (10000, 784, 1)

# 2. Build the 1D CNN model
model = models.Sequential([
    # Conv1D layer: 32 filters, kernel size 3, ReLU activation
    # Input shape: (784, 1) -> applies filters to the 784-length sequence
    layers.Conv1D(filters=32, kernel_size=3, activation='relu', input_shape=(784, 1)),
    # MaxPooling1D: Reduces sequence length by taking max over windows of size 2
    layers.MaxPooling1D(pool_size=2),
    
    # Second Conv1D layer: 64 filters, kernel size 3
    layers.Conv1D(filters=64, kernel_size=3, activation='relu'),
    layers.MaxPooling1D(pool_size=2),
    
    # Flatten the output for dense layers
    layers.Flatten(),
    
    # Dense layer with 128 units
    layers.Dense(128, activation='relu'),
    # Dropout to prevent overfitting
    layers.Dropout(0.5),
    # Output layer: 10 units (one per digit), softmax for classification
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Print model summary to see the architecture
model.summary()

# 3. Train the model
history = model.fit(x_train, y_train,
                    epochs=10,
                    batch_size=128,
                    validation_split=0.2)  # Use 20% of training data for validation

# 4. Evaluate the model on test data
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"\nTest accuracy: {test_accuracy:.4f}")

# 5. Visualize training history (accuracy and loss)
plt.figure(figsize=(12, 4))

# Plot accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

# Plot loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.show()

# 6. Visualize some predictions
predictions = model.predict(x_test[:5])
for i in range(5):
    plt.figure(figsize=(2, 2))
    # Reshape back to 28x28 for visualization
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Pred: {np.argmax(predictions[i])}, True: {np.argmax(y_test[i])}")
    plt.axis('off')
    plt.show()