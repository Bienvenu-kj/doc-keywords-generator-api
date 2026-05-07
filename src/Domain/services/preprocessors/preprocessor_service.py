from ...ports.custom_print import CustomPrint, CustomPrintData
from ...ports.preprocessors.i_cleaner import Cleaner
from ...ports.preprocessors.i_normalizer import Normalizer
from ...ports.preprocessors.i_tokenizer import Tokenizer
from ...utils.custom_print_util import CustomPrintUtil
from ....Domain.models.preprocessing_result import PreprocessingResult
from ....Domain.services.preprocessors.cleaner import CleanerService
from ....Domain.services.preprocessors.normalizer import NormalizerService
from ....Domain.services.preprocessors.term_constructor import TermConstructorService
from ....Domain.services.preprocessors.tokenizer import TokenizerService


class PreprocessorService:
    def __init__(self, tokenizer: Tokenizer, normalizer:Normalizer, cleaner:Cleaner,printer:CustomPrint):
        self.normalizer = normalizer
        self.tokenizer = tokenizer
        self.cleaner = cleaner
        self.printer = printer

    async def preprocess(self,document_content:str)->PreprocessingResult:
        """
            Prétraitement du document
        """

        # normalisation
        normalized_content = await NormalizerService(normalizer=self.normalizer).normalize(document_content)
        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("success", "Nous venons de normaliser son contenu")).print()


        # nettoyage
        cleaned_content = await CleanerService(cleaner=self.cleaner).clean(normalized_content)
        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("success", "Nous venons de le nettoyer")).print()


        # tokenisation
        tokens = await TokenizerService(tokenizer=self.tokenizer).tokenize(cleaned_content, n_gram=False)
        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("success", "Nous venons de générer les tokens")).print()


        # construction de terms avec 0 comme valeur aux propriétés tf, idf et tf_idf
        terms = await TermConstructorService().construct_terms(tokens)
        CustomPrintUtil(custom_print=self.printer,data=CustomPrintData("success", "Nous avons maintenant les termes")).print()


        return PreprocessingResult(all_unique_terms=terms,all_terms=tokens)


