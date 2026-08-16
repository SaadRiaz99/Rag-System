
import csv

filename = "Document.csv"

def load_document():
    with open (filename , "r" , encoding=UnicodeTranslateError) as file:
        csv.load(file)