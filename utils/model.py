import keras
import tensorflow as tf
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Input, Flatten, SeparableConv2D
from keras.layers import GlobalMaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam, SGD, RMSprop

class XRayModel():

	def __init__(self , model_path):
		self.model_path = model_path

	def build_model(self):
		input_img = Input(shape=(224,224,3), name='ImageInput')
		x = Conv2D(64, (3,3), activation='relu', padding='same', name='Conv1_1')(input_img)
		x = Conv2D(64, (3,3), activation='relu', padding='same', name='Conv1_2')(x)
		x = MaxPooling2D((2,2), name='pool1')(x)
		
		x = SeparableConv2D(128, (3,3), activation='relu', padding='same', name='Conv2_1')(x)
		x = SeparableConv2D(128, (3,3), activation='relu', padding='same', name='Conv2_2')(x)
		x = MaxPooling2D((2,2), name='pool2')(x)
		
		x = SeparableConv2D(256, (3,3), activation='relu', padding='same', name='Conv3_1')(x)
		x = BatchNormalization(name='bn1')(x)
		x = SeparableConv2D(256, (3,3), activation='relu', padding='same', name='Conv3_2')(x)
		x = BatchNormalization(name='bn2')(x)
		x = SeparableConv2D(256, (3,3), activation='relu', padding='same', name='Conv3_3')(x)
		x = MaxPooling2D((2,2), name='pool3')(x)
		
		x = SeparableConv2D(512, (3,3), activation='relu', padding='same', name='Conv4_1')(x)
		x = BatchNormalization(name='bn3')(x)
		x = SeparableConv2D(512, (3,3), activation='relu', padding='same', name='Conv4_2')(x)
		x = BatchNormalization(name='bn4')(x)
		x = SeparableConv2D(512, (3,3), activation='relu', padding='same', name='Conv4_3')(x)
		x = MaxPooling2D((2,2), name='pool4')(x)
		
		x = Flatten(name='flatten')(x)
		x = Dense(1024, activation='relu', name='fc1')(x)
		x = Dropout(0.7, name='dropout1')(x)
		x = Dense(512, activation='relu', name='fc2')(x)
		x = Dropout(0.5, name='dropout2')(x)
		x = Dense(2, activation='softmax', name='fc3')(x)
		
		model = Model(inputs=input_img, outputs=x)
		return model

	def load_model(self , model_path=None):
		if model_path==None:
			model_path = self.model_path

		self.model = self.build_model()
		try:
			self.model.load_weights(model_path)
		except:
			print("Model weights not found")	
		#TODO code for loading the model from .h5 file		
		