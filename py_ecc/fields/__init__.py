from .field_elements import (
    FQ,
    FQP,
    FQ2,
    FQ12,
)

from .field_properties import (
    field_properties,
)

from .optimized_field_elements import (
    FQ as optimized_FQ,
    FQP as optimized_FQP,
    FQ2 as optimized_FQ2,
    FQ12 as optimized_FQ12,
)


#
# btoy curve fields
#
class btoy_FQ(FQ):
    field_modulus = 101


class btoy_FQP(FQP):
    field_modulus = 101


class btoy_FQ2(FQ2, btoy_FQP):
    field_modulus = 101
    FQ2_MODULUS_COEFFS = field_properties["bn128"]["fq2_modulus_coeffs"]


class btoy_FQ12(FQ12, btoy_FQP):
    field_modulus = 101
    FQ12_MODULUS_COEFFS = field_properties["bn128"]["fq12_modulus_coeffs"]

#
# bn128 curve fields
#
class bn128_FQ(FQ):
    field_modulus = field_properties["bn128"]["field_modulus"]


class bn128_FQP(FQP):
    field_modulus = field_properties["bn128"]["field_modulus"]


class bn128_FQ2(FQ2, bn128_FQP):
    field_modulus = field_properties["bn128"]["field_modulus"]
    FQ2_MODULUS_COEFFS = field_properties["bn128"]["fq2_modulus_coeffs"]


class bn128_FQ12(FQ12, bn128_FQP):
    field_modulus = field_properties["bn128"]["field_modulus"]
    FQ12_MODULUS_COEFFS = field_properties["bn128"]["fq12_modulus_coeffs"]


#
# bls12_381 curve fields
#
class bls12_381_FQ(FQ):
    field_modulus = field_properties["bls12_381"]["field_modulus"]


class bls12_381_FQP(FQP):
    field_modulus = field_properties["bls12_381"]["field_modulus"]


class bls12_381_FQ2(FQ2, bls12_381_FQP):
    field_modulus = field_properties["bls12_381"]["field_modulus"]
    FQ2_MODULUS_COEFFS = field_properties["bls12_381"]["fq2_modulus_coeffs"]


class bls12_381_FQ12(FQ12, bls12_381_FQP):
    field_modulus = field_properties["bls12_381"]["field_modulus"]
    FQ12_MODULUS_COEFFS = field_properties["bls12_381"]["fq12_modulus_coeffs"]


#
# optimized_bn128 curve fields
#

class optimized_bn128_FQ(optimized_FQ):
    field_modulus = field_properties["bn128"]["field_modulus"]


class optimized_bn128_FQP(optimized_FQP):
    field_modulus = field_properties["bn128"]["field_modulus"]


class optimized_bn128_FQ2(optimized_FQ2, optimized_bn128_FQP):
    field_modulus = field_properties["bn128"]["field_modulus"]
    FQ2_MODULUS_COEFFS = field_properties["bn128"]["fq2_modulus_coeffs"]


class optimized_bn128_FQ12(optimized_FQ12, optimized_bn128_FQP):
    field_modulus = field_properties["bn128"]["field_modulus"]
    FQ12_MODULUS_COEFFS = field_properties["bn128"]["fq12_modulus_coeffs"]


#
# optimized_bls12_381 curve fields
#
class optimized_bls12_381_FQ(optimized_FQ):
    field_modulus = field_properties["bls12_381"]["field_modulus"]


class optimized_bls12_381_FQP(optimized_FQP):
    field_modulus = field_properties["bls12_381"]["field_modulus"]


class optimized_bls12_381_FQ2(optimized_FQ2, optimized_bls12_381_FQP):
    field_modulus = field_properties["bls12_381"]["field_modulus"]
    FQ2_MODULUS_COEFFS = field_properties["bls12_381"]["fq2_modulus_coeffs"]


class optimized_bls12_381_FQ12(optimized_FQ12, optimized_bls12_381_FQP):
    field_modulus = field_properties["bls12_381"]["field_modulus"]
    FQ12_MODULUS_COEFFS = field_properties["bls12_381"]["fq12_modulus_coeffs"]
