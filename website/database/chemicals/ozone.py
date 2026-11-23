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
triple_add('ozone', 'has_chemical_formula', 'o3', '', 11)
triple_add('ozone', 'has_molecurlar_formula', 'o3', '', 12)
triple_add('ozone', 'has_empirical_formula', 'o3', '', 13)
triple_add('ozone', 'has_structural_formula', 'O=O⁺–O⁻ ↔ ⁻O–O⁺=O', '', 14)
triple_add('ozone', 'has_molecular_entity_type', 'elemental molecule', '', 15)
triple_add('ozone', 'has_chemical_substance_classification', 'inorganic molecular substance', '', 16)
triple_add('ozone', 'has_chemical_species_classification', 'elemental molecule', '', 17)
triple_add('ozone', 'has_chemical_family', 'oxygen allotropes', '', 18)
triple_add('ozone', 'has_chemical_class', 'elemental molecule', '', 19)
triple_add('ozone', 'has_inorganic_or_organic_classification', 'inorganic', '', 20)
triple_add('ozone', 'has_elemental_substance_classification', 'elemental molecule', '', 21)
triple_add('ozone', 'has_molecular_substance_classification', 'elemental molecule', '', 22)
triple_add('ozone', 'has_allotrope_classification', 'oxygen', '', 23)
triple_add('ozone', 'has_oxidant_classification', 'strong oxidizing agent', '', 24)
triple_add('ozone', 'has_reactive_oxygen_species_classification', 'non-radical reactive oxygen species (ROS)', '', 25)
triple_add('ozone', 'has_atmospheric_chemical_species_classification', 'reactive gas', '', 26)

