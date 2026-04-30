from math import log

from ....Domain.models.term import Term
from ....Domain.models.corpus import Corpus




class IDFProcessorService:
    def __init__(self,corpus:Corpus|None, term:Term):
        self.corpus = corpus
        self.term = term



    async def process(self) -> Term:
        documents_count = len(self.corpus.documents)
        documents_where_term_appear_count = 1

        for document in self.corpus.documents:
            if self.term in document.all_unique_terms:
                documents_where_term_appear_count += 1
            print(documents_where_term_appear_count)
        idf_score = float(log(documents_count / documents_where_term_appear_count))
        return Term(tf_idf_score=self.term.tf_idf_score,name=self.term.name,is_n_gram=self.term.is_n_gram, tf_score=self.term.tf_score, idf_score=idf_score)