#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import csv
import pandas
# TODO: Définissez vos fonctions ici
def read(path : str="./data/winequality-white.csv"):
    with open('file.csv') as csv_file:
        df = csv.reader(csv_file, delimiter=';')
        x = df["quality"]
        y = df.drop(columns = ["quality"])
    return np.array([x,y])



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    read(winequality_white.csv)