"""
# Description

This module contains utility functions to handle multiple `aton.qrotor.system` calculations.


# Index

| | |
| --- | --- |
| `check()`            | Check that a list only contains System objects |
| `get_energies()`     | Get the eigenvalues from all systems |
| `get_gridsizes()`    | Get all gridsizes |
| `get_runtimes()`     | Get all runtimes |
| `get_groups()`       | Get the chemical groups in use |
| `sort_by_gridsize()` | Sort systems by gridsize |
| `reduce_size()`      | Discard data that takes too much space |
| `get_ideal_E()`      | Calculate the ideal energy for a specified level |

---
"""


from .system import System


def check(systems:list) -> None:
    """Check that a list only contains System objects."""
    for i in systems:
        if not isinstance(i, System):
            raise ValueError(f"All values in the list must be a System object, found instead: {type(i)}")
    return None


def get_energies(systems:list) -> list:
    """Get a list with all eigenvalues from all systems.

    If no eigenvalues are present for a particular system, appends None.
    """
    check(systems)
    energies = []
    for i in systems:
        if all(i.eigenvalues):
            energies.append(i.eigenvalues)
        else:
            energies.append(None)
    return energies


def get_gridsizes(systems:list) -> list:
    """Get a list with all gridsize values.

    If no gridsize value is present for a particular system, appends None.
    """
    check(systems)
    gridsizes = []
    for i in systems:
        if i.gridsize:
            gridsizes.append(i.gridsize)
        else:
            gridsizes.append(None)
    return gridsizes


def get_runtimes(systems:list) -> list:
    """Returns a list with all runtime values.
    
    If no runtime value is present for a particular system, appends None.
    """
    check(systems)
    runtimes = []
    for i in systems:
        if i.runtime:
            runtimes.append(i.runtime)
        else:
            runtimes.append(None)
    return runtimes


def get_groups(systems:list) -> list:
    """Returns a list with all `System.group` values."""
    check(systems)
    groups = []
    for i in systems:
        if i.group not in groups:
            groups.append(i.group)
    return groups


def sort_by_gridsize(systems:list) -> list:
    """Sorts a list of System objects by `System.gridsize`."""
    check(systems)
    systems = sorted(systems, key=lambda sys: sys.gridsize)
    return systems


def reduce_size(systems:list) -> list:
    """Discard data that takes too much space.

    Removes eigenvectors, potential values and grids,
    for all System values inside the `systems` list.
    """
    check(systems)
    for dataset in systems:
        dataset = dataset.reduce_size()
    return systems


def get_ideal_E(E_level:int) -> int:
    """Calculates the ideal energy for a specified `E_level`.

    To be used in convergence tests with `potential_name = 'zero'`.
    """
    real_E_level = None
    if E_level % 2 == 0:
        real_E_level = E_level / 2
    else:
        real_E_level = (E_level + 1) / 2
    ideal_E = int(real_E_level ** 2)
    return ideal_E

