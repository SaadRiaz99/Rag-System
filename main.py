
import csv
import document
filename = "document/Documenr.csv"

def load_document():
    with open (filename , "r" , encoding="utf-8") as file:
        data = csv.DictReader(file)

        return list(data)
loader = load_document()
def doumentcsv():
    for loader in document:
         print(document["title"])
    print(document["content"])
    print()
        