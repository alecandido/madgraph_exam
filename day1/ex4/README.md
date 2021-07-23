---
documentclass: article
geometry: margin=3cm
header-includes: |
  \usepackage{physics}
title: Exercise 4
---

<!--compile with:-->
<!--pandoc -s -o README.pdf README.md-->

The full calculation is provided in `ex4.nb` Mathematica notebook, it has been
performed using the `HEPMath` package.

# part (a)

$$
\frac{e^4 Q_f^2 (\cos (2 \theta )+3)}{4 \pi  s} =  Q_f^2\frac{\pi\alpha^2}{2 s}(1+\cos^2 ( \theta ))
$$

This is the same cross section for production of muon pairs from
electron-positron annihilation, apart from the charge factor $Q_f^2$, and the
omitted sum over colors.

The flavors to sum on should be those who are possible to excite at the
experiment energy, and so those whose mass is below $s/2$.

The observed plateaus in the ratio between the electrons-into-hadrons and
electron-into-muons indeed gave two fundamental pieces of information for the
birth of the quark model:

- the number of active flavors is increasing with the energy
- the plateaus and hadrons charges can be explained with attributing the known
  charges to the quarks, but then a factor $3$ is still missing in the ratio:
  together with the hadron multiplets structure this has been a crucial clue of
  a further hidden quantum number, the color

# part (b)

$$
\frac{\frac{1}{64} \left(8 \sin^4(\theta_W)-4 \sin^2(\theta_W)+1\right)
\left(A_f^2+V_f^2\right) (\cos (2 \theta )+3)+\frac{1}{4} (1-4
\sin^2(\theta_W)) A_f V_f \cos (\theta )}{128 \pi  s}
$$

The $\cos (\theta)$ distribution is split in two parts:

- the first one still proportional to $\cos (2 \theta) + 3 = 2 (1 +
  \cos^2(\theta))$, whose coefficient is proportional to $A_f^2 + V_f^2$, i.e.
  it gets contribution from all the bits in the square amplitudes that contain
  an even number of $\gamma^5$
- the second one it's now proportional to $\cos(\theta)$ instead of
  $\cos(2\theta) \to \cos^2(\theta)$, and its coefficient is proportional to
  $A_f V_f$, so it is the contribution of the terms that are odd in $\gamma^5$
  (i.e. that contain a single $\gamma^5$)
