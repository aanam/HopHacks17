import gensim
import os
import collections
import smart_open
import random




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
    return  model

def doc2vec_vectors(dataset, model):
    for doc_id in range(len(dataset)):
        inferred_vector = model.infer_vector(dataset[doc_id].words)



ranks = []
second_ranks = []
'''
with open('/Users/amritaanam/Documents/GIT_Repo/HopHacks17/Data/' + 'training_data.txt', 'w+') as train_file:
    for doc_id in range(len(train_corpus)):
        #train_file.write('Document ({}): {}\n'.format(doc_id, ' '.join(train_corpus[doc_id].words)))
        inferred_vector = model.infer_vector(train_corpus[doc_id].words)
        sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
        rank = [docid for docid, sim in sims].index(doc_id)
        ranks.append(rank)

    second_ranks.append(sims[1])

collections.Counter(ranks)  # Results vary due to random seeding and very small corpus
print('Document ({}): {}\n'.format(doc_id, ' '.join(train_corpus[doc_id].words)))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: %s\n' % (label, sims[index], ' '.join(train_corpus[sims[index][0]].words)))
'''




def main(save):

    # Set file names for train and test data
    test_data_dir = '{}'.format(os.sep).join([gensim.__path__[0], 'test', 'test_data'])
    lee_train_file = test_data_dir + os.sep + 'lee_background.cor'
    lee_test_file = test_data_dir + os.sep + 'lee.cor'

    train_corpus = list(read_corpus(lee_train_file))
    test_corpus = list(read_corpus(lee_test_file, tokens_only=True))

    model = doc2vec_model(train_corpus)
    org_vecs = []
    with open(in_data) as our_file:
        for doc in our_file:
            org_vecs.append(model.infer_vector([doc.strip().split(" ")]))

    if save == 1:
        with open('/Users/amritaanam/Documents/GIT_Repo/HopHacks17/Data/' + 'training_data.txt', 'w+') as train_file:
            for doc_id in range(len(train_corpus)):
                train_file.write('Document ({}): {}\n'.format(doc_id, ' '.join(train_corpus[doc_id].words)))


        with open('/Users/amritaanam/Documents/GIT_Repo/HopHacks17/Data/' + 'test_data.txt', 'w+') as test_file:
            for doc_id in range(len(test_corpus)):
                test_file.write('Document ({}): {}\n'.format(doc_id, ' '.join(test_corpus[doc_id])))

in_data = 'some_path'
main(save=0)