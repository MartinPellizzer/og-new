triples = []
def triple_add(_subject, _predicate, _object, _source):
    triple = {
        'subject': _subject,
        'predicate': _predicate,
        'object': _object,
        'source': _source,
    }
    triples.append(triple)

triple_add('ozone', 'has_preferred_chemical_name', 'ozone', 'PubChem', 1)
triple_add('ozone', 'has_common_name', 'ozone', 'EN 1278:2024', 2)
triple_add('ozone', 'has_scientific_name', 'ozone', 'PubChem', 3)
triple_add('ozone', 'has_iupac_name', 'trioxygen', 'IUPAC Red Book', 4)
triple_add('ozone', 'has_systematic_name', 'trioxygen', 'IUPAC Red Book', 5)
triple_add('ozone', 'has_alternative_name', 'trioxygen', '', 6)
triple_add('ozone', 'has_alternative_name', 'triatomic oxygen', '', 6)
triple_add('ozone', 'has_alternative_name', 'trioxygene', '', 6)
triple_add('ozone', 'has_alternative_name', 'ozon', '', 6)
triple_add('ozone', 'has_hystorical_name', 'ozon', '', 7)
triple_add('ozone', 'has_hystorical_name', 'electrified oxygen', '', 7)
triple_add('ozone', 'has_hystorical_name', 'electrical odour', '', 7)
triple_add('ozone', 'has_trivial_name', 'ozone', '', 8)
triple_add('ozone', 'has_trivial_name', 'trioxygen', '', 8)
triple_add('ozone', 'has_trivial_name', 'triatomic oxygen', '', 8)
triple_add('ozone', 'has_synonym', 'trioxygen', '', 9)
triple_add('ozone', 'has_synonym', 'triatomic oxygen', '', 9)
triple_add('ozone', 'has_synonym', 'ozon', '', 9)
triple_add('ozone', 'has_synonym', 'o3', '', 9)
triple_add('ozone', 'has_synonym', 'oxygen, mol. (o3)', '', 9)
triple_add('ozone', 'has_synonym', 'trisauerstoff', '', 9)
triple_add('ozone', 'has_synonym', 'trioxygene', '', 9)
triple_add('ozone', 'has_abbreviation', 'o3', '', 10)
