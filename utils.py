from bs4 import BeautifulSoup
from nltk import word_tokenize
import numpy as np

# loading data

def load_data(path_to_data):
    """
    Loads `.tsv` of data into a <dict>
    Ensures that `.html` has been removed
    :param path_to_data: full/path/to/data
    :return: <list> of <tuple> ([id], [label], [text])
    """
    out_ = []
    with open(path_to_data, "r") as f:
        for line in f:
            # parse line
            line_split = line.rstrip().split("\t")
            if len(line_split) != 3:
                continue
            id = line_split[0]
            label = line_split[1]
            raw_text = line_split[2]
            # ensure html is removed
            text = BeautifulSoup(raw_text, "html.parser").get_text()
            out_.append((id, label, text))
    return out_

def get_all_docs(list_of_tuples):
    """
    Given a dictionary of data, this will collect all the text into one list
    :param list_of_tuples: Output of load_data()
    :return <list> of documents, lookup_dict
    """
    all_docs = []
    lookup = {}
    for i in range(len(list_of_tuples)):
        current = list_of_tuples[i]
        all_docs.append(current[2])
        lookup[i] = current[2]
    return all_docs, lookup

# calculations

def normalize_vector(vector):
    """
    Normalizes a vector so that all its values are between 0 and 1
    :param vector: a `numpy` vector
    :return: a normalized `numpy` vector
    """
    # norm = np.sqrt(vector.dot(vector))
    # numpy has a built in function
    norm = np.linalg.norm(vector)
    if norm:
        return vector / norm
    else:
        # if norm == 0, then original vector was all 0s
        return vector

def cos_sim(vector_one, vector_two):
    """
    Calculate the cosine similarity of two `numpy` vectors
    :param vector_one: a `numpy` vector
    :param vector_two: a `numpy` vector
    :return: A score between 0 and 1
    """
    # ensure that both vectors are already normalized
    vector_one_norm = normalize_vector(vector_one)
    vector_two_norm = normalize_vector(vector_two)

    # calculate the dot product between the two normalized vectors
    return vector_one_norm.dot(vector_two_norm)

def generate_all_cos_sim(X_matrix):
    """
    Generates a matrix of cosine similarities for a set of documents
    WARNING: this is too computationally expensive for a python notebook.  Run in console.
    :param X_matrix: dense `numpy` matrix: num_documents (d) x words_in_vocabulary (v)
    :return: dense `numpy` matrix d x d
    """
    # ensure matrix is dense
    if "sparse" in str(type(X_matrix)):
        X_matrix = X_matrix.toarray()
    # get shape
    X_shape = X_matrix.shape
    size = X_shape[0]
    # build empty matrix
    cos_matrix = np.zeros((size, size))
    # iterate through rows
    for i in range(size):
        for j in range(size):
            if i != j:
                print(i,j)
                # calculate cosine similarity
                cos_matrix[i][j] = cos_sim(X_matrix[i], X_matrix[j])
            else:
                # set diagonal to None
                cos_matrix[i][j] = None
    return cos_matrix

def get_similar(cos_sim_matrix, idx, n, direction="most"):
    """
    Determines similarity of n documents
    :param cos_sim_matrix: `numpy` dense array of num_documents x num_documents with values as cosine similarity
    :param idx: index of document to calculate most similar
    :param n: number of most similar indices to return
    :param direction: "most" or "least" for top or bottom of ranked list
    :return: <list> of (idx, cos_sim)
    """
    if direction != "most" and direction != "least":
        raise Exception("chooose `most` or `least` for `direction`")
    # get all values
    if direction == "most":
        all_values = sorted(enumerate(filter(lambda x: not np.isnan(x), cos_sim_matrix[idx])), key=lambda x: x[1], reverse=True)
    else:
        all_values = sorted(enumerate(filter(lambda x: not np.isnan(x), cos_sim_matrix[idx])), key=lambda x: x[1])
    return [(x[0] + 1, x[1]) for x in all_values[:n]]


# I/O

def save_matrix_to_csv(X_matrix, save_location):
    """
    Saves a matrix to csv
    :param X_matrix: dense `numpy` array
    :param save_location: full/path/to/desired/location.csv
    """
    # ensure matrix is dense
    if "sparse" in str(type(X_matrix)):
        X_matrix = X_matrix.toarray()
    np.savetxt(save_location, X_matrix, delimiter=",")

def load_matrix_from_csv(location):
    """
    Loads a matrix from csv
    :param location: full/path/to/location.csv
    :return: dense `numpy` array
    """
    return np.loadtxt(location, delimiter=",")

