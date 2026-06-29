import os
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt
import json
import time

# Suppress warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# ==================== CONFIGURATION ====================
DATASET_PATH = 'dataset'
IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 25
MODEL_SAVE_PATH = 'model_waste.h5'

print("=" * 60)
print("🌿 AI Waste Classification - Training")
print("=" * 60)

# ==================== STEP 1: LOAD DATA ====================
print("\n📂 Step 1: Loading Dataset...")

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    validation_split=0.15
)

train_generator = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

validation_generator = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation',
    shuffle=False
)

# Get actual number of classes from dataset
num_classes = len(train_generator.class_indices)
print(f"✅ Training images: {train_generator.samples}")
print(f"✅ Validation images: {validation_generator.samples}")
print(f"✅ Number of classes: {num_classes}")
print(f"✅ Class names: {list(train_generator.class_indices.keys())}")

# ==================== STEP 2: BUILD MODEL ====================
print("\n🧠 Step 2: Building AI Model...")

base_model = MobileNetV2(
    input_shape=(IMG_SIZE, IMG_SIZE, 3),
    include_top=False,
    weights='imagenet',
    pooling='avg'
)

base_model.trainable = False

model = keras.Sequential([
    base_model,
    layers.Dropout(0.3),
    layers.Dense(256, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    layers.Dense(num_classes, activation='softmax')
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("✅ Model built successfully!")
model.summary()

# ==================== STEP 3: CALLBACKS ====================
print("\n⚙️ Step 3: Setting up training callbacks...")

callbacks = [
    keras.callbacks.EarlyStopping(
        patience=8,
        restore_best_weights=True,
        monitor='val_accuracy',
        mode='max'
    ),
    keras.callbacks.ModelCheckpoint(
        MODEL_SAVE_PATH,
        save_best_only=True,
        monitor='val_accuracy',
        mode='max'
    )
]

# ==================== STEP 4: TRAIN THE MODEL ====================
print("\n🚀 Step 4: Training the Model...")
start_time = time.time()

history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=EPOCHS,
    callbacks=callbacks,
    verbose=1
)

end_time = time.time()
print(f"⏱️ Training completed in: {end_time - start_time:.2f} seconds")

# ==================== STEP 5: SAVE MODEL & METADATA ====================
print("\n💾 Step 5: Saving Model and Metadata...")

model.save(MODEL_SAVE_PATH)
print(f"✅ Model saved as: {MODEL_SAVE_PATH}")

# Save class names mapping
class_indices = train_generator.class_indices
class_indices = {v: k for k, v in class_indices.items()}

with open('class_names.json', 'w') as f:
    json.dump(class_indices, f, indent=2)
print("✅ Class names saved to: class_names.json")

# ==================== STEP 6: PLOT RESULTS ====================
print("\n📊 Step 6: Plotting Training Results...")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('training_results.png', dpi=150)
plt.show()

# ==================== STEP 7: FINAL SUMMARY ====================
print("\n" + "=" * 60)
print("🎉 TRAINING COMPLETE!")
print("=" * 60)
print(f"📁 Final Model: {MODEL_SAVE_PATH}")
print(f"📁 Class Names: class_names.json")
print(f"📊 Training Results: training_results.png")
print(f"📈 Final Validation Accuracy: {history.history['val_accuracy'][-1]:.4f}")
print("=" * 60)