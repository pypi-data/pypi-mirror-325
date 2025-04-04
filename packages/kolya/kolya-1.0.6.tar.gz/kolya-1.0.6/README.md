[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10818194.svg)](https://doi.org/10.5281/zenodo.10818194)
# Kolya

## Content
Kolya is a Python package for the calculation of the moments and the rate of inclusive semileptonic B decays in the kinetic scheme.
Kolya provides predictions both in the Standard Model and in the presence of new physics encoded in dimension-6 operators within the Weak Effective Theory.

M. Fael, I. S. Milutin, K. K. Vos.     
Kolya: an open-source package for inclusive semileptonic B decays.      
arXiv: hep-ph/2409.15007

If you use kolya, please consider also to cite the following papers whose resuts are implemented in the library:
`\cite{Manohar:1993qn,Blok:1993va,Gremm:1996df,Bigi:1996si,Czarnecki:1997sz,Aquila:2005hq,Dassinger:2006md,Pak:2008qt,Pak:2008cp,Dowling:2008mc,Biswas:2009rb,Mannel:2010wj,Alberti:2012dn,Alberti:2013kxa,Fael:2018vsp,Fael:2020iea,Fael:2020njb,Fael:2020tow,Fael:2022frj,Mannel:2023yqf,Egner:2023kxw,Mannel:2021zzr,Fael:2024gyw,Finauri:2025ost}`. These citation keys allow to retrieve the bibliographic information for the referenced papers from the INSPIRE database using the bibliography generator: [here](https://inspirehep.net/bibliography-generator)

## Observables

The package currently implement the preditions for massless lepton $`\ell`$
- Total inclusive rate $`\Gamma_\mathrm{sl}`$ and branching ratio $`Br(B \to X_c \ell \bar \nu_\ell)`$.
- Branching ratio $`\Delta Br(E_\mathrm{cut})`$ with lower cut $`E_\ell \ge E_\mathrm{cut}`$.
- Centralized moments of the charged-lepton energy $`E_\ell`$ with $`n=1,2,3`$. 
- Centralized moments of the hadronic invariant mass $`M_X^2`$ with $`n=1,2,3`$.
- Centralized moments of the leptonic invariant mass $`q^2`$ with $`n=1,2,3,4`$.

## Higher-order corrections implemented

- Power corrections at tree level up to $`1/m_b^5`$ in the historical basis.
- Total rate and $`q^2`$ moments are available also for the so-called "RPI" basis.
- Total rate: N3LO QCD corrections at leading order in the HQE ($`1/m_b^0`$) and NLO up to ($`1/m_b^3`$).
- $`q^2`$ moments: NNLO QCD corrections at leading order in the HQE ($`1/m_b^0`$) and NLO up to ($`1/m_b^3`$).
- $`E_l`$ and $`M_X^2`$ moments: NNLO QCD corrections at leading order in the HQE ($`1/m_b^0`$) and NLO up to ($`1/m_b^2`$).

## Chebyshev intepolation grids

The evaluation of the NLO and NNLO QCD corrections to the moments requires a non-trivial and numerically expensive evaluation of the differential
rates which are written in terms of HPLs and Generalized Polylogarithms (GPLs). 
Such NLO and NNLO corrections are functions of two variables, the mass ratio $`m_c/m_b`$ and the normalized lower cut $`E_\mathrm{cut}/m_b`$ or
$`q_\mathrm{cut}^2/m_b^2`$.
Kolya implements precise 2D interpolation grids based on the Chebyshev approximation method (see [here](https://www.cec.uchile.cl/cinetica/pcordero/MC_libros/NumericalRecipesinC.pdf#page=214)).
Chebyshev polynomial is close to the minimal polynomial, which (among all polynomials of the same degree) has the smallest maximum deviation 
from the true function $`f(x)`$. The interpolation grids are guaranteed to reproduce the true distributions with a precision of $`10^{-5}`$.
For the evaluation of the derivative of the NLO corrections the grids reach a precision of $`10^{-4}`$.

## Optional arguments

- Include $`1/m_b^4`$ and $`1/m_b^5`$ with the optional argument `flagmb4=1` and `flagmb5=1`.
  By default thay are switched off.
- Exclude NNLO corrections by setting `flag_includeNNLO=0`. By default `flag_includeNNLO=1`.
- Exclude N3LO corrections in the total rate by setting `flag_includeN3LO=0`. By default `flag_includeN3LO=1`.
- Exclude NLO corrections to power-suppressed terms by setting `flag_includeNLOpw=0`. By default `flag_includeNLOpw=1`.
- By default the moments are calculated in the historical basis: `flag_basisPERP=1`.
  Setting `flag_basisPERP=0` will change the evaluation to the so-called RPI basis (currently available only for $`q^2`$ moments and the total rate).
- The option `flag_DEBUG=1` will print a report of the various contributions coming from the higher-order QCD corrections (default `flag_DEBUG=0`). The contributions denoted by `NLO`, `NNLO` and `N3LO` are the coefficients in front of $`\alpha_s(\mu_s)/\pi`$, 
$`(\alpha_s(\mu_s)/\pi)^2`$ and $`(\alpha_s(\mu_s)/\pi)^3`$ at partonic level. 
The term `NLO pw` corresponds to the overall NLO correction in the terms of order $`1/m_b^2`$ and and $`1/m_b^3`$. 
In the kinetic scheme, the inclusion of the NLO corrections to the power-suppressed terms induces also an additional 
$`O(\alpha_s^2)`$ contribution in the partonic rate. This contribution is denoted by `NNLO from NLO pw`.


