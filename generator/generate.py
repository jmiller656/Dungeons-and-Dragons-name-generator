import numpy as np
import os
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import sys
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dropout, TimeDistributed, Dense, Activation, Embedding
sys.stderr = stderr
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def build_sample_model(vocab_size,emb_size=100,num_layers=1,hidden_size=100,dropout=0.2):
	model = Sequential()
	model.add(Embedding(vocab_size,emb_size,batch_input_shape=(1,1)))
	for i in range(num_layers):
		model.add(LSTM(hidden_size,return_sequences=(i<num_layers-1),stateful=True))
		model.add(Dropout(dropout))

	model.add(Dense(vocab_size))
	model.add(Activation('softmax'))
	return model

def sample(header, num_chars):
	model = build_sample_model(vocab_size)
	model.load_weights('generator/weights/weights.h5')

	sampled = [char_to_ix[c] for c in header]
	for c in header[:-1]:
		batch = np.zeros((1, 1))
		batch[0, 0] = char_to_ix[c]
		model.predict_on_batch(batch)

	for i in range(num_chars):
		batch = np.zeros((1, 1))
		if sampled:
			batch[0, 0] = sampled[-1]
		else:
			batch[0, 0] = np.random.randint(vocab_size)
		result = model.predict_on_batch(batch).ravel()
		sample = np.random.choice(range(vocab_size), p=result)
		if ix_to_char[sample] == "\n":
			break
		sampled.append(sample)

	return ''.join(ix_to_char[c] for c in sampled)

text = open("generator/names.txt").read()
char_to_ix = {ch:i for (i,ch) in enumerate(sorted(list(set(text))))}
ix_to_char = {i:ch for (ch,i) in char_to_ix.items()}
vocab_size = len(char_to_ix)
