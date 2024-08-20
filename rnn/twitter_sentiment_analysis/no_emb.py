import numpy as np
import pandas as pd
from tensorflow import keras
from keras.layers import Dense, LSTM, Embedding, Dropout, Activation, Input
from keras.models import Model
import matplotlib.pyplot as plt
import csv

def find_vocabulary(data_file, top_words = 10000):
    """
    Find out top top_words words occuring in training set.
    Return index to word, word to index and word to vector mapping of these top_words
    """
    with open(data_file, 'r') as f:
        csvReader = csv.reader(f)

        word_freq = dict()

        for row in csvReader:
            sentence = row[3]
            li = sentence.lower().strip().split()
            for w in li:
                # If there is no alphabet in w, then continue
                if not any(chr.isalpha() for chr in w): continue
                
                if w in word_freq.keys():
                    word_freq[w] += 1
                else: word_freq[w] = 1
    most_freq_words = sorted(word_freq.items(), key = lambda x: x[1], reverse=True)[:top_words]
    most_freq_words = sorted(most_freq_words, key=lambda x:x[0])

    idx_to_word = dict()
    word_to_idx = dict()

    i = 1
    for w, _ in most_freq_words:
        word_to_idx[w] = i
        idx_to_word[i] = w
        i += 1

    word_to_vec_map = dict()
    
    temp_arr = np.zeros((top_words, ))
    for w, idx in word_to_idx.items():
        temp_arr[idx-1] = 1.0
        word_to_vec_map[w] = temp_arr.copy()
        temp_arr[idx-1] = 0.0

    return word_to_vec_map, word_to_idx, idx_to_word

def load_data(label_to_idx, csv_file = 'data/twitter_training.csv'):
    X = []
    y = []
    with open(csv_file, 'r') as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            X.append(row[3])
            y.append(label_to_idx[row[2]])
    X = np.asarray(X)
    y = np.asarray(y, dtype=int)
    return X, y

def sentence_to_indices(X, words_to_idx ,maxLen):
    m = X.shape[0]
    X_out = np.zeros((m, maxLen))
    for i in range(m):
        li = X[i].lower().strip().split()
        j = 0
        for w in li:
            if (j >= maxLen): break
            if w in words_to_idx.keys():
                X_out[i,j] = words_to_idx[w]
            j += 1
    return X_out

def pretrained_embedding_layer(word_to_vec_map, word_to_index):
    """
    Creates a Keras Embedding() layer and loads in pre-trained GloVe 50-dimensional vectors.
    
    Arguments:
    word_to_vec_map -- dictionary mapping words to their GloVe vector representation.
    word_to_index -- dictionary mapping from words to their indices in the vocabulary (400,001 words)

    Returns:
    embedding_layer -- pretrained layer Keras instance
    """
    
    vocab_size = len(word_to_index) + 1              # adding 1 to fit Keras embedding (requirement)
    any_word = list(word_to_vec_map.keys())[0]
    emb_dim = word_to_vec_map[any_word].shape[0]    # define dimensionality of your GloVe word vectors (= 50)
      
    ### START CODE HERE ###
    # Step 1
    # Initialize the embedding matrix as a numpy array of zeros.
    # See instructions above to choose the correct shape.
    emb_matrix = np.zeros((vocab_size, emb_dim))
    
    # Step 2
    # Set each row "idx" of the embedding matrix to be 
    # the word vector representation of the idx'th word of the vocabulary
    for word, idx in word_to_index.items():
        emb_matrix[idx, :] = word_to_vec_map[word]

    # Step 3
    # Define Keras embedding layer with the correct input and output sizes
    # Make it non-trainable.
    embedding_layer = Embedding(input_dim = vocab_size, output_dim = emb_dim, trainable = False)
    ### END CODE HERE ###

    # Step 4 (already done for you; please do not modify)
    # Build the embedding layer, it is required before setting the weights of the embedding layer. 
    embedding_layer.build((None,)) # Do not modify the "None".  This line of code is complete as-is.
    
    # Set the weights of the embedding layer to the embedding matrix. Your layer is now pretrained.
    embedding_layer.set_weights([emb_matrix])
    
    return embedding_layer

def build_model(input_shape, words_to_vec_map, words_to_idx):
    sentence_indices = Input(shape = input_shape)

    embedding_layer = pretrained_embedding_layer(words_to_vec_map, words_to_idx)

    embeddings = embedding_layer(sentence_indices)

    X = LSTM(units=128, return_sequences=True)(embeddings)

    X = Dropout(rate = 0.5)(X)

    X = LSTM(units = 128, return_sequences=False)(X)

    X = Dropout(rate = 0.5)(X)

    X = Dense(units= 1)(X)

    X = Activation('tanh')(X)

    model = Model(inputs = sentence_indices, outputs = X)

    return model

# Load data
df_train = pd.read_csv('data/twitter_training.csv', header=None)
print(">>Done reading data:")
print(df_train.head())

label_to_idx = {'Irrelevant': 0, 'Negative': -1, 'Neutral': 0, 'Positive': 1}

word_to_vec_map, word_to_idx, idx_to_word = find_vocabulary('data/twitter_training.csv', top_words=15000)

print("\n>>Done finding vocabulary")

maxLen = len(max(df_train[3], key=lambda x:len(str(x).strip().split())).strip().split())
print(f"Maximum length of a message is: {maxLen}\n")

X_train, y_train = load_data(label_to_idx, 'data/twitter_training.csv')
X_val, y_val = load_data(label_to_idx, 'data/twitter_validation.csv')

X_train_indices = sentence_to_indices(X_train, word_to_idx, maxLen)
X_val_indices = sentence_to_indices(X_val, word_to_idx, maxLen)

print(">>Done loading data\n")

model = build_model((maxLen, ), word_to_vec_map, word_to_idx)
print(">>Model build completed\n")

model.compile(loss='mean_squared_error', optimizer= 'adam', metrics=['accuracy'])
print(">>Model compilation completed\n")

history = model.fit(X_train_indices, y_train, epochs = 50, batch_size = 32, shuffle=True)

model_save_name = "model_no_emb.h5"
model.save(model_save_name)
print(f">>Done fitting, saved the model '{model_save_name}'\n")

print("Running on validation data:")
model.evaluate(X_val_indices, y_val)