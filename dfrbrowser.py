import json
import os
from zipfile import ZipFile
from scipy.sparse import csc_matrix

class dfrBrowserConverter():
    
    def __init__(self, ldahandler, path='data', num_words = 20):
        self.ldahandler = ldahandler
        self.ldamodel = ldahandler.model
        self.path = path
        # self.num_topics =
        self.num_words = num_words
        
    def generate_files(self, title='title', meta_info='meta info', data=None):
        
        os.mkdir(self.path)
        
        self.create_info(title, meta_info)
        self.create_dt()
        self.create_tw()
        self.create_meta(data)
        
    def create_info(self, title, meta_info, vis=None, topic_labels=None):
        
        dc = {'title': title, 'meta_info': meta_info}
        
        vis = {"metadata": {
                    "type": "base"
                },
               "bib": {
                    "type": "base"
               },
               "bib_view": {
                    "major": "all",
                    "minor": "raw"
               },
               "condition": {
                    "type": "ordinal",
                    "name": "text",
                    "spec": {
                        "field": "text"
                    }
               }  
              } 
        
        if vis: dc['vis'] = vis
        if topic_labels: dc['topic_labels'] = topic_labels
        
        with open(self.path+'/info.json', 'w') as f:
            json.dump(dc, f, indent=4)   

    def create_tw(self):
                
        dc = {'alpha': self.ldamodel.alpha.tolist(),
              'tw': self.get_word_topics()}
        
        with open(self.path+'/tw.json', 'w') as f:
            json.dump(dc, f, indent=4)
            
    def create_dt(self):
        
        doc_topics = self.ldahandler.get_doc_topic_matrix()
        
        dc = {'i': csc_matrix(doc_topics).toarray().tolist()}
        
        with open(self.path+'/dt.json', 'w') as f:
            json.dump(dc, f, indent=4)
        
        with ZipFile(self.path+'/dt.json.zip', 'w') as zip:
            zip.write(self.path+'/dt.json')
            
        os.remove(self.path+'/dt.json')
        
    def create_meta(self, data):
        
        data.to_csv(self.path+'/meta.csv', sep=',', index=False, header=True)
        
        with ZipFile(self.path+'/meta.csv.zip', 'w') as zip:
            zip.write(self.path+'/meta.csv')
            
        os.remove(self.path+'/meta.csv')
    
    # def def_vis()
        
    def get_word_topics(self):
        
        word_topics = self.ldamodel.show_topics(num_topics=-1, num_words=self.num_words, formatted=False)
        list_topics = []
        
        for i in word_topics:
            
            dc = {}
            dc['words'] = [j[0] for j in i[1]]
            dc['weights'] = [j[1] for j in i[1]]
            
            list_topics.append(dc)
            
        return list_topics