from Domain.models.document import Document
from Domain.models.term import Term



class TFProcessorService:
    def __init__(self, document:Document, term:Term):
        self.document = document
        self.term = term

    async def process(self) -> Term:
        document_terms_count = len(self.document.all_terms)
        term_appearing_count = 0
        term_name = self.term.name

        for term in self.document.all_terms:
            if term == term_name:
                term_appearing_count += 1

        tf_score = float(term_appearing_count) / float(document_terms_count)
        return Term(name=term_name, tf_score=tf_score, tf_idf_score=self.term.TF_IDF_Score,idf_score=self.term.IDF_score,is_n_gram=self.term.isN_gram)
