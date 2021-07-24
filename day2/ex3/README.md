# Exercise 3

## Results

- LO: 1494 ± 4.8 pb
- NLO: 2087 ± 8.7 pb

Thus the K-factor is: 1.3969 ± 0.0074

(here and in the previous exercise the error on K-factor has been obtained as
the approximate variance, thus summing in quadrature)

```python
import numpy as np

def kfactor(a, da, b, db):
    r = a / b
    return (r, np.sqrt(r**2 * ((da/a)**2 + (db/b)**2)))
```

## LO - NLO plots comparison

Plots that does involve $p_t$ are trivial for LO, since the particles are
outgoing back-to-back, instead they are non-trivial for the NLO analysis,
because of the further jets.
