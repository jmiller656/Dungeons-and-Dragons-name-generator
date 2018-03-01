import os
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation, Embedding, TimeDistributed
import numpy as np
import json
import matplotlib.pyplot as plt

def build_model(batch_size,seq_len,vocab_size,emb_size=100,num_layers=1,hidden_size=100,dropout=0.2):
	model = Sequential()
	model.add(Embedding(vocab_size,emb_size,batch_input_shape=(batch_size,seq_len)))
	for i in range(num_layers):
		model.add(LSTM(hidden_size,return_sequences=True,stateful=True))
		model.add(Dropout(dropout))
	model.add(TimeDistributed(Dense(vocab_size)))
	model.add(Activation('softmax'))
	return model

def save_weights(epoch,model):
	model.save_weights("weights.{}.h5".format(epoch))

def read_batches(T,vocab_size,batch_size,seq_len):
	length = T.shape[0]
	batch_chars = length / batch_size
	for start in range(0, batch_chars - seq_len, seq_len):
		X = np.zeros((batch_size, seq_len))
		Y = np.zeros((batch_size, seq_len, vocab_size))
		for batch_idx in range(0, batch_size):
			for i in range(0, seq_len):
				X[batch_idx, i] = T[batch_chars * batch_idx + start + i]
				Y[batch_idx, i, T[batch_chars * batch_idx + start + i + 1]] = 1
	yield X, Y

def train(text,epochs,save_freq=10,batch_size=1000,seq_len=20):
	char_to_ix = {ch:i for (i,ch) in enumerate(sorted(list(set(text))))}
	#with open("char_to_ix.json",'w') as f:
	#	json.dump(char_to_ix,f)
	
	ix_to_char = {i:ch for (ch,i) in char_to_ix.items()}
	vocab_size = len(char_to_ix)
	print vocab_size
	model = build_model(batch_size,seq_len,vocab_size)
	model.summary()
	model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=['accuracy'])
	
	T = np.asarray([char_to_ix[c] for c in text],dtype=np.int32)
	steps_per_epoch = (len(text)/batch_size-1)/seq_len
	#log = TrainLogger('training_log.csv')
	losses,accs = [],[]
	for epoch in range(epochs):
		print "\nEpoch {}/{}".format(epoch+1,epochs)
		
		for i, (X,Y) in enumerate(read_batches(T,vocab_size,batch_size,seq_len)):
			loss, acc = model.train_on_batch(X,Y)
			print 'Batch {}: loss = {}, acc = {}'.format(i + 1, loss, acc)
			losses.append(loss)
			accs.append(acc)
		
		if (epoch+1)%save_freq ==0:
			save_weights(epoch+1,model)
			print "Saved"
	plt.plot(range(len(accs)),accs)
	plt.show()

text = open("names.txt").read()
train(text,10000,seq_len=15)
