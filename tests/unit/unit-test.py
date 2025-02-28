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
    a = Q(1.0, "Mt CO2/yr")
    b = Q(1.0, "kt CO2/yr")

    exp = Q(1.001, "Mt CO2/yr")

    res = add_unit_aware(a, b)

    pint.testing.assert_equal(res, exp)
