# Exercise 4

## part (a)

- LO: 461.3 ± 2.3
- LO + PS: 459.2 ± 2.1
- K factor (LO+PS/LO): 0.9954 ± 0.0067

(error on the K-factor by summing in quadrature, see previous exercise)

In the pure LO the top pair is emitted back to back, since no other particle is
present in the outgoing state.
For this reason the last plot in the file `lo.pdf` shows a single-bin
distribution, since all the events fall in the 0 bin.

On the other hand when parton shower is active further particles are emitted
from the outgoing top pair, and thus even the transverse momentum of the pair
itself is modified, making a non-trivial distribution, as shown in the last plot
of `lo_ps.pdf`

## part (b)

- NLO: 679.4 ± 4.5
- NLO + PS: 680.2 ± 4
- K factor (NLO+PS/NLO): 1.0011 ± 0.0089
- K factor (NLO/LO): 1.472 ± 0.012

Also the NLO (even w/o PS) makes possible to have a richer outgoing state,
making the pt distribution of the ttbar pair non-trivial.

In the case of the fixed order calculation the results for the individual
transverse momentum distributions (pt of t and tbar) are much more noisy w.r.t.
LO and LO+PS, and even w.r.t. the same NLO+PS.

Indeed the major effect of the PS is still on the transverse momentum's
distribution of the pair, moving a lot of weights from low transverse momentum
in the high pt range, as it was happening for the LO (in which the single bin at
0 was spread all over the range).

See `nlo.pdf` and `nlo_ps.pdf` last plots for the pt distribution of the ttbar
pair.
