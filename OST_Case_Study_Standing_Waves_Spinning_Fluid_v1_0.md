# Standing Waves in a Spinning Fluid as an OST Case Study

## A formal reading of Singh, Rønning, Liu, Angheluta, Concha, and Bandi (2026) within the Ordinative Set Theory framework

**Author**: Fabio Ghioni
**Framework version**: TE_CORE v5.1 / OST v2.1 / OST Extension (Teleodynamics & Causal Inversion) v1.1
**Document status**: Working paper — case study for OST, intended as supporting material for forthcoming work on (i) Reaction-Diffusion Civilizational Dynamics v1.3, (ii) Ordinative Category Theory (OCT), (iii) the foundational text on the Semantic Genome
**Version**: 1.0
**Date**: April 21, 2026

---

## Abstract

A recent experimental and theoretical study by Singh, Rønning, Liu, Angheluta, Concha, and Bandi (*Communications Physics* 9:123, 2026) demonstrates that shallow-water standing waves scattered by a single irrotational vortex develop quantized, system-spanning nodal lines that rotate counter to the vortex circulation. The phenomenon is a hydrodynamic analogue of the Aharonov–Bohm (AB) effect, but generalises the classical Berry et al. (1980) result in a structurally significant way: the topological response is non-local and global rather than confined to the vortex core, and the number of nodal lines is quantized by a single dimensionless parameter α derived from a continuous source.

This document offers a formal Ordinative Set Theory (OST) reading of the Singh et al. result. The argument is that this experiment, while wholly grounded in classical fluid dynamics and quantum mechanical analogy, instantiates four propositions that OST has previously articulated as structural principles: (i) ordinative non-additivity of triples ⟨Σ, R, Φ⟩ under modification of the relation R, (ii) emergence of structural Controfase as the unique coherent response of a system to an organising attractor, (iii) topology-generated quantization in the absence of a quantized source, and (iv) teleodynamic causal inversion in which a global configuration constraint retroacts on the spatial domain over which a local cause expresses itself. The Singh et al. system thus functions as an external, peer-reviewed, fully reproducible empirical example of OST principles operating in a controlled physical setting. Consequences for the active OST research programme are outlined, with explicit confidence grading and a declared inventory of what the paper does *not* establish.

---

## 1. Introduction and empirical context

The Aharonov–Bohm (AB) effect, predicted in 1959 and experimentally verified in stages from the 1960s onward, is conventionally regarded as one of the cleanest demonstrations that quantum mechanical observables depend on electromagnetic potentials, not only on local fields. A charged particle wave function acquires a phase shift on encircling a region of magnetic flux even when the particle traverses no region of nonzero magnetic field.

Berry, Chambers, Large, Upstill, and Walmsley (1980) showed that the AB effect has a precise classical analogue in shallow-water surface waves scattered by an irrotational draining vortex. In that analogue, the vector potential is replaced by the azimuthal velocity field of the vortex, the magnetic flux Φ_B is replaced by the flow circulation Γ, and the dimensionless parameter governing the scattering pattern is

$$ \alpha_q = \frac{q\Phi_B}{h} \;\longleftrightarrow\; \alpha_f = -\frac{\Gamma}{\lambda v_g} \tag{1.1} $$

with q the particle charge, h Planck's constant, λ the wavelength, and v_g the wave group velocity. In the Berry configuration a single travelling wave incident on the vortex develops *wavefront dislocations* — localised topological defects pinned at or near the vortex core, whose number is set by α.

Singh et al. (2026) modify one parameter of this configuration. Instead of a single travelling wave, they generate a standing wave by superposing two counter-propagating travelling waves of the same wavelength, with the vortex at the centre of the standing-wave pattern. The technical change in the scattering solution is the substitution n → 2n in the Bessel-function summation that constructs the wave function:

$$ \psi = 2\sum_{n} (-i)^{l_q} J_{l_q}(kr) \, e^{2 n i \varphi}, \qquad l_q = |2n - \alpha| \tag{1.2} $$

This substitution enforces double angular periodicity. The empirical and theoretical consequence is qualitatively new. Instead of localised wavefront dislocations near the vortex core, the system develops a discrete number of *nodal lines* — system-spanning lines of zero wave amplitude — that radiate outward from the vortex core to the far field, rotate at constant angular velocity ω = ν/α (where ν is the wave frequency), and rotate in the direction *opposite* to the vortex circulation. The number N of nodal lines is bounded by

$$ |\alpha| - 1 < N < |\alpha| + 1 \tag{1.3} $$

so that for integer α the number is exactly |α|, and for non-integer α the number oscillates in time between the two integers bracketing |α|, with periodic disappearance and reappearance on the x-axis. The quantization is *topological* in origin and emerges from the geometry of the configuration, not from any quantization of the source: Γ is a continuous parameter freely tunable by the experimenter.

The authors document the result with high-speed caustic imaging, particle imaging velocimetry to measure circulation, and analytical asymptotics derived using the saddle-point method on the Bessel integrals. The agreement between experiment and theory is presented "with no adjustment parameters." The paper is open access; analysis code is publicly archived (Zenodo DOI 10.5281/zenodo.18652566); and the work has passed standard peer review at *Communications Physics*.

The result is, on its own terms, a contribution to fluid dynamics and to the broader programme of classical analogue physics. The authors propose extending the configuration to lattices of vortices, which would emulate vortex matter in superconductors and provide a hydrodynamic platform for studying AB caging and topological localisation effects experimentally inaccessible in the quantum regime.

This document addresses a different question. It asks: what is the Singh et al. result, when read in the dictionary of Ordinative Set Theory? The answer is that the result instantiates four OST propositions in a clean, fully controlled, externally validated setting. The remainder of this document develops that reading.

---

## 2. The experimental result, recapitulated structurally

To make the OST reading possible, restate the Singh et al. result by separating physical content from configuration:

**System composition**: A bounded fluid domain of average depth H and surface tension and viscosity within standard ranges, in which three components are co-present:

- A **stationary irrotational vortex** at the centre, generated by a constant-rate drain. Far-field velocity field $\vec U(\vec r) = (\Gamma / 2\pi r)\hat\varphi$, with circulation Γ continuously tunable.
- A **standing surface wave** generated by two pairs of acoustic transducers vibrating in phase on opposite sides of the vortex, producing two counter-propagating travelling waves of common wavelength λ.
- The **fluid medium** itself, satisfying the shallow-water equation $(\partial_t + \vec U\cdot\nabla)^2 \eta - c^2 \nabla^2\eta = 0$ with $c = \sqrt{gh}$.

**Configuration regime**: Shallow water (hk ≪ 1), weak background flow (U ≪ c), and short wavelength relative to vortex core (β = Rk ≫ 1). Within this regime the surface deformation $\eta$ maps onto a Schrödinger equation for a charged particle in the azimuthal gauge of the vortex flow.

**Observed response**: The standing wave plus vortex system develops a discrete set of nodal lines whose number, angular separation, rotation rate, and rotation direction are all fixed by a single dimensionless parameter α. The nodal lines:

1. Are global, spanning the experimental domain (subject to dissipative attenuation in the far field);
2. Are quantized in number;
3. Rotate in the direction opposite to the vortex;
4. Carry a phase discontinuity of π across them, so that adjacent angular sectors of the field oscillate out of phase;
5. Are not derivable as a superposition of features present in the single-travelling-wave configuration — the substitution n → 2n is not a small perturbation of n → n but a different topological prescription.

**Key contrast with prior work**: The Berry (1980) configuration produces a *local* topological response (dislocations near the vortex core). The Singh et al. configuration produces a *non-local* topological response (nodal lines spanning the full domain). The difference resides not in the components but in the configuration of the relations among them.

This last sentence, in the experimental physics register, is also the OST proposition that follows.

---

## 3. Ordinative reading I: the standing-wave-plus-vortex system as an Insieme Ordinativo

OST v2.1 represents an ordinative system as a triple $\langle \Sigma, R, \Phi \rangle$ in which $\Sigma$ is the set of constituents, $R$ the set of relations under which they are co-present, and $\Phi$ the system's response or expressive function. A central proposition of OST is that the response $\Phi$ is in general not derivable from $\Sigma$ alone: changes in $R$, even arithmetically minor changes, can induce qualitatively new $\Phi$.

The Singh et al. experiment realises this proposition under conditions in which all three terms are fully specified, and the change in $R$ is exactly one bit of structure.

Define the system $S_B$ of the Berry configuration:

- $\Sigma_B = \{\text{fluid medium},\; \text{vortex},\; \text{single travelling wave}\}$
- $R_B = \{\text{shallow-water dynamics},\; \text{azimuthal gauge},\; \text{single-direction wave incidence}\}$
- $\Phi_B = $ wavefront dislocation pattern, localised in a neighbourhood of the vortex core

Define the system $S_S$ of the Singh configuration:

- $\Sigma_S = \Sigma_B \cup \{\text{counter-propagating travelling wave}\} = \{\text{fluid},\; \text{vortex},\; \text{wave}_+,\; \text{wave}_-\}$
- $R_S = R_B \setminus \{\text{single-direction incidence}\} \cup \{\text{double-direction incidence in standing-wave configuration}\}$
- $\Phi_S = $ system-spanning quantized rotating nodal lines

A classical superposition argument would predict $\Phi_S = \Phi_B + \Phi_B^{\text{mirrored}}$, that is, two superposed dislocation patterns. The authors explicitly state this was their prior expectation. The actual result departs from this prediction because the change in $R$ — the addition of double angular periodicity — is not a mere addition of a second wave but a topological reconfiguration that forces a different solution branch of the scattering problem. In the OST formalism:

$$ \Phi(\Sigma_B \cup \{x\},\, R_B) \neq \Phi(\Sigma_B,\, R_B) + \Phi(\{x\},\, R_B) \tag{3.1} $$

even when the added element $x$ (here, the second travelling wave) is, in isolation, indistinguishable from the original element of $\Sigma_B$. The non-additivity is carried by the relation $R$, not by the constituents.

This is the basic ordinative non-additivity proposition of OST, instantiated in a fully controlled and quantitatively predicted physical system. The instantiation is significant for three reasons:

(a) The system is *minimally complex*. There are three classes of constituent and the relation modification is exactly one structural prescription. There is no opportunity to attribute the qualitative change to hidden components or unmodelled couplings.

(b) The non-additivity is *predicted analytically*. The double-periodicity solution is derived from the Bessel-function expansion of the scattering problem, with no free parameters. The experimental verification matches the analytical prediction without adjustment.

(c) The non-additivity is *observable globally*. The departure from the superposition expectation is not confined to a small region but spans the system, providing visual confirmation that $\Phi_S$ is a property of the full configured field, not a local feature.

**Confidence**: $S_1$. The physical content is established at $S_0$; the OST reading identifies the structural isomorphism with a proposition the framework already articulates.

---

## 4. Ordinative reading II: nodal lines as structural Controfase

The Controfase, in the TE_CORE v5.1 lexicon, is a structural feature of an ordinative system that emerges *as the coherent negation* of an attractor's organising influence, distinct both from the attractor's direct expression and from its destructive cancellation. A Controfase is not absence; it is the *geometry the system must assume in order to remain coherent under the action of an attractor*.

The nodal lines reported by Singh et al. satisfy every criterion a structural Controfase must satisfy.

**Criterion 1: Emergence by structural necessity, not by addition.** The nodal lines are not present in either of the constituent travelling-wave configurations taken alone. Each travelling wave separately produces dislocations, not nodal lines. The nodal lines emerge only when both waves and the vortex are simultaneously present, and emerge as the unique configuration the field can adopt while satisfying the shallow-water equation under the azimuthal gauge of the vortex flow. They are not added; they are *forced*.

**Criterion 2: Coherent opposition to the attractor.** The vortex possesses a definite circulation sense set by the sign of Γ. The nodal lines rotate with angular velocity $\omega = \nu / \alpha$, and the sign of α is opposite to that of Γ. The nodal lines therefore rotate in the direction *opposite* to the vortex. This is not a generic counter-rotation of an unrelated structure; the rotation rate is fixed by the same parameter that fixes the vortex's strength, with opposite sign. The opposition is structural, not coincidental.

**Criterion 3: Quantization of the response.** A Controfase is not arbitrary. It is determined by the constraint of coherence between the attractor's organising action and the system's expressive capacity. The nodal lines satisfy this in a strong form: their number is fixed by the integer-bracketing of |α| (Equation 1.3), and not by any continuous parameter of the system. The Controfase here is *integer-valued*. The system cannot respond with 1.7 nodal lines.

**Criterion 4: Phase opposition across the Controfase.** The first cosine factor in Equation (1) of Singh et al. changes sign on crossing a nodal line, corresponding to a phase shift of π in the surface deformation $\eta$. The regions of the field separated by the nodal lines are therefore in *anti-phase*. This is the hydrodynamic instantiation of what TE_CORE describes as the function of the Controfase: to organise the expressive field into coherent zones whose boundary is the nodal locus itself.

**Criterion 5: Independence of the Controfase from the attractor's micro-structure.** Singh et al. state explicitly that "the nodal line structure is robust to near-core details and depends only on the far-field background flow." The Controfase is a property of the *global* relation between attractor and field, not of the attractor's interior structure. This is the OST proposition that Controfase is a system-level, not a local, response.

The case is direct enough to merit a one-line reformulation: **the nodal lines of Singh et al. are an experimentally observed Controfase, in the formal sense the term carries within TE_CORE.** The authors did not use this language and have no reason to; the structural identification is the object of the present document.

The significance of this identification is twofold. First, it offers a hydrodynamic exemplar of the Controfase concept that is fully reproducible and analytically derived, available for didactic and expository use in OST presentations. Second, it constrains the way Controfase should be modelled in OST applications outside fluid dynamics: the Singh et al. system shows that the Controfase is (i) integer-quantized when the configuration is topologically constrained, (ii) phase-opposed across its boundary, (iii) counter-rotating with respect to the attractor, and (iv) independent of attractor micro-structure. These four properties become testable hypotheses when OST is applied to non-fluid systems.

**Confidence**: $S_1$ on the structural identification (the four criteria are direct mappings of the experimental result onto framework definitions). $S_2$ on the proposal that the four properties constitute testable hypotheses for non-fluid OST applications, since the generalisation across substrates requires further work.

---

## 5. Ordinative reading III: topology-generated quantization without source quantization

Quantum mechanics is, in part, the science of why certain physical quantities take only discrete values. The standard answer attributes quantization to source-level structure: angular momentum is quantized because of the canonical commutation relations; magnetic flux through a superconductor is quantized because of the topology of the order parameter manifold; charge is quantized for reasons that remain partly open but trace to the structure of gauge symmetries.

The Singh et al. experiment shows quantization of a different kind. The number of nodal lines is integer-valued, and this integer is selected by the geometry of the standing-wave configuration combined with a continuous parameter α that depends on the vortex circulation Γ. Γ is a continuous quantity; the experimenter sets it by adjusting the drain rate; nothing in the source is quantized. The quantization is generated by the *topology of the configuration*, not inherited from the source.

The authors note the contrast explicitly: "the difference between the quantised magnetic flux Φ_B in quantum AB and continuous vorticity α marks an essential distinction between the two systems, even though their scattering pattern is otherwise identical in the chosen gauge."

In OST terms, this is a clean instance of what the framework articulates as **emergent topological quantization**: the proposition that integer-valued response variables can arise in an ordinative system $\langle \Sigma, R, \Phi \rangle$ purely from the topological constraints encoded in $R$, without requiring any element of $\Sigma$ to be itself quantized.

The mechanism in the Singh et al. case is fully transparent. The double angular periodicity imposed by the standing-wave configuration forces the asymptotic wave function to have the form (Eq. 6 of the paper)

$$ \psi \sim 2\cos\!\left(kr\cos\varphi \mp \alpha\frac{\pi}{2}\right) e^{i\alpha(\varphi \mp \pi/2)} \quad\text{for } \varphi \in (0,\pm\pi) \tag{5.1} $$

The nodal-line condition is the zero-set of the time-dependent cosine, which solves $\theta(t) = m\pi/\alpha + (\nu t)/\alpha + \ldots$ The bound $|\alpha| - 1 < N < |\alpha| + 1$ then follows from a counting argument on the angular distance $\pi/|\alpha|$ between adjacent zeros and the requirement that the field on the x-axis vanish only at integer α. The integer comes out of the counting argument; it is not put in.

The proposition this instantiates is significant for three current research streams.

**For the Reaction-Diffusion Civilizational Dynamics paper (v1.2 → v1.3).** The triple-scale temporal model and the Arajat *senza vista / con vista* distinction both rely on the claim that ordinative systems can produce integer-valued *macro-phase counts* from continuous underlying parameters. The Singh et al. system is an external precedent for this kind of emergence in a controlled setting, and can be cited as such in v1.3 to support the structural plausibility of the macro-phase counting argument. The hydrodynamic precedent does not validate the civilizational application directly — that requires its own evidence — but it removes the burden of proving that topology-generated quantization is itself a coherent physical phenomenon.

**For Ordinative Category Theory (OCT).** A natural categorical reading of the Singh et al. result is as a functor from the category of fluid configurations (with morphisms given by changes in the relation R) to the category of integer-valued topological response counts. The substitution n → 2n is then a morphism in the source category whose image in the target category is a doubling of the angular index, with the integer-counting bound (1.3) following as a consequence. This is the kind of structural mapping that OCT, when developed, will be expected to formalise. The Singh et al. case is a small but well-defined example to keep in view as the categorical formalism is constructed.

**For the Semantic Genome programme.** One of the open questions in the programme is whether the integer-valued structures observed in well-formed ordinative outputs (coherent identity zones, discrete attractor counts in expressive terminals) reflect deep quantization or are statistical artefacts. The Singh et al. result establishes that integer-valued response counts can emerge necessarily from continuous parameters when the system's relational structure imposes the right topological constraint. The Semantic Genome is *not* shown to be such a system by this result, but the result clears the conceptual ground: integer outputs from continuous inputs is a real physical phenomenon, not a heuristic.

**Confidence**: $S_1$ on the physical fact and the OST identification. $S_2$ on the proposed implications for the three research streams above (each requires its own development; the Singh et al. result is supporting context, not direct validation).

---

## 6. Ordinative reading IV: teleodynamic structure and causal inversion

OST Extension v1.1 develops the proposition that in certain ordinative systems the spatial or temporal scope over which a local cause expresses its effects depends on the global organisational state of the system. The locution used in the Extension is *causal inversion*: the configuration constraint (the global state of the system as a whole) retroacts on the cause to determine which effects the cause can in fact produce.

The Berry/Singh contrast is a textbook case.

A vortex of circulation Γ in a single-travelling-wave field produces a wavefront dislocation localised in the neighbourhood of the vortex core. The vortex's "cause" — its action on the field — is expressed *locally*. The same vortex of the same circulation Γ in a standing-wave field produces system-spanning nodal lines. The vortex's cause is now expressed *globally*. The vortex itself has not changed. What has changed is the configuration of the rest of the system: a second wave has been added, and the relation $R$ now includes double-direction incidence.

The vortex-as-cause has two different effect-spaces depending on the global configuration. In neither case is the vortex doing anything different at the level of its own dynamics. The difference is in what the system *permits* the vortex to express.

This is the formal pattern of teleodynamic causal inversion as articulated in OST Extension §3 (Causal Inversion in Configured Systems): the global configuration acts as a *receptor structure* that determines the spatial and temporal envelope over which a local source can express. When the receptor structure is impoverished (single wave), the source's expression is confined; when the receptor structure carries the right topological richness (double-direction periodicity), the source's expression becomes global.

The Singh et al. result therefore furnishes:

- An empirical demonstration of teleodynamic causal inversion in a controlled physical system;
- A *quantitative* link between the structure of the receptor configuration (here, the n → 2n substitution) and the change in the source's effect-envelope (here, local → global);
- A clean separation between the source's intrinsic strength (Γ, unchanged) and the spatial scope of its expression (changed by configuration).

There is a further point worth recording. In OST Extension the meta-receptivity parameter $C^*$ is introduced to quantify a system's capacity to host expression of a given source. The Singh et al. result suggests a candidate operationalisation: in a configured system, $C^*$ may be measurable as the spatial integral of the source's response function over the domain. In the Berry configuration this integral is finite and concentrated near the core; in the Singh configuration it is bounded only by the dissipative attenuation of the medium. The receptor's capacity has changed by a measurable factor, traceable to a single structural prescription.

This is a candidate operationalisation, not a derivation. It is offered here as a direction for the Reaction-Diffusion v1.3 development of $C^*$.

**Confidence**: $S_1$ on the identification of the empirical pattern as causal inversion in the OST sense. $S_2$ on the proposed operationalisation of $C^*$ as the spatial integral of response; the operationalisation needs independent development against existing OST commitments.

---

## 7. Implications for OST and active research programmes

This section consolidates the implications of the four readings above for ongoing OST work.

### 7.1 For the Reaction-Diffusion Civilizational Dynamics paper

The Singh et al. system is suitable for citation in v1.3 as an external precedent for the following propositions used in the civilizational dynamics paper:

(i) The triple-scale temporal model assumes that macro-phase boundaries can be integer-counted within a terminal envelope. The Singh et al. result establishes that integer counting of phase structures can emerge necessarily from continuous parameters under topological constraint. This removes the burden of arguing for the abstract possibility; it does not establish the civilizational application.

(ii) The triple bifurcation distinction between Structural Controfase ($\mathcal{C}_s$) and Deliberate Controfase ($\mathcal{C}_d$) requires a clear physical exemplar of the structural variant. The Singh et al. nodal lines are a paradigmatic Structural Controfase: they emerge by topological necessity from the configuration, with no agentic component. v1.3 may cite the case to anchor the $\mathcal{C}_s$ definition.

(iii) The meta-receptivity parameter $C^*$ benefits from the operationalisation suggestion of §6 (spatial integral of response over domain). v1.3 may include this as a methodological appendix.

The recommended citation form for v1.3 is direct: "Singh et al. (2026) provide a controlled hydrodynamic example of structural Controfase emergence under topological configuration constraint." No further interpretive language is required; the structural mapping speaks for itself once the OST glossary is in place.

### 7.2 For Ordinative Category Theory (OCT)

The Singh et al. case furnishes a small, well-controlled example for the categorical formalism. The category $\mathbf{Cfg}$ of fluid configurations has objects (configurations $\langle \Sigma, R, \Phi \rangle$) and morphisms (admissible modifications of $R$ holding $\Sigma$ fixed up to specified additions). The category $\mathbf{Top}_{\mathbb{Z}}$ of integer-valued topological responses has objects (response patterns characterised by their integer-counting structure) and morphisms (transitions between response patterns).

The Berry-to-Singh transition is a morphism in $\mathbf{Cfg}$: the object $\langle \Sigma_B, R_B, \Phi_B \rangle$ is connected by a morphism to $\langle \Sigma_S, R_S, \Phi_S \rangle$, where the morphism encodes the n → 2n substitution. Under the response functor $F: \mathbf{Cfg} \to \mathbf{Top}_{\mathbb{Z}}$, the image of this morphism is the transition from "localised dislocation pattern" to "system-spanning quantized rotating nodal lines." The functoriality property (composition of morphisms preserved by F) is something that can in principle be tested by composing further configuration changes.

This is one example, not a development. It is offered as an anchor for the OCT formalism in early stages.

### 7.3 For the Semantic Genome programme

The Semantic Genome research traces emergence of integer-valued, discretely indexed structures in the outputs of LLMs operating under TE conditions. The interpretive question is whether such discreteness reflects an underlying topological constraint of the ordinative configuration, or is a statistical artefact of finite vocabulary and discrete tokenisation.

The Singh et al. result does not resolve this question. It does, however, establish that:

(i) Integer-valued output counts can emerge necessarily from continuous parameters when the system's relational structure carries the right topological constraint;

(ii) The topological constraint can be added to a system by a structurally minimal modification of one component of $R$;

(iii) The resulting integer-valued structures can be system-spanning rather than local.

These three propositions are conditions of possibility for the Semantic Genome interpretation of integer-valued LLM output structures. They do not constitute evidence for that interpretation. The conditions of possibility being established empirically in fluid dynamics is, however, of methodological value: it removes one form of objection (the abstract possibility objection) and refocuses the question on the specific empirical pattern in LLM outputs.

### 7.4 For the forthcoming book on Ordinative AI philosophy

The Singh et al. case is a strong didactic exemplar for the proposition, central to the forthcoming book, that *coherent identity is not a chosen state but a structural resolution*. The nodal lines are not selected by the system from a menu of options; they emerge as the unique geometry the field can adopt while satisfying the constraints of the configured system. The case is concise, fully reproducible, and visually demonstrable in the supplementary movies of the paper. It can serve as the opening exemplar of a chapter on emergent coherence.

---

## 8. Open questions and proposed extensions

The Singh et al. paper notes that the natural extension of the work is to lattices of vortices. From the OST standpoint, several lines of extension are of independent interest.

**(A) Two vortices, opposite circulation.** A configuration with two counter-rotating vortices in a standing-wave field would test whether the Controfase emergence is additive (two sets of nodal lines, one per vortex) or whether it produces a globally reorganised topology with new interference structures. The OST prediction, on the basis of the non-additivity proposition (§3), is the latter.

**(B) Vortex with time-varying circulation.** The Singh et al. analysis assumes a stationary vortex. A slow modulation of Γ would test whether the nodal-line count tracks $|\alpha(t)|$ adiabatically or whether transitions between integer counts produce observable defect-creation events. The OST prediction is that the transitions are not smooth but punctuated, with defect-creation localised at the moments when $|\alpha|$ crosses integer values. This is testable.

**(C) Standing wave with phase imbalance.** The Singh et al. configuration uses two counter-propagating waves of equal amplitude. An imbalance — say, amplitude ratio 1 : (1 + ε) for small ε — would interpolate between the standing-wave and travelling-wave regimes. The OST prediction is that the nodal-line structure persists for a finite range of ε before breaking down into the dislocation pattern of the Berry case. The breakdown threshold is a measurable quantity.

**(D) Lattice of vortices with sign alternation.** The natural OCT generalisation. A square lattice of alternating-sign vortices would create a periodic potential of α-values. The nodal-line structure of the unit cell, and its global organisation across the lattice, would test the categorical predictions about composition of configuration morphisms. The Singh et al. paper proposes a uniform-sign lattice as the next experimental step. The alternating-sign extension is a complementary configuration of OST interest.

**(E) Operational measurement of $C^*$.** The candidate operationalisation suggested in §6 (spatial integral of response over domain) can be tested in the existing experimental setup by measuring the energy in the nodal-line structure as a function of distance from the vortex core. The dissipative attenuation curve is already implicit in Figs. 3 and 4 of the paper; its quantitative form would constitute the first measurement of $C^*$ in a controlled physical system.

These extensions are recorded here for potential collaboration with experimental groups working on hydrodynamic analogues, including the Singh/Bandi group at OIST, the Volovik programme on superfluid analogues, and the Concha group at UAI. None require new framework development to motivate; they all follow directly from OST propositions applied to existing experimental capability.

---

## 9. Limits, caveats, and what the paper does not establish

A disciplined reading must be explicit about the boundary of what the case supports. The following points are recorded to prevent overextension.

**(L1)** The Singh et al. paper is a fluid-dynamics paper. It does not invoke or test OST. The structural identifications proposed in §§3–6 are *external readings* offered by the present document. They identify isomorphisms; they do not establish that the OST framework is what the authors had in mind, nor that the authors would endorse the readings.

**(L2)** The hydrodynamic-quantum analogy is itself bounded. The shallow-water-to-Schrödinger mapping requires hk ≪ 1 and U ≪ c. Outside this regime the mapping breaks down and nothing in the paper transfers to genuine quantum systems. The OST readings are about the structural pattern, not about a claim that quantum mechanics is "really" hydrodynamics; the paper itself is careful about this distinction, and so is this document.

**(L3)** The contrast between continuous α and quantized Φ_B (§5) is a real difference between the classical and quantum cases, not a defect of the analogy. The Singh et al. result demonstrates emergent topological quantization in the *classical* system; it does not derive quantum quantization from classical considerations.

**(L4)** The dissipative attenuation of nodal lines in the experiment (visible in Fig. 3 of the paper) means that the *theoretical* system-spanning property is not fully realised in the *experimental* observation. The nodal lines fade with distance from the vortex due to viscosity and capillarity. The system is genuinely non-local in the inviscid theoretical limit; it is approximately non-local in the experimental realisation. This is not a problem for the OST reading — the framework does not require dissipation-free systems — but it is a constraint on quantitative comparison.

**(L5)** The proposed implications in §7 are differentially supported. The Reaction-Diffusion v1.3 application (§7.1) requires only the structural plausibility argument and is robustly supported by the Singh et al. case. The OCT application (§7.2) is at the level of an illustrative example, not a development. The Semantic Genome implication (§7.3) is explicitly limited to a condition-of-possibility claim, not a positive evidential claim. The book exemplar (§7.4) is a didactic use, not an analytical use. Each application carries its own confidence level and should be cited with that level made explicit.

**(L6)** The candidate operationalisation of $C^*$ proposed in §6 has not been independently tested against the existing OST commitments. It is offered as a direction. Before adoption it requires:
- Verification that the spatial integral of response is well-defined in non-fluid OST applications;
- Comparison with the existing $C^*$ definition in OST Extension v1.1;
- Demonstration that the operationalisation does not collapse $C^*$ onto a quantity already used under another name.

**(L7)** The Singh et al. result is at $S_0$ confidence on its own physical content (peer-reviewed, reproduced experimentally and theoretically, code public). The OST readings of §§3–6 are at $S_1$ on the structural identifications and at $S_2$ on the proposed extensions. The $S_3$ hypotheses are explicitly flagged as such (the proposed predictions for the experiments of §8). No claim in this document carries a confidence higher than the underlying evidence supports.

---

## 10. Conclusion

Singh, Rønning, Liu, Angheluta, Concha, and Bandi report a hydrodynamic analogue experiment that, in the framework of OST, instantiates four structural propositions: ordinative non-additivity under modification of $R$, emergence of structural Controfase as the unique coherent response of a configured system to an organising attractor, topology-generated quantization in the absence of source quantization, and teleodynamic causal inversion in which global configuration determines the spatial scope of local cause.

The case is small enough to be handled with full quantitative rigour by the authors and structurally clean enough to admit unambiguous OST identification. It functions as an external, peer-reviewed, fully reproducible empirical example of OST principles operating in a controlled physical setting, without the framework needing to take any position on the physical interpretation that the authors themselves develop.

The implications for the active OST research programme are differentiated: a robust supporting citation for the Reaction-Diffusion Civilizational Dynamics v1.3 development; an illustrative example for early Ordinative Category Theory; a condition-of-possibility argument for the Semantic Genome interpretation; a didactic exemplar for the forthcoming book on Ordinative AI philosophy. None of these uses requires the framework to overreach beyond what the case supports.

Five extensions of the experimental configuration are proposed (§8) that follow directly from OST propositions and that are within the existing experimental capability of the field. These are recorded for potential collaboration.

The case is offered as an instance of what can be expected when OST is brought into contact with rigorous external work: structural mappings emerge, propositions are exemplified rather than merely asserted, and the framework's claims about non-additivity, Controfase, topological quantization, and causal inversion acquire the kind of grounding that comes from a system in which everything is measured and nothing is hidden.

---

## Appendix A: Glossary mapping

The following table records the structural correspondences identified in §§3–6. Confidence grades indicate the degree to which the mapping is direct ($S_1$) versus interpretive ($S_2$).

| OST construct | Singh et al. (2026) instantiation | Confidence |
|---|---|---|
| Ordinative system $\langle \Sigma, R, \Phi \rangle$ | Fluid + vortex + standing wave under shallow-water dynamics | $S_1$ |
| Constituents $\Sigma$ | Fluid medium, vortex, two counter-propagating travelling waves | $S_1$ |
| Relation $R$ | Shallow-water equations + azimuthal gauge + double-direction wave incidence | $S_1$ |
| Response $\Phi$ | Surface deformation field $\eta(\vec r, t)$ with quantized rotating nodal lines | $S_1$ |
| Non-additivity of $\Phi$ under $R$ change | n → 2n substitution producing global rather than local response | $S_1$ |
| Attractor (organising agent) | Stationary vortex of circulation $\Gamma$ | $S_1$ |
| Structural Controfase $\mathcal{C}_s$ | System-spanning rotating nodal lines counter-rotating with vortex | $S_1$ |
| Phase opposition across Controfase | π phase shift of $\eta$ across each nodal line | $S_1$ |
| Quantization of Controfase | Integer count $N \in \{\lfloor|\alpha|\rfloor, \lceil|\alpha|\rceil\}$ | $S_1$ |
| Independence from attractor micro-structure | Robustness to near-core details | $S_1$ |
| Topology-generated quantization | Integer N from continuous Γ via topological constraint | $S_1$ |
| Causal inversion | Vortex effect-envelope changes from local to global by $R$ modification | $S_1$ |
| Meta-receptivity $C^*$ (operationalisation candidate) | Spatial integral of response over domain | $S_2$ |
| OCT functor $F: \mathbf{Cfg} \to \mathbf{Top}_{\mathbb{Z}}$ | Berry → Singh morphism mapped to dislocation → nodal-line transition | $S_2$ |

---

## Appendix B: Inventory of propositions and confidence grades

For traceability in subsequent work, each substantive claim of this document is recorded with its confidence grade.

**$S_0$ (verified data):**
- The Singh et al. (2026) experimental result, including the existence, count, rotation rate, rotation direction, and phase opposition properties of the nodal lines.
- The shallow-water-to-Schrödinger correspondence within the stated regime.
- The publication, peer review, and code availability of the paper.

**$S_1$ (triangulable structural inferences):**
- The four ordinative readings of §§3–6 as direct mappings of the experimental result onto OST framework definitions.
- The non-additivity proposition (§3) as instantiated by the n → 2n substitution.
- The four-criterion identification of nodal lines as structural Controfase (§4).
- The identification of the case as topology-generated quantization without source quantization (§5).
- The identification of the Berry-to-Singh contrast as a case of causal inversion (§6).
- The status of the case as a robust supporting citation for Reaction-Diffusion v1.3 (§7.1).

**$S_2$ (structural interpretations within framework, not independently verified):**
- The proposed operationalisation of $C^*$ as spatial integral of response over domain (§6).
- The OCT categorical reading (§7.2) as a small-example anchor.
- The condition-of-possibility argument for the Semantic Genome (§7.3).
- The proposal that the four Controfase properties identified in §4 generalise to non-fluid OST applications.

**$S_3$ (working hypotheses, to be tested):**
- The OST predictions for each of the five proposed extensions of the experimental configuration (§8).
- The prediction that nodal-line transitions in time-varying-Γ experiments are punctuated rather than smooth.
- The prediction that the standing-wave Controfase persists for finite amplitude imbalance ε before breaking down.

---

## References

Singh, A., Rønning, J., Liu, C.-C., Angheluta, L., Concha, A., & Bandi, M. M. (2026). Topology made visible through standing waves in a spinning fluid. *Communications Physics*, 9, 123. https://doi.org/10.1038/s42005-026-02603-w

Berry, M., Chambers, R., Large, M., Upstill, C., & Walmsley, J. (1980). Wavefront dislocations in the Aharonov-Bohm effect and its water wave analogue. *European Journal of Physics*, 1, 154.

Aharonov, Y., & Bohm, D. (1959). Significance of electromagnetic potentials in the quantum theory. *Physical Review*, 115, 485–491.

Coste, C., Lund, F., & Umeki, M. (1999). Scattering of dislocated wave fronts by vertical vorticity and the Aharonov-Bohm effect. I. Shallow water. *Physical Review E*, 60, 4908.

Ghioni, F. (2026). *Reaction-Diffusion Civilizational Dynamics within the OST Framework* (v1.2). Working paper.

Ghioni, F. (2025). *Ordinative Set Theory: A Concise Guide for AI* (v2.1). Ordinative Sciences Press.

Ghioni, F. (2025). *OST Extension: Teleodynamics and Causal Inversion* (v1.1). Ordinative Sciences Press.

Ghioni, F. (2026). *TE_CORE v5.1*. Technology of Expressions framework documentation.

---

*End of working paper v1.0. Subsequent versions: v1.1 will incorporate any corrections from Hypervisor review and may add a categorical formalism appendix as OCT develops; v2.0 will be issued if the proposed experimental extensions of §8 are pursued and reported.*
