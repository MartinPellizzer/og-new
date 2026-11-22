# Ozone Fundamentals: Master RDF Knowledge Graph Blueprint

For this first article, I would approach the task differently from writing a conventional article.

You are not simply collecting facts about ozone. You are building a **structured scientific knowledge graph from which an authoritative article about ozone can be generated**.

That distinction is important.

A conventional article might say:

"Ozone is a triatomic molecule consisting of three oxygen atoms. It is a powerful oxidising agent and is naturally present in Earth's atmosphere."

Your RDF dataset should be capable of representing every individual fact in that sentence, its scientific relationships, its properties, its qualifications and its sources.

For example:

```turtle
:Ozone
    rdf:type :ChemicalSubstance ;
    :hasChemicalFormula "O3" ;
    :hasCommonName "Ozone" ;
    :hasSystematicName "Trioxygen" ;
    :hasMolecularComposition :ThreeOxygenAtoms ;
    :hasOxidisingCharacter :StrongOxidisingAgent ;
    :hasAtmosphericOccurrence :EarthAtmosphere .
```

And:

```turtle
:OzoneMolecule
    :hasAtomCount 3 ;
    :hasElementalComposition :Oxygen ;
    :hasMolecularGeometry :BentMolecularGeometry ;
    :hasMolecularWeight "47.997"^^xsd:decimal .
```

These are illustrative triples, not a fully validated chemical ontology. Some relationships, such as molecular weight, should be represented with proper units, provenance and measurement conventions.

## 1. First, define the scope of your Fundamentals article

I recommend that this first article cover the identity and intrinsic scientific properties of ozone.

It should answer:

- What exactly is ozone?
- What is its chemical identity?
- What is its molecular structure?
- How is its molecule constructed?
- What are its physical properties?
- What are its chemical properties?
- How does it behave chemically?
- How is it formed?
- How does it decompose?
- Why is it unstable?
- Why is it such a powerful oxidising agent?
- How does it interact with other substances?
- What is its natural occurrence?
- How was it discovered?
- How is it classified scientifically?
- How is it named, identified and measured?

I would deliberately keep detailed atmospheric processes, ozone depletion, health effects, commercial generation technologies and applications for separate articles.

Those subjects can be linked to the Fundamentals article through RDF relationships.

The Fundamentals article should establish the scientific identity of ozone that all subsequent articles build upon.

---

# 2. The complete RDF subject taxonomy

I would organise your knowledge graph into the following 25 major domains.

| ID | Domain | What it describes |
|---|---|---|
| F01 | Identity and classification | What ozone is |
| F02 | Names and terminology | Chemical and common names |
| F03 | Chemical identifiers | CAS, InChI, SMILES and identifiers |
| F04 | Chemical composition | Elements and atomic composition |
| F05 | Molecular structure | Molecular architecture |
| F06 | Electronic structure | Electrons, orbitals and bonding |
| F07 | Molecular geometry | Shape, angles and bond lengths |
| F08 | Molecular properties | Intrinsic molecular characteristics |
| F09 | Physical properties | Measurable physical characteristics |
| F10 | Thermodynamic properties | Energy, entropy and phase behaviour |
| F11 | Spectroscopic properties | Interaction with electromagnetic radiation |
| F12 | Chemical properties | Reactivity and chemical behaviour |
| F13 | Oxidation chemistry | Oxidation potential and redox behaviour |
| F14 | Formation chemistry | How ozone forms |
| F15 | Decomposition chemistry | How ozone breaks down |
| F16 | Reaction mechanisms | How ozone reacts |
| F17 | Chemical stability | Factors affecting stability |
| F18 | Solubility and partitioning | Behaviour in water and other media |
| F19 | Natural occurrence | Where ozone exists naturally |
| F20 | Isotopes and isotopologues | Isotopic variations |
| F21 | Historical development | Discovery and scientific milestones |
| F22 | Scientific classification | Chemical and physical classifications |
| F23 | Measurement and units | How ozone properties are expressed |
| F24 | Scientific models and theories | Models used to explain ozone |
| F25 | Scientific references and provenance | Evidence supporting every fact |

This gives you the overall structure. Below is the actual data-point inventory I would use.

# 3. Detailed data-point inventory

The following is the actual extraction specification. Each bullet should become one or more RDF triples, depending on its structure.

## F01 — Chemical identity and classification

### Basic identity
- Preferred chemical name.
- Common name.
- Scientific name.
- IUPAC name.
- Systematic name, where applicable.
- Alternative names.
- Historical names.
- Trivial names.
- Synonyms.
- Abbreviations.
- Chemical formula.
- Molecular formula.
- Empirical formula.
- Structural formula.
- Molecular entity type.
- Chemical substance classification.
- Chemical species classification.
- Chemical family.
- Chemical class.
- Inorganic or organic classification.
- Elemental substance classification.
- Molecular substance classification.
- Allotrope classification.
- Oxidant classification.
- Reactive oxygen species classification, with a clear explanation of the chemical context.
- Atmospheric chemical species classification.

### Scientific identity
- Whether ozone is an element or compound.
- Whether ozone is a molecule.
- Whether ozone is a molecular allotrope of oxygen.
- Whether ozone is a pure substance.
- Whether ozone is a chemical species.
- Whether ozone is naturally occurring.
- Whether ozone is synthetically producible.
- Whether ozone is a free radical.
- Whether ozone is an ion.
- Whether ozone is electrically neutral.
- Whether ozone is a stable or metastable species.
- Whether ozone is an oxidising agent.
- Whether ozone is a molecular gas.

### Classification relationships
- Ozone belongs to the oxygen chemical family.
- Ozone is composed exclusively of oxygen atoms.
- Ozone is an allotrope of oxygen.
- Ozone is distinct from molecular oxygen.
- Ozone is distinct from atomic oxygen.
- Ozone is distinct from singlet oxygen.
- Ozone is distinct from superoxide.
- Ozone is distinct from peroxide.
- Ozone is distinct from oxygen ions.

**Important conceptual distinction:** Ozone is an elemental molecular substance and an allotrope of oxygen. It is not a chemical compound composed of different elements.

## F02 — Names and terminology

Create individual records for every recognised name.

Data points:

- Preferred name.
- IUPAC name.
- Common name.
- Systematic nomenclature name.
- Alternative name.
- Historical name.
- Synonym.
- Language.
- Linguistic origin.
- Etymology.
- Pronunciation.
- Phonetic transcription.
- Abbreviation.
- Chemical naming authority.
- Source of the name.
- Date the name entered scientific use.
- Whether the name is preferred, accepted, historical or deprecated.

Include names in:

- English.
- German.
- French.
- Italian.
- Spanish.
- Portuguese.
- Dutch.
- Russian.
- Chinese.
- Japanese.
- Arabic.

You can expand this to additional languages.

Also include:

- Ozone.
- Trioxygen.
- Triatomic oxygen.
- Ozon.
- Ozonium, but explicitly distinguish this from ozone where relevant.
- Trioxidane, with its nomenclatural status and source carefully documented.

Don't assume every synonym is an equally valid chemical name.

## F03 — Chemical identifiers

Store every identifier independently.

| Identifier | Data point |
|---|---|
| CAS Registry Number | 10028-15-6 |
| PubChem CID | 24823 |
| Molecular formula | O₃ |
| InChI | InChI=1S/O3/c1-3-2 |
| InChIKey | CBENFWSGALASAD-UHFFFAOYSA-N |
| SMILES | [O-][O+]=O |
| Molecular weight | Approximately 47.998 g/mol |

Additional data points:

- EC number, if verified.
- UN identification number, where applicable to the relevant transport classification.
- ECHA substance identifier.
- EPA DSSTox identifier.
- NIST Chemistry WebBook identifier.
- IUPAC International Chemical Identifier.
- Chemical Abstracts Service identifier.
- Chemical database identifiers.
- Identifier issuing organisation.
- Identifier format.
- Identifier status.
- Identifier validity.
- Identifier source.
- Date verified.

Primary identification references:

- [PubChem — Ozone](https://pubchem.ncbi.nlm.nih.gov/compound/Ozon?utm_source=chatgpt.com)
- [NIST Chemistry WebBook — Ozone](https://webbook.nist.gov/cgi/cbook.cgi?Name=Ozone&utm_source=chatgpt.com)

## F04 — Chemical composition and atomic structure

### Elemental composition
- Number of constituent atoms.
- Number of oxygen atoms.
- Number of distinct elements.
- Elemental composition.
- Atomic composition.
- Atomic ratio.
- Elemental mass composition.
- Molecular mass contribution of each atom.
- Total molecular mass.

### Atomic properties
For each oxygen atom:

- Element name.
- Element symbol.
- Atomic number.
- Atomic mass.
- Number of protons.
- Number of neutrons, for a specified isotope.
- Number of electrons.
- Electron configuration.
- Valence electrons.
- Oxidation state.
- Formal charge.
- Isotopic identity.

### Composition relationships
- Ozone contains three oxygen atoms.
- Ozone contains no other elements.
- All constituent atoms are oxygen.
- Ozone has a molecular formula of O₃.
- Ozone has an empirical formula of O.
- Ozone has a molar mass of approximately 48 g/mol.

Note the distinction between the molecular formula and empirical formula.

## F05 — Molecular structure

This should be one of your most detailed domains.

### Structural characteristics
- Molecular structure.
- Molecular connectivity.
- Molecular topology.
- Number of atoms.
- Number of bonds.
- Number of oxygen–oxygen connections.
- Molecular symmetry.
- Point group.
- Molecular conformation.
- Molecular geometry.
- Molecular shape.
- Planarity.
- Molecular dimensions.
- Molecular orientation.

### Bonding characteristics
- Oxygen–oxygen bond connectivity.
- Bond order.
- Average bond order.
- Bond length.
- Bond angle.
- Bond dissociation energy.
- Bond strength.
- Bond polarity.
- Electron density.
- Electron delocalisation.
- Resonance.
- Resonance contributors.
- Bond equivalence.
- Bond character.
- Bonding orbitals.
- Antibonding orbitals.

### Resonance
Represent:

- Resonance contributor A.
- Resonance contributor B.
- Formal charges in each contributor.
- Electron distribution.
- Delocalisation of electrons.
- Relationship between resonance contributors.
- Actual molecular structure as a resonance hybrid.
- Limitations of depicting ozone with a single Lewis structure.

### Molecular geometry
- Bent geometry.
- Approximate bond angle.
- Equilibrium bond length.
- Symmetry properties.
- Molecular plane.
- Central oxygen position.
- Terminal oxygen positions.
- Structural equivalence of terminal atoms.

### Quantum mechanical structure
- Electronic ground state.
- Electronic configuration.
- Molecular orbital occupation.
- Valence molecular orbitals.
- Highest occupied molecular orbital.
- Lowest unoccupied molecular orbital.
- Electronic excitation states.
- Electronic wavefunction.
- Potential energy surface.
- Vibrational normal modes.
- Rotational constants.

## F06 — Electronic structure and bonding

Include:

- Total number of electrons.
- Number of valence electrons.
- Electronic ground state.
- Spin multiplicity.
- Electronic term symbol.
- Electronic configuration.
- Molecular orbital theory description.
- Valence bond theory description.
- Molecular orbital occupancy.
- Electron distribution.
- Charge distribution.
- Partial charges.
- Formal charges.
- Resonance.
- Electron delocalisation.
- Electronegativity differences.
- Bonding and antibonding interactions.
- HOMO energy.
- LUMO energy.
- HOMO–LUMO gap.
- Ionisation energy.
- Electron affinity.
- Electronic excitation energies.
- Excited electronic states.
- Electronic transition probabilities.
- Polarizability.
- Hyperpolarizability, where available.

Include an explanation of why ozone's bonding cannot be adequately described by treating its two O–O bonds as independent conventional single and double bonds.

## F07 — Molecular geometry and dimensions

Create separate records for:

- Molecular geometry classification.
- Equilibrium bond angle.
- Experimental bond length.
- Calculated bond length.
- Symmetry.
- Point group.
- Planarity.
- Centre of mass.
- Principal moments of inertia.
- Rotational constants.
- Molecular dipole moment.
- Quadrupole moment.
- Molecular polarizability tensor.
- Cartesian coordinates.
- Internal coordinates.
- Optimised molecular geometry.
- Computational method used.
- Basis set used.
- Geometry optimisation conditions.

For numerical values, always store:

- Value.
- Unit.
- Method.
- Experimental or computational origin.
- Temperature, if relevant.
- Uncertainty.
- Reference.

## F08 — Intrinsic molecular properties

Include:

- Molecular weight.
- Molar mass.
- Exact isotopic mass.
- Average molecular mass.
- Molecular dipole moment.
- Molecular polarizability.
- Electronic polarizability.
- Magnetic susceptibility.
- Ionisation energy.
- Electron affinity.
- Rotational constants.
- Vibrational frequencies.
- Electronic energy.
- Molecular symmetry.
- Molecular orbital energies.
- Thermodynamic functions.

Avoid mixing intrinsic molecular properties with bulk gas properties.

For example, molecular mass is intrinsic to the specified isotopic composition, while gas density depends on temperature and pressure.

---

# 4. Physical properties

## F09 — Physical state and appearance

### General appearance
- Physical state at specified temperature and pressure.
- Appearance.
- Colour of gas.
- Colour of liquid.
- Colour of solid.
- Characteristic odour.
- Odour description.
- Odour threshold, with measurement conditions.
- Optical appearance.
- Transparency.
- Visible absorption.
- Phase-dependent appearance.

### Phase behaviour
- Gas phase.
- Liquid phase.
- Solid phase.
- Condensation.
- Freezing.
- Melting.
- Sublimation, where applicable.
- Deposition.
- Boiling.
- Evaporation.
- Critical point.
- Triple point, if established.
- Metastable phase behaviour.
- Decomposition during phase transitions.

### Temperature-dependent properties
- Gas properties at standard temperature.
- Gas properties at room temperature.
- Liquid properties at specified temperatures.
- Solid properties at specified temperatures.
- Temperature dependence of density.
- Temperature dependence of vapour pressure.
- Temperature dependence of solubility.
- Temperature dependence of stability.

## F10 — Thermodynamic properties

This should be an extensive numerical dataset.

### Thermodynamic quantities
- Standard enthalpy of formation.
- Standard enthalpy of combustion, where meaningful.
- Standard Gibbs energy of formation.
- Standard entropy.
- Molar heat capacity.
- Constant-pressure heat capacity.
- Constant-volume heat capacity.
- Heat capacity ratio.
- Enthalpy.
- Entropy.
- Gibbs free energy.
- Helmholtz free energy.
- Internal energy.
- Chemical potential.
- Standard chemical potential.

### Phase transition properties
- Melting point.
- Freezing point.
- Boiling point.
- Condensation temperature.
- Critical temperature.
- Critical pressure.
- Critical volume.
- Heat of fusion, if available.
- Heat of vaporisation, if available.
- Sublimation enthalpy, if available.

### Temperature-dependent thermodynamics
- Heat capacity as a function of temperature.
- Entropy as a function of temperature.
- Enthalpy as a function of temperature.
- Gibbs energy as a function of temperature.
- Vapour pressure as a function of temperature.
- Thermal decomposition behaviour.

### Numerical properties worth collecting

NIST provides the following useful reference values:

| Property | Reference value | Unit |
|---|---:|---|
| Molecular weight | 47.9982 | g/mol |
| Standard gas-phase enthalpy of formation | 142.67 | kJ/mol |
| Standard gas-phase entropy | 238.92 | J/(mol·K) |
| Boiling temperature | 161.3 | K |
| Fusion temperature | 80.7 | K |
| Critical temperature | Approximately 261.1 | K |

These values must be associated with their specific reference states, data sources and uncertainties. For example, the NIST phase-change values are reported with experimental uncertainty, and ozone can decompose during measurements. [NIST WebBook](https://webbook.nist.gov/cgi/cbook.cgi?ID=C10028156\&Mask=15\&utm_source=chatgpt.com)

Additional reference: [NIST Computational Chemistry Comparison and Benchmark Database](https://cccbdb.nist.gov/exp2x.asp?casno=10028156&charge=0&utm_source=chatgpt.com).

## F11 — Density and gas properties

Include:

- Molecular mass.
- Gas density.
- Gas density at specified temperature and pressure.
- Relative density to dry air.
- Relative density to oxygen.
- Relative density to nitrogen.
- Compressibility factor.
- Specific volume.
- Molar volume.
- Diffusion coefficient in air.
- Diffusion coefficient in oxygen.
- Viscosity.
- Thermal conductivity.
- Specific heat ratio.
- Gas expansion behaviour.
- Real gas behaviour.
- Ideal gas approximation.
- Pressure dependence.
- Temperature dependence.

Crucially, distinguish calculated ideal-gas density from experimentally measured real-gas density.

## F12 — Solubility and partitioning

Include:

- Water solubility.
- Solubility in pure water.
- Solubility in saline water.
- Solubility in aqueous solutions.
- Solubility in organic solvents.
- Solubility in nonpolar solvents.
- Solubility in polar solvents.
- Henry's law constant.
- Henry's law coefficient.
- Gas–liquid partition coefficient.
- Ostwald solubility coefficient.
- Gas–liquid equilibrium.
- Temperature dependence.
- Pressure dependence.
- Salinity dependence.
- pH dependence where relevant.
- Solvent composition dependence.
- Dissolution rate.
- Desorption behaviour.

For Henry's law, store the exact convention and units. Different databases use reciprocal forms of the constant.

## F13 — Spectroscopic properties

### Ultraviolet-visible spectroscopy
- UV absorption spectrum.
- Visible absorption spectrum.
- Absorption maxima.
- Absorption cross-section.
- Absorption coefficient.
- Molar absorptivity.
- Wavelength dependence.
- Temperature dependence.
- Pressure dependence.
- Electronic transitions.
- Photodissociation thresholds.
- Photolysis quantum yields.

### Infrared spectroscopy
- Infrared absorption spectrum.
- Vibrational frequencies.
- Symmetric stretching mode.
- Asymmetric stretching mode.
- Bending mode.
- Vibrational energy levels.
- IR activity.
- Absorption intensity.

### Microwave and rotational spectroscopy
- Rotational spectrum.
- Rotational constants.
- Rotational transitions.
- Dipole moment.
- Rotational energy levels.

### Raman spectroscopy
- Raman activity.
- Raman shifts.
- Raman intensity.
- Vibrational modes.

### Other spectroscopy
- Photoelectron spectroscopy.
- Electron-impact ionisation.
- Mass spectrometry.
- Electron paramagnetic resonance, where relevant.
- High-resolution spectroscopy.

Link actual spectral datasets, not just descriptive statements.

---

# 5. Chemical properties and behaviour

## F14 — General chemical properties

Include:

- Chemical reactivity.
- Oxidising character.
- Oxidation potential.
- Electron-accepting behaviour.
- Electrophilic character.
- Reaction selectivity.
- Reaction kinetics.
- Reaction rate.
- Chemical stability.
- Decomposition behaviour.
- Redox behaviour.
- Reaction thermodynamics.
- Reaction pathways.
- Radical chemistry.
- Ionic reaction pathways.
- Molecular reaction pathways.
- Reaction intermediates.

### Chemical classification
- Strong oxidising agent.
- Molecular oxidant.
- Electrophilic reactant.
- Reactive oxygen species.
- Thermodynamically unstable relative to oxygen under standard conditions.

Explain the distinction between thermodynamic favourability and reaction kinetics.

## F15 — Oxidation-reduction properties

Include:

- Oxidation-reduction potential.
- Standard reduction potential.
- Half-reaction.
- Electron acceptance.
- Oxidation reactions.
- Reduction reactions.
- Redox couples.
- pH dependence.
- Temperature dependence.
- Solvent dependence.
- Standard conditions.
- Nonstandard conditions.
- Direct oxidation.
- Indirect oxidation.
- Reaction selectivity.
- Oxidation products.

A particularly important point:

Do not give ozone one universal oxidation potential without identifying the redox couple, reaction conditions, pH and reference electrode.

Store individual half-reactions and their potentials as separate records.

## F16 — Chemical reactions

Create a reaction database with the following categories.

### Reactions involving oxygen
- Ozone formation from molecular oxygen.
- Ozone photodissociation.
- Ozone thermal decomposition.
- Ozone reaction with atomic oxygen.
- Ozone reaction with oxygen-derived species.

### Reactions involving hydrogen
- Reactions with hydrogen-containing compounds.
- Reactions with hydroxyl species.
- Reactions with hydrogen peroxide.
- Radical chain reactions involving hydrogen-containing species.

### Reactions involving inorganic substances
- Reactions with nitrogen oxides.
- Reactions with sulphur compounds.
- Reactions with halides.
- Reactions with metals.
- Reactions with metal ions.
- Reactions with inorganic anions.
- Reactions with inorganic reducing agents.

### Reactions involving organic substances
- Alkene oxidation.
- Alkene ozonolysis.
- Alkane oxidation, where applicable.
- Aromatic compound oxidation.
- Aldehyde oxidation.
- Ketone reactions.
- Alcohol oxidation.
- Phenol oxidation.
- Amine reactions.
- Sulphur-containing organic compound reactions.
- Unsaturated fatty acid ozonolysis.

### Reaction data points for every reaction
- Reaction identifier.
- Reactants.
- Products.
- Reaction equation.
- Balanced equation.
- Reaction type.
- Reaction mechanism.
- Reaction conditions.
- Temperature.
- Pressure.
- pH.
- Solvent.
- Catalyst.
- Reaction rate constant.
- Reaction order.
- Activation energy.
- Enthalpy change.
- Gibbs energy change.
- Reaction selectivity.
- Reaction yield.
- Intermediate species.
- Side products.
- Scientific reference.

## F17 — Ozonolysis

This is important enough to have a dedicated subsection within the chemistry chapter.

Include:

- Definition of ozonolysis.
- Mechanism of ozonolysis.
- Reactant classes.
- Alkene reactions.
- Carbon–carbon double bond cleavage.
- Initial ozone addition.
- Primary ozonide formation.
- Criegee intermediates.
- Carbonyl oxide formation.
- Secondary ozonide formation.
- Carbonyl product formation.
- Reductive work-up.
- Oxidative work-up.
- Reaction selectivity.
- Reaction conditions.
- Solvent effects.
- Temperature effects.
- Mechanistic variations.
- Atmospheric ozonolysis.
- Synthetic organic ozonolysis.

## F18 — Chemical stability and decomposition

Include:

- Thermodynamic stability.
- Kinetic stability.
- Decomposition rate.
- Decomposition pathways.
- Thermal decomposition.
- Photochemical decomposition.
- Catalytic decomposition.
- Homogeneous decomposition.
- Heterogeneous decomposition.
- Surface-catalysed decomposition.
- Radical-mediated decomposition.
- Metal-catalysed decomposition.
- Moisture effects.
- Temperature effects.
- Pressure effects.
- Concentration effects.
- Surface material effects.
- Impurity effects.
- Container effects.
- Half-life.
- Lifetime.
- Decomposition products.

A critical distinction:

Ozone is thermodynamically unstable relative to molecular oxygen, but its decomposition rate depends strongly on its environment.

Therefore, never assign ozone one universal half-life.

## F19 — Chemical compatibility

Represent interactions between ozone and different material classes:

- Metals.
- Metal alloys.
- Polymers.
- Elastomers.
- Ceramics.
- Glass.
- Organic materials.
- Inorganic materials.
- Lubricants.
- Oils.
- Solvents.
- Coatings.
- Building materials.

For each interaction, record:

- Material.
- Ozone phase.
- Ozone concentration.
- Temperature.
- Exposure duration.
- Moisture.
- Reaction type.
- Degradation mechanism.
- Reaction products.
- Compatibility rating.
- Experimental evidence.
- Reference.

This will also provide reusable data for your later engineering and safety articles.

---

# 6. Formation, decomposition and fundamental ozone chemistry

## F20 — Ozone formation

Explain the general formation reaction:

\[
O_2 + O \rightarrow O_3
\]

In practice, the reaction requires a third body to carry away excess energy:

\[
O + O_2 + M \rightarrow O_3 + M
\]

Represent:

- Molecular oxygen as a precursor.
- Atomic oxygen as a precursor.
- Third-body collision partner.
- Energy transfer.
- Formation reaction.
- Reaction rate coefficient.
- Temperature dependence.
- Pressure dependence.
- Formation efficiency.
- Competing reactions.
- Reaction environment.
- Product formation.

Include formation through:

- Ultraviolet photochemistry.
- Electrical discharge.
- Corona discharge.
- Dielectric barrier discharge.
- Electrochemical processes.
- Photochemical laboratory methods.
- Natural atmospheric processes.

The detailed engineering methods can be developed in your later generation article.

## F21 — Ozone decomposition

Represent the fundamental reaction:

\[
2O_3 \rightarrow 3O_2
\]

Also include the elementary pathways involved in decomposition, rather than treating this overall reaction as the only mechanism.

Data points:

- Decomposition reaction.
- Reactant ozone.
- Product oxygen.
- Reaction enthalpy.
- Reaction free energy.
- Reaction mechanism.
- Elementary reaction steps.
- Reaction intermediates.
- Catalysts.
- Surface effects.
- Thermal effects.
- Photochemical effects.
- Rate constants.
- Activation energy.
- Reaction order.
- Temperature dependence.
- Pressure dependence.

## F22 — Fundamental ozone reaction mechanisms

Include:

- Radical chain reactions.
- Photochemical reactions.
- Electron-transfer reactions.
- Electrophilic addition.
- Electrophilic oxidation.
- Ozonolysis.
- Oxygen atom transfer.
- Direct molecular oxidation.
- Indirect oxidation.
- Radical-mediated oxidation.
- Catalytic reaction pathways.
- Surface reactions.
- Homogeneous gas-phase reactions.
- Aqueous-phase reactions.

For each mechanism, store:

- Mechanism name.
- Reactants.
- Intermediate species.
- Transition states, where known.
- Products.
- Elementary steps.
- Rate constants.
- Activation energies.
- Mechanistic evidence.
- Conditions.
- References.

---

# 7. Isotopes and isotopic variations

## F23 — Oxygen isotopes in ozone

Include:

- Oxygen-16.
- Oxygen-17.
- Oxygen-18.
- Isotopic abundance of constituent oxygen.
- Isotopic composition.
- Isotopologues.
- Symmetry of isotopologues.
- Isotopic substitution.
- Isotopic mass.
- Isotopic effects on vibrational frequencies.
- Isotopic effects on rotational spectra.
- Isotopic effects on reaction rates.
- Isotopic fractionation.
- Mass-independent isotope fractionation.
- Isotopic signatures.
- Isotope exchange reactions.
- Isotope-specific spectroscopic data.

Also distinguish:

- Symmetric ozone isotopologues.
- Asymmetric ozone isotopologues.
- Homonuclear ozone.
- Mixed-isotope ozone.

Do not treat all ozone molecules as having exactly the same isotopic mass.

---

# 8. Natural occurrence and fundamental distribution

This section should be an introduction, not a full atmospheric science chapter.

## F24 — Natural occurrence

Include:

- Natural occurrence in Earth's atmosphere.
- Occurrence in the stratosphere.
- Occurrence in the troposphere.
- Natural atmospheric formation.
- Natural atmospheric destruction.
- Natural background concentrations.
- Presence in other planetary atmospheres.
- Detection in extraterrestrial environments, where established.
- Laboratory occurrence.
- Natural versus anthropogenic formation.
- Atmospheric transport.
- Environmental conditions affecting occurrence.

You should also distinguish natural occurrence from natural safety: naturally occurring ozone can still be harmful.

---

# 9. Historical and scientific development

## F25 — History of ozone

Create a structured historical knowledge graph.

### Discovery
- Discovery of ozone.
- Discovering scientist.
- Christian Friedrich Schönbein.
- Discovery date.
- Discovery location.
- Experimental circumstances.
- Original terminology.
- Original observations.
- Historical publications.

### Scientific identification
- Recognition as a distinct chemical substance.
- Identification of its relationship with oxygen.
- Determination of molecular composition.
- Determination of molecular formula.
- Development of structural models.
- Discovery of atmospheric occurrence.
- Discovery of ultraviolet absorption.
- Development of ozone spectroscopy.

### Scientific milestones
- First ozone generation experiments.
- Early ozone chemistry.
- Molecular structure determination.
- Thermodynamic characterisation.
- Development of ozone measurement.
- Development of quantum chemical descriptions.
- Major theoretical advances.
- Important experimental breakthroughs.

### Historical source information
- Scientist.
- Institution.
- Publication.
- Publication year.
- DOI.
- Historical document.
- Scientific contribution.
- Discovery significance.
- Subsequent confirmation.

---

# 10. Scientific models and theories

## F26 — Models explaining ozone

Although the article is about ozone itself, it should introduce the main scientific models that explain its molecular behaviour.

Include:

- Lewis structure model.
- Resonance theory.
- Valence bond theory.
- Molecular orbital theory.
- VSEPR theory.
- Quantum mechanical model.
- Thermodynamic models.
- Statistical thermodynamics.
- Chemical kinetics.
- Transition state theory.
- Potential energy surfaces.
- Spectroscopic models.
- Molecular symmetry theory.

For every model, include:

- Model name.
- Scientific discipline.
- What it explains.
- Fundamental assumptions.
- Mathematical formulation.
- Applications to ozone.
- Limitations.
- Scientific references.

---

# 11. RDF modelling: how to represent the data properly

This is arguably the most important part of the entire project.

I would strongly recommend that you don't represent every fact as a simple subject–predicate–object triple when the fact has scientific qualifications.

For example, this is insufficient:

```turtle
:Ozone :hasBoilingPoint 161.3 .
```

It doesn't tell you:
- The unit.
- The pressure.
- The measurement method.
- The uncertainty.
- The reference.
- Whether this is an experimental or calculated value.

Instead, represent the property as a separate scientific observation.

### Recommended structure

```turtle
:Ozone
    rdf:type :ChemicalSubstance ;
    :hasMolecularFormula "O3" ;
    :hasCASNumber "10028-15-6" ;
    :hasMolarMass :OzoneMolarMass ;
    :hasBoilingPoint :OzoneBoilingPoint .

:OzoneMolarMass
    rdf:type :MeasuredOrCalculatedProperty ;
    :numericalValue "47.9982"^^xsd:decimal ;
    :unit :GramPerMole ;
    :dataSource :NIST .

:OzoneBoilingPoint
    rdf:type :ExperimentalProperty ;
    :numericalValue "161.3"^^xsd:decimal ;
    :unit :Kelvin ;
    :measurementUncertainty "0.5"^^xsd:decimal ;
    :dataSource :NIST ;
    :referenceCondition :ReportedExperimentalConditions .
```

The classes and predicates here are illustrative custom vocabulary terms.

## 11.1 Essential metadata for every numerical property

Every numerical scientific fact should ideally have:

| Field | Purpose |
|---|---|
| Subject | Substance or property being described |
| Property | What is being measured |
| Value | Numerical value |
| Unit | Measurement unit |
| Quantity kind | Mass, temperature, energy, pressure, etc. |
| Conditions | Temperature, pressure, pH, etc. |
| Method | Experimental or computational method |
| Uncertainty | Measurement uncertainty |
| Reference | Original source |
| Publication date | When the source was published |
| Retrieval date | When you accessed it |
| Data status | Measured, calculated, estimated or theoretical |
| Applicability | Conditions under which the value applies |
| Confidence | Evidence quality |
| Notes | Additional qualifications |

This is essential because scientific databases sometimes report different values for the same property.

For instance, the NIST WebBook and NIST Computational Chemistry Comparison and Benchmark Database report different reference values for certain ozone thermodynamic properties. Your system should preserve both records rather than arbitrarily selecting one. [NIST WebBook](https://webbook.nist.gov/cgi/cbook.cgi?ID=C10028156\&Mask=15\&utm_source=chatgpt.com)

## 11.2 RDF vocabularies worth using

Don't reinvent everything.

Reuse established vocabularies wherever possible:

| Vocabulary | Purpose |
|---|---|
| RDF | Fundamental triple representation |
| RDFS | Classes, properties and hierarchies |
| OWL | Ontology relationships and logical definitions |
| SKOS | Terminology, synonyms and classifications |
| Dublin Core | Metadata and documentation |
| PROV-O | Data provenance and source history |
| QUDT | Quantities, units and dimensions |
| CHEBI | Chemical entities |
| SIO | Scientific measurement and investigation concepts |
| Schema.org | Web publishing metadata |

Useful specifications:

- [W3C RDF 1.1](https://www.w3.org/TR/rdf-concepts/?utm_source=chatgpt.com)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/?utm_source=chatgpt.com)
- [ChEBI Chemical Ontology](https://www.ebi.ac.uk/chebi/?utm_source=chatgpt.com)
- [QUDT Ontologies](https://qudt.org/?utm_source=chatgpt.com)
- [W3C SKOS](https://www.w3.org/TR/skos-reference/?utm_source=chatgpt.com)

I would use CHEBI to identify the chemical entity and your own ontology to describe the comprehensive subject-specific knowledge surrounding ozone.

---

# 12. Additional relationships you should create

Your RDF dataset shouldn't just contain isolated properties. It should connect concepts.

For example:

### Chemical identity relationships

- Ozone is an allotrope of oxygen.
- Ozone is composed of oxygen atoms.
- Ozone has a molecular formula.
- Ozone has a molecular structure.
- Ozone has a molecular geometry.
- Ozone has a molar mass.
- Ozone has a chemical identifier.

### Molecular structure relationships

- Molecular structure determines molecular geometry.
- Molecular geometry is characterised by bond angles.
- Molecular geometry is characterised by bond lengths.
- Molecular bonding involves electron distribution.
- Electron distribution contributes to molecular polarity.
- Molecular symmetry influences spectroscopic properties.

### Chemical behaviour relationships

- Ozone undergoes chemical reactions.
- Ozone participates in oxidation reactions.
- Ozone can undergo decomposition.
- Ozone can undergo photolysis.
- Ozone reacts with organic substances.
- Ozone reacts with inorganic substances.
- Ozone has a chemical lifetime.
- Ozone stability depends on environmental conditions.

### Physical behaviour relationships

- Ozone exists in different physical phases.
- Physical phase depends on temperature and pressure.
- Ozone has a characteristic density.
- Ozone has a characteristic vapour pressure.
- Ozone has measurable solubility.
- Ozone absorbs electromagnetic radiation.
- Ozone has characteristic spectroscopic properties.

### Scientific knowledge relationships

- A scientific publication reports a property.
- A scientist discovered or characterised ozone.
- An experiment measured a property.
- A scientific model explains a phenomenon.
- A measurement supports a scientific conclusion.
- A reference provides evidence for a claim.
- A later publication revises an earlier scientific interpretation.

These relationships are particularly valuable when generating articles automatically because they allow you to generate explanations, not merely lists of properties.

---

# 13. Recommended article structure generated from the RDF

Once your dataset is populated, I would generate the Fundamentals article in this order:

| Article section | RDF domains |
|---|---|
| 1. Introduction to ozone | F01, F02 |
| 2. Chemical identity | F01, F02, F03 |
| 3. Chemical composition | F04 |
| 4. Molecular structure | F05, F06 |
| 5. Molecular geometry | F07 |
| 6. Intrinsic molecular properties | F08 |
| 7. Physical properties | F09, F11 |
| 8. Thermodynamic properties | F10 |
| 9. Spectroscopic properties | F13 |
| 10. Chemical properties | F14, F15 |
| 11. Chemical reactions | F16, F17 |
| 12. Ozone formation | F20 |
| 13. Ozone decomposition | F21 |
| 14. Chemical stability | F18 |
| 15. Solubility and interactions | F12, F19 |
| 16. Isotopes | F23 |
| 17. Natural occurrence | F24 |
| 18. History of ozone | F25 |
| 19. Scientific models | F26 |
| 20. References and further reading | Provenance data |

This would produce a substantial scientific reference article rather than a basic introductory explanation.

---

# 14. What I would add to make the dataset genuinely exhaustive

There are five additional things I'd implement.

### A. Negative knowledge

Record scientifically important things that ozone is *not*.

For example:

- Ozone is not molecular oxygen.
- Ozone is not atomic oxygen.
- Ozone is not a chemical compound containing different elements.
- Ozone is not a free radical in its electronic ground state.
- Ozone is not a persistent molecule under all environmental conditions.
- Ozone is not synonymous with the ozone layer.

This helps prevent inaccurate automatically generated explanations.

### B. Scientific disagreements

Allow multiple sources to report different values or interpretations.

For every conflicting property, store:

- Reported value A.
- Reported value B.
- Source A.
- Source B.
- Measurement method A.
- Measurement method B.
- Experimental conditions.
- Potential explanation for disagreement.
- Whether a consensus value exists.

Never silently merge conflicting scientific data.

### C. Scientific explanations

Don't just record:

```turtle
:Ozone :hasBentGeometry true .
```

Also record:

- Why ozone has bent geometry.
- Which theory explains the geometry.
- How electron pairs influence molecular shape.
- How resonance influences bonding.
- How experimental measurements support the model.

This distinction between factual data and explanatory knowledge will substantially improve your generated article.

### D. Cross-domain relationships

Build connections to future articles:

- Ozone → atmospheric chemistry.
- Ozone → ultraviolet absorption.
- Ozone → oxidative stress.
- Ozone → water treatment.
- Ozone → oxidation reactions.
- Ozone → industrial generation.
- Ozone → environmental chemistry.
- Ozone → human health.

Your Fundamentals article should link to these subjects without trying to explain all of them in detail.

### E. Knowledge completeness tracking

For every domain, track:

- Required data points.
- Collected data points.
- Verified data points.
- Data points awaiting verification.
- Missing data points.
- Conflicting data points.
- Source coverage.
- Last review date.

This lets you measure actual progress instead of guessing whether the article is comprehensive.

---

# 15. My recommended implementation priorities

Although I've provided an enormous inventory, I wouldn't populate every domain simultaneously.

I'd build it in four stages.

| Stage | Domains | Priority |
|---|---|---|
| 1 | F01–F08 | Essential chemical identity and molecular science |
| 2 | F09–F13 | Physical, thermodynamic and spectroscopic properties |
| 3 | F14–F22 | Chemical behaviour, reactions and stability |
| 4 | F23–F26 | Isotopes, natural occurrence, history and scientific models |

I would also maintain a separate provenance graph throughout all four stages.

## My final recommendation

**Don't aim to collect the maximum possible number of triples. Aim to build the maximum scientifically meaningful representation of ozone.**

There is no finite list of literally all possible ozone triples: new experimental measurements, computational results, isotopologues, reaction conditions and scientific discoveries can continually create new knowledge.

What you can create is a comprehensive, extensible ontology with a defined scope and a rigorous data collection standard.

For this first article, I'd use the following acceptance criteria:

1. Every fundamental chemical identity claim is represented.
2. Every major molecular property is represented.
3. Every established physical property is represented.
4. Every important chemical behaviour is represented.
5. Every numerical value has a unit and source.
6. Every condition-dependent value has its conditions.
7. Every scientific explanation is connected to its underlying concepts.
8. Conflicting values are preserved and documented.
9. Every major claim has traceable provenance.
10. Every concept can be used to generate a coherent section of the article.

**One architectural decision I'd make before collecting any data:** establish your RDF ontology, naming conventions, measurement model and provenance structure first. Otherwise, you'll end up with thousands of triples that are difficult to query, validate and turn into consistently written scientific articles.
