from ....Domain.models.term import Term



class TFIDFProcessorService:
    def __init__(self, term:Term):
        self.term = term

    async def process(self) -> Term:
        tf_idf_score = self.term.tf_score * self.term.idf_score
        return Term(is_n_gram=self.term.is_n_gram,idf_score=self.term.idf_score,tf_score=self.term.tf_score,tf_idf_score=tf_idf_score,name=self.term.name)