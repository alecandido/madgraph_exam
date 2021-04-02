import numpy as np
import matplotlib.pyplot as plt

CF = 4 / 3
alphas = 0.118  # alphas(MZ)


def xs_full_massive(x1, x2, rho):
    """
    Equation(4) on the exam sheet
    """
    beta = np.sqrt(1 - rho)
    return (CF / beta * alphas / (2 * np.pi)) * (
        2 * (x1 + x2 - 1 - rho / 2) / ((1 - x1) * (1 - x2))
        - rho / 2 * (1 / (1 - x1) ** 2 + 1 / (1 - x2) ** 2)
        + 1 / (1 + rho / 2) * (((1 - x1) ** 2 + (1 - x2) ** 2) / ((1 - x1) * (1 - x2)))
    )


def xs_lo(theta, rho):
    """
    Peskin (5.12), m_mu = m is the mass of the outcome
    """
    Ecm2 = s
    E2 = Ecm2 / 2
    m2 = rho * s / 4
    alpha = 1 / 137
    return (
        (alpha ** 2 / 4 * Ecm2)
        * np.sqrt(1 - m2 / E2)
        * ((1 + m2 / E2) + (1 - m2 / E2) * np.cos(theta) ** 2)
    )


def xs_massive(z, theta, rho):
    """
    Equation(6) on the exam sheet
    """
    return CF * alphas / np.pi * 1 / z * theta ** 2 / (theta ** 2 + rho) ** 2


# GeV^2, the unique relevant energy scale
# it's just a reference, anything else is adimensional referred to this
# scale
s = 1

rho_m0 = 0
rho_m1 = 4 / 100  # in units of (m ** 2) / s
# kt = p * sin(theta) ~= p * theta
# kt ** 2 = theta ** 2 * p ** 2
kts = np.linspace(1e-2, 1.5, 1000)
thetas = kts / np.sqrt(s)
z = 2 * 3e-3 / np.sqrt(s)


# rho, m = 0
# xs_m0_lo = np.vectorize(xs_lo, excluded=[1])(thetas, rho_m0)
xs_m0 = np.vectorize(xs_massive, excluded=[0, 2])(z, thetas, rho_m0)
# rho, m = 1
# xs_m1_lo = np.vectorize(xs_lo, excluded=[1])(thetas, rho_m1)
xs_m1 = np.vectorize(xs_massive, excluded=[0, 2])(z, thetas, rho_m1)

plt.plot(kts, xs_m0, label="massless")  # * xs_m0_lo)
plt.plot(kts, xs_m1, label=r"massive $m=\sqrt{s}/10$")  # * xs_m1_lo)

plt.vlines(np.sqrt(rho_m1), 0, 80, color="tab:red", ls=(0, (3, 7)), lw=0.5)


plt.tick_params(which="both", direction="in", top=True, right=True)
plt.minorticks_on()

plt.xlim(0, 1.5)
plt.xticks(np.linspace(0, 1.5, 7))
plt.ylim(0, 80)
plt.yticks(np.linspace(0, 80, 5))
plt.legend()

# plt.show()
plt.savefig("angmom.pdf")
