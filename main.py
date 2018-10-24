import argparse

from models import *
from dataset import *

model_names = ['KNN', 'RF', 'LR', 'SVM', 'MLP', 'VGG16', 'DenseNet']
parser = argparse.ArgumentParser(description='P1 Cell Image Classification')
parser.add_argument('model', choices=model_names)

parser.add_argument('space', choices=['image', 'wndchrm'])


if __name__ == '__main__':
    args = parser.parse_args()
    if args.space == 'wndchrm' and args.model in ['VGG16', 'DenseNet']:
        raise ValueError("conflict options: {} {}".format(args.model, args.space))

    dataset = load_dataset(space=args.space)
    if args.model in ['VGG16', 'DenseNet']:
        nn_clf(args.model, dataset)
    else:
        sklearn_clf(args.model, dataset)

