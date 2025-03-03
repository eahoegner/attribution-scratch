# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pint
import pint.testing
from pint import UnitRegistry
from attribution_scratch.unit_aware import add_unit_aware

# %%
Q = pint.get_application_registry().Quantity


# %%
def test_add_unit_aware():
    T_rel = Q(30.0, "K")
    T_abs = Q(274.15, "K")
    exp = Q(31.0, "degC")

    res = add_unit_aware(T_rel, T_abs)

    pint.testing.assert_equal(res, exp)


# %%
def test_add_plain_floats():
    T_rel = Q(30)
    T_abs = Q(274.15)
    exp = Q(31.0)

    res = add_unit_aware(T_rel, T_abs)

    pint.testing.assert_equal(res, exp)


# %%
test_add_unit_aware()
test_add_plain_floats()
