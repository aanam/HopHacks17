import gensim
import os
import collections
import smart_open
import random
from pymongo import MongoClient
import pandas as pd
import numpy as np
from scipy import spatial

def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])


def doc2vec_model(train_corpus):
    model = gensim.models.doc2vec.Doc2Vec(size=50, min_count=2, iter=100)
    model.build_vocab(train_corpus)
    return model


def doc_similarity(q, doc_df):
    doc = doc_df.values

    sim = []
    for row in doc:
        sim.append(1 - spatial.distance.cosine(q, row))
    sim_rank = pd.DataFrame(sim, index=doc_df.index.tolist(), columns = ['similarity'])
    sim_rank = sim_rank.sort_values(by='similarity', ascending=False)
    return sim_rank[0:3]


def main(query, save):
    # Set file names for train and test data
    test_data_dir = '{}'.format(os.sep).join([gensim.__path__[0], 'test', 'test_data'])
    lee_train_file = test_data_dir + os.sep + 'lee_background.cor'
    lee_test_file = test_data_dir + os.sep + 'lee.cor'

    train_corpus = list(read_corpus(lee_train_file))
    test_corpus = list(read_corpus(lee_test_file, tokens_only=True))

    model = doc2vec_model(train_corpus)
    org_vecs = []
    org_names = []

    client = MongoClient('localhost', 27017)
    db = client['organizations']
    posts = db.posts

    for doc in posts.find():
        org_names.append(str(doc['name']))
        doc = doc['about'].strip().split()
        org_vecs.append(model.infer_vector(doc))

    doc_df = pd.DataFrame(org_vecs, index = org_names)
    doc_df = doc_df.drop_duplicates()
    q_vec = model.infer_vector(query.strip().split())

    top_3 = doc_similarity(q_vec, doc_df)

    if save == 1:
        doc_df.to_csv("org.csv")
        with open('Data/' + 'training_data.txt', 'w+') as train_file:
            for doc_id in range(len(train_corpus)):
                train_file.write('Document ({}): {}\n'.format(doc_id, ' '.join(train_corpus[doc_id].words)))

        with open('Data/' + 'test_data.txt', 'w+') as test_file:
            for doc_id in range(len(test_corpus)):
                test_file.write('Document ({}): {}\n'.format(doc_id, ' '.join(test_corpus[doc_id])))

query = "I have been affected by hurricane"
main( query, save=0)
