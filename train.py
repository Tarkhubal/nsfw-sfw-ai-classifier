from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# We create a generator of images for the training
train_datagen = ImageDataGenerator(rescale=1./255)

# We put the images in the folder 'dataset' in the folder 'train' with two subfolders 'nsfw' and 'sfw'
train_data = train_datagen.flow_from_directory(
    'train/dataset',
    target_size=(64, 64),  # Images size (64x64) at the enter of the neural network
    batch_size=32,
    class_mode='binary'  # Binary classification (nsfw or sfw)
)

# We create the neural network
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# And we train it
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_data, epochs=5)
model.save('model_nsfw_sfw.h5')
