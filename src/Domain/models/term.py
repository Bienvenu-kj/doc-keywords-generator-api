
class Term:
    def __init__(self,
        name:str,is_n_gram:bool,tf_score:float,
        idf_score:float,tf_idf_score:float
    ):
        self.name = name
        self.isN_gram = is_n_gram
        self.TF_score = tf_score
        self.IDF_score = idf_score
        self.TF_IDF_Score = tf_idf_score
