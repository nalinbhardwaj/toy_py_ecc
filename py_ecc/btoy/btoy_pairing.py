from __future__ import absolute_import

from py_ecc.fields import (
    btoy_FQ as FQ,
    btoy_FQ2 as FQ2,
    btoy_FQ12 as FQ12,
)
from py_ecc.fields.field_properties import (
    field_properties,
)

from py_ecc.typing import (
    Field,
    Point2D,
)

from .btoy_curve import (
    double,
    add,
    multiply,
    is_on_curve,
    twist,
    b,
    b2,
    curve_order,
    G1,
)


field_modulus = field_properties["bn128"]["field_modulus"]

ate_loop_count = 29793968203157093288
log_ate_loop_count = 63


# Create a function representing the line between P1 and P2,
# and evaluate it at T
def linefunc(P1: Point2D[Field],
             P2: Point2D[Field],
             T: Point2D[Field]) -> Field:
    assert P1 and P2 and T  # No points-at-infinity allowed, sorry
    x1, y1 = P1
    x2, y2 = P2
    xt, yt = T
    if x1 != x2:
        m = (y2 - y1) / (x2 - x1)
        return m * (xt - x1) - (yt - y1)
    elif y1 == y2:
        m = 3 * x1**2 / (2 * y1)
        return m * (xt - x1) - (yt - y1)
    else:
        return xt - x1


def cast_point_to_fq12(pt: Point2D[FQ]) -> Point2D[FQ12]:
    if pt is None:
        return None
    x, y = pt
    fq12_point = (FQ12([x.n] + [0] * 11), FQ12([y.n] + [0] * 11))
    return fq12_point


# Check consistency of the "line function"
one, two, three = G1, double(G1), multiply(G1, 3)
negone, negtwo, negthree = (
    multiply(G1, curve_order - 1),
    multiply(G1, curve_order - 2),
    multiply(G1, curve_order - 3),
)


assert linefunc(one, two, one) == FQ(0)
assert linefunc(one, two, two) == FQ(0)
assert linefunc(one, two, three) != FQ(0)
assert linefunc(one, two, negthree) == FQ(0)
assert linefunc(one, negone, one) == FQ(0)
assert linefunc(one, negone, negone) == FQ(0)
assert linefunc(one, negone, two) != FQ(0)
assert linefunc(one, one, one) == FQ(0)
assert linefunc(one, one, two) != FQ(0)
assert linefunc(one, one, negtwo) == FQ(0)


# Main miller loop
def miller_loop(Q: Point2D[FQ12],
                P: Point2D[FQ12]) -> FQ12:
    if Q is None or P is None:
        return FQ12.one()
    R = Q   # type: Point2D[FQ12]
    f = FQ12.one()
    for i in range(log_ate_loop_count, -1, -1):
        f = f * f * linefunc(R, R, P)
        R = double(R)
        if ate_loop_count & (2**i):
            f = f * linefunc(R, Q, P)
            R = add(R, Q)
    # assert R == multiply(Q, ate_loop_count)
    Q1 = (Q[0] ** field_modulus, Q[1] ** field_modulus)
    # assert is_on_curve(Q1, b12)
    nQ2 = (Q1[0] ** field_modulus, -Q1[1] ** field_modulus)
    # assert is_on_curve(nQ2, b12)
    f = f * linefunc(R, Q1, P)
    R = add(R, Q1)
    f = f * linefunc(R, nQ2, P)
    # R = add(R, nQ2) This line is in many specifications but it technically does nothing
    return f ** ((field_modulus ** 12 - 1) // curve_order)


# Pairing computation
def pairing(Q: Point2D[FQ2], P: Point2D[FQ]) -> FQ12:
    assert is_on_curve(Q, b2)
    assert is_on_curve(P, b)
    return miller_loop(twist(Q), cast_point_to_fq12(P))


def final_exponentiate(p: Field) -> Field:
    return p ** ((field_modulus ** 12 - 1) // curve_order)
