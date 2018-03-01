'''
Created on 1 Mar 2018

@author: CyberNeurons
'''

import bibtexparser
import fire
import re
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import author


class Parser(object):
    '''
    The exported bib file from RefWorks is very hard to be cited in LateX editor. The EasyRef will convert "RefWorks:doc:5a12981de4b096fe30a0622b" to AUTHOR:YEAR:TITLE.
    '''
      
    def __init__(self):
        '''
        Constructor
        '''
        self._REGEX = "[^0-9a-zA-Z]+"  
        
    def parse(self, bib_file, out_bib_file):
        parser = BibTexParser()
        parser.customization = self._customizations
        with open(bib_file) as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file, parser=parser)
        self._store(out_bib_file, bib_database)
            
    def _store(self, out_file, bib_database):
        with open(out_file, 'w') as bibtex_file:
            bibtexparser.dump(bib_database, bibtex_file)

    def _customizations(self, record):
        """Use some functions delivered by the library
    
        :param record: a record
        :returns: -- customized record
        """
        
        orig_author_name = record["author"]
        record = author(record)
        if "author" in record:
            author_name = record["author"][0].split(",")[0]
        else:
            author_name = "NONE"
        year = "0000"
        title = "NONE"
        if "year" in record:
            year = record["year"]
        if "title" in record:
            title = record["title"]
            title = title.encode('ascii', 'ignore')
            title = re.sub(self._REGEX, '_', title)
        if "ID" in record:
            record["ID"] = author_name + ":" + year + ":" + title
        record["author"] = orig_author_name
        return record


fire.Fire(Parser)
