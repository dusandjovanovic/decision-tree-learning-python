
import numpy as numpy
import pandas as pandas
import pprint as pprint

epsilon = numpy.finfo(float).eps

main_attr = 'dangerous'
main_dataset_csv = 'dataset.csv'

def find_entropy(dataframe):
    Class = dataframe.keys()[-1]
    entropy = 0
    values = dataframe[Class].unique()
    for value in values:
        fraction = dataframe[Class].value_counts()[value] / len(dataframe[Class])
        entropy += -fraction * numpy.log2(fraction)
    return entropy

def find_entropy_attribute(dataframe, attribute):
    Class = dataframe.keys()[-1]
    target_variables = dataframe[Class].unique()
    variables = dataframe[attribute].unique()
    entropy2 = 0
    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(dataframe[attribute][dataframe[attribute] == variable][dataframe[Class] == target_variable])
            den = len(dataframe[attribute][dataframe[attribute] == variable])
            fraction = num / (den + epsilon)
            entropy += -fraction * numpy.log2(fraction + epsilon)
        fraction2 = den / len(dataframe)
        entropy2 += -fraction2 * entropy
    return abs(entropy2)

def find_winner(dataframe):
    IG = []
    for key in dataframe.keys()[:-1]:
        IG.append(find_entropy(dataframe) - find_entropy_attribute(dataframe, key))
    return dataframe.keys()[:-1][numpy.argmax(IG)]

def get_subtable(dataframe, node, value):
    return dataframe[dataframe[node] == value].reset_index(drop = True)

def build_tree(dataframe, tree = None):
    Class = dataframe.keys()[-1]

    node = find_winner(dataframe)
    att_value = numpy.unique(dataframe[node])

    if tree is None:
        tree = {}
        tree[node] = {}

    for value in att_value:
        subtable = get_subtable(dataframe, node, value)
        cl_value, counts = numpy.unique(subtable[main_attr], return_counts = True)

        if len(counts) == 1:
            tree[node][value] = cl_value[0]
        else:
            tree[node][value] = build_tree(subtable)

    return tree

def predict(attributes, tree):
    node = tree

    if type(node) is dict:
        for key in node.keys():
            x = node[key]
            y = x[attributes[key]]
            predict(attributes, node[key][attributes[key]]);
    else:
        print(f'\nSample for prediction: {attributes}.')
        print(f'\nPrediction for entered values is {node}.\n')

def main():
    dataframe = pandas.read_csv(main_dataset_csv)
    d3_tree = build_tree(dataframe)

    pprint.pprint(d3_tree)

    attributes = {
        "size": "medium",
        "sharp": "no",
        "feet": "yes",
        "habitat": "land",
        "domesticated": "no"
    }

    predict(attributes, d3_tree)
  
if __name__== "__main__":
    main()