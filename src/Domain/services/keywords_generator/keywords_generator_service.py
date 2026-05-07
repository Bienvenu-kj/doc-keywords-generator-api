from ...models.corpus import Corpus
from ...models.document import Document
from ...models.keyword import Keyword
from ...models.term import Term
from ...ports.custom_print import CustomPrint, CustomPrintData
from ...services.keywords_generator.find_n_max_keywords import find_n_max_keywords
from ...services.tf_idf_processors.idf_processor_service import IDFProcessorService
from ...services.tf_idf_processors.tf_idf_processor_service import TFIDFProcessorService
from ...services.tf_idf_processors.tf_processor_service import TFProcessorService
from ...utils.custom_print_util import CustomPrintUtil


class KeywordsGeneratorService:
    def __init__(self,corpus:Corpus|None, max_keywords_count:int, document:Document, custom_printer:CustomPrint):
        self.corpus = corpus
        self.max_keywords_count = max_keywords_count
        self.document = document
        self.printer = custom_printer

    async def generate_keywords(self) -> list[Keyword]:

        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("warning",f"génération encours sur le : {self.document.name}")).print()
        terms_with_tf_score : list[Term]= []
        terms_with_idf_score : list[Term]= []
        terms_with_tf_idf_score : list[Term]= []

        # on calcule le score tf de chaque term
        for term in self.document.all_unique_terms:
            terms_with_tf_score.append((await TFProcessorService(document=self.document,term=term).process()))
        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("success", f"calcul du tf déjà fait ! {len(terms_with_tf_score)} - {len(self.document.all_terms)}")).print()

        # on calcule le score idf de chaque term
        for term in terms_with_tf_score:
            terms_with_idf_score.append((await IDFProcessorService(corpus=self.corpus,term=term).process()))
        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("success", f"calcul du idf, vient d'être fait aussi ! {len(terms_with_idf_score)} - {len(self.document.all_terms)}")).print()

        # on calcule enfin le score tf_idf de chaque term
        for term in terms_with_idf_score:
            terms_with_tf_idf_score.append((await TFIDFProcessorService(term=term).process()))
        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("success", f"calcul du tf_idf enfin fait aussi ! {len(terms_with_tf_idf_score)} - {len(self.document.all_terms)}")).print()

        self.document.__setitem__("all_unique_terms",terms_with_tf_idf_score)
        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("warning", "les mots-clés sont presque prêt à être généré")).print()

        keywords = [Keyword(term=term) for term in (await find_n_max_keywords(terms=terms_with_tf_idf_score,max_keywords_count=self.max_keywords_count))]
        return keywords