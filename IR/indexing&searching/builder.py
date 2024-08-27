import logging, sys
logging.disable(sys.maxsize)
import sys
import lucene
import os
from org.apache.lucene.store import MMapDirectory, SimpleFSDirectory, NIOFSDirectory
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.analysis.core import WhitespaceAnalyzer, SimpleAnalyzer, StopAnalyzer
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions, DirectoryReader
from org.apache.lucene.search import IndexSearcher, BoostQuery, Query
from org.apache.lucene.search.similarities import BM25Similarity
import json

def create_index(dir, anlzr="Standard"):
    if not os.path.exists(dir):
        os.mkdir(dir)
    store = SimpleFSDirectory(Paths.get(dir))
    if anlzr=="Standard":
        analyzer = StandardAnalyzer()
    elif anlzr=="WhiteSpace":
        analyzer = WhitespaceAnalyzer()
    elif anlzr=="Simple":
        analyzer = SimpleAnalyzer()
    elif anlzr=="Stop":
        analyzer = StopAnalyzer()

    config = IndexWriterConfig(analyzer)
    config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
    writer = IndexWriter(store, config)

    metaType = FieldType()
    metaType.setStored(True)
    metaType.setTokenized(False)

    contextType = FieldType()
    contextType.setStored(True)
    contextType.setTokenized(True)
    contextType.setIndexOptions(IndexOptions.DOCS_AND_FREQS_AND_POSITIONS)

    for document in documents:
        Name = document['Name']
        URL = document['URL']
        Data = document['Data']
        Image_Serialized = document['Image_Serialized']

        doc = Document()
        doc.add(Field('Name', str(Name), metaType))
        doc.add(Field('URL', str(URL), metaType))
        doc.add(Field('Image_Serialized', str(Image_Serialized), metaType))
        doc.add(Field('Data', str(Data), contextType))
        writer.addDocument(doc)
    writer.close()

if __name__=="__main__":
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    # Path to your JSON file
    json_file_path = sys.argv[1]

    # Load the JSON data from the file
    with open(json_file_path, 'r', encoding='utf8') as file:
        documents = json.load(file)
    create_index('sample_lucene_index/', sys.argv[2])