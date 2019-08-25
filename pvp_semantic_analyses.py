import pandas as pd
import numpy as np
from textblob import TextBlob

#### Game Plan

#1 correlate length of memories/adjectives with relationship satisfaction and behav pref indices

#2 see if we can predict labels (parent/friend) from memories/adjectives

#3 run NNMF on data to see what latent topics emerge separately for parents and friends

#4 score each individual on topics according to word embeddings and see whether that predicts prefs

#5 use similarity between word embeddings to create networks (overall/topic focused) and test diff between par/fri

#6 look at differences between semantic networks, relate to prefs
