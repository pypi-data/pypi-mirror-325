"""
Implements common airspeed conversions.

```txt
        _________________
        v               v
IAS    CAS --> EAS <-> TAS    GS
            ^           |
            |           |------> q
            |           |
            |           |------> p_t ----> q_c
            |                               |
            |                               v
            |                    compressibility factor f
            |                               |
            |-------------------------------|
```

The equivalent airspeed $V_e$ is such that the dynamic pressure at some altitude
$q = \\frac{1}{2} \\rho V^2$ is the same as the dynamic pressure at
[sea level ISA conditions][airtrafficsim.performance.isa]
$q = \\frac{1}{2} \\rho_0 V_e^2$. EAS and TAS is related through
[airtrafficsim.performance.airspeed.eas_from_tas][].
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..thermodynamics import (
    GAMMA_DRY_AIR,
    impact_pressure,
    impact_pressure_behind_normal_shock,
)
from .isa import A_0, P_0, RHO_0

if TYPE_CHECKING:
    from typing import Annotated

    from annotated_types import Gt

    from .. import units as u
    from ..quantity import (
        CAS,
        EAS,
        TAS,
        Density,
        ImpactPressure,
        RatioOfSpecificHeats,
        StaticPressure,
    )
    from ..types import Array, ArrayOrScalarT


def impact_pressure_from_cas(
    cas: Annotated[Array, CAS(u.MPS)],
    gamma: Annotated[Array, RatioOfSpecificHeats(None)] = GAMMA_DRY_AIR,
) -> Annotated[Array, ImpactPressure(u.PASCAL)]:
    """Impact pressure, compressible flow"""
    return impact_pressure(cas, RHO_0, P_0, gamma)


def impact_pressure_from_cas_behind_normal_shock(
    cas: Annotated[Array, CAS(u.MPS)],
    gamma: Annotated[Array, RatioOfSpecificHeats(None)] = GAMMA_DRY_AIR,
) -> Annotated[Array, ImpactPressure(u.PASCAL)]:
    """Impact pressure, behind normal shock wave, supersonic flow"""
    return impact_pressure_behind_normal_shock(cas, A_0, P_0, gamma)


def density_factor(
    rho: Annotated[ArrayOrScalarT, Density(u.KGM3)],
) -> ArrayOrScalarT:
    return (rho / RHO_0) ** 0.5  # type: ignore


def eas_from_tas(
    tas: Annotated[Array, TAS(u.MPS)],
    rho: Annotated[Array, Density(u.KGM3)],
) -> Annotated[Array, EAS(u.MPS)]:
    """Converts TAS to EAS"""
    return tas * density_factor(rho)


def tas_from_eas(
    eas: Annotated[Array, EAS(u.MPS)],
    rho: Annotated[Array, Density(u.KGM3)],
) -> Annotated[Array, TAS(u.MPS)]:
    """Converts EAS to TAS"""
    return eas / density_factor(rho)


def compressibility_factor(
    qc: Annotated[Array, ImpactPressure(), Gt(0)],
    p: Annotated[Array, StaticPressure(u.PASCAL)],
    gamma: Annotated[Array, RatioOfSpecificHeats(None)] = GAMMA_DRY_AIR,
) -> Array:
    """Assumption: subsonic speeds"""
    exponent = (gamma - 1) / gamma
    inner = (qc / p + 1) ** exponent - 1
    return (exponent * p / qc * inner) ** 0.5


def eas_from_cas(
    cas: Annotated[Array, CAS(u.MPS), Gt(0)],
    p: Annotated[Array, StaticPressure(u.PASCAL)],
    gamma: Annotated[Array, RatioOfSpecificHeats(None)] = GAMMA_DRY_AIR,
) -> Annotated[Array, EAS(u.MPS)]:
    """Assumption: subsonic speeds"""
    qc = impact_pressure_from_cas(cas)
    f = compressibility_factor(qc, p, gamma)
    f0 = compressibility_factor(qc, P_0, gamma)
    return cas * f / f0


def tas_from_cas(
    cas: Annotated[Array, CAS(u.MPS)],
    rho: Annotated[Array, Density(u.KGM3)],
    p: Annotated[Array, StaticPressure(u.PASCAL)],
) -> Annotated[Array, TAS(u.MPS)]:
    """Assumption: subsonic speeds"""
    eas = eas_from_cas(cas, p)
    return tas_from_eas(eas, rho)


def cas_from_tas(
    tas: Annotated[Array, TAS(u.MPS), Gt(0)],
    rho: Annotated[Array, Density(u.KGM3)],
    p: Annotated[Array, StaticPressure(u.PASCAL)],
    gamma: Annotated[Array, RatioOfSpecificHeats(None)] = GAMMA_DRY_AIR,
) -> Annotated[Array, CAS(u.MPS)]:
    """Assumption: subsonic speeds"""
    eas = eas_from_tas(tas, rho)
    qc = impact_pressure(tas, rho, p, gamma)
    f = compressibility_factor(qc, p, gamma)
    f0 = compressibility_factor(qc, P_0, gamma)
    return eas * f0 / f
