from ....Domain.models.term import Term


async def find_n_max_keywords(terms:list[Term], max_keywords_count:int)->list[Term]:
    sorted_terms = terms.copy()
    sorted_terms.sort(key=lambda x: x.tf_idf_score, reverse=True)

    return sorted_terms[:max_keywords_count]




def custom_algorithm_to_filter_max_keywords(_terms:list[Term], max_keywords_count:int)->list[Term]:
    received_terms = _terms.copy()

    max_terms: list[Term] = []
    max_term = received_terms[0]

    tour = 0
    for i in range(max_keywords_count):
        for term in received_terms:
            if term.tf_idf_score > max_term.tf_idf_score:
                max_term = term
            tour += 1
            print(tour)
        max_terms.append(max_term)  # on remplit la liste de terms maximal par le nouveau term
        received_terms.remove(max_term)  # on efface de la liste des terms, le terme maximal trouvé
        max_term = received_terms[
            0]  # on définit le nouveau term maximal à comparer, comme étant le premier élément de la liste courante de terms
    print(f"Tours : {tour}, max_keywords_count : {max_keywords_count}, complexity: {max_keywords_count * len(_terms)}")
    return max_terms