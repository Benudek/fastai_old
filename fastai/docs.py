import tarfile
from fastai import *
from fastai.vision import *
from fastai.text import *

DATA_PATH = Path('..')/'data'
MNIST_PATH = DATA_PATH / 'mnist_sample'
IMDB_PATH = DATA_PATH / 'imdb_sample'

def untar_mnist():
    tarfile.open(MNIST_PATH.with_suffix('.tgz'), 'r:gz').extractall(DATA_PATH)

def untar_imdb():
    tarfile.open(IMDB_PATH.with_suffix('.tgz'), 'r:gz').extractall(DATA_PATH)

def get_mnist():
    if not MNIST_PATH.exists(): untar_mnist
    return image_data_from_folder(MNIST_PATH)

def get_imdb(classifier=False):
    if not IMDB_PATH.exists(): untar_imdb
    data_func = classifier_data if classifier else lm_data
    return text_data_from_csv(IMDB_PATH, tokenizer=Tokenizer(), data_func=data_func)

