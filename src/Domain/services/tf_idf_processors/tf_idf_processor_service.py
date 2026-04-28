from Domain.models.term import Term



class TFIDFProcessorService:
    def __init__(self, term:Term):
        self.term = term

    async def process(self) -> Term:
        tf_idf_score = self.term.TF_score * self.term.IDF_score
        return Term(is_n_gram=self.term.isN_gram,idf_score=self.term.IDF_score,tf_score=self.term.TF_score,tf_idf_score=tf_idf_score,name=self.term.name)