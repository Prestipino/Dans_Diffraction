"""
Load data generated by Vesta
Ver. 3.5.8 11/08/2022
"""

import os
import numpy as np

data_dir = os.path.join(os.path.dirname(__file__), 'data')

WAVELENGTH = 1.54059  # angstrom (Cu Ka)
LATTICE = {
    'cubic': {'a': 3.92},
    'hexagonal': dict(a=2.85, c=10.8, gamma=120.),
    'tetragonal': dict(a=5.9, b=5.9, c=8.7),
    'monoclinic': dict(a=4.5, b=4.5, c=4.5, beta=65.0),
    'rhombohedral': dict(a=4.9, b=4.9, c=4.9, alpha=85.0, beta=85.0, gamma=85.0),
    'triclinic': dict(a=6.867, b=16.706, c=5.399, alpha=62.98, beta=42.25, gamma=52.16)
}
HKL = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1)
]


# Calcualted using vesta
vesta = {
    'cubic': os.path.join(data_dir, 'vesta_cubic.txt'),
    'hexagonal': os.path.join(data_dir, 'vesta_hexagonal.txt'),
    'tetragonal': os.path.join(data_dir, 'vesta_tetragonal.txt'),
    'monoclinic': os.path.join(data_dir, 'vesta_monoclinic.txt'),
    'rhombohedral': os.path.join(data_dir, 'vesta_rhombohedral.txt'),
    'triclinic': os.path.join(data_dir, 'vesta_triclinic.txt'),
    'rutile_neutron': os.path.join(data_dir, 'vesta_Rutile_neutron.txt'),
    'rutile_xray': os.path.join(data_dir, 'vesta_Rutile_xray.txt'),
}
VOLUMES = {
    'cubic': 60.236292,
    'hexagonal': 75.970343,
    'tetragonal': 302.847003,
    'monoclinic': 82.587297,
    'rhombohedral': 116.379532,
    'triclinic': 328.878918
}


class VestaData:
    """Vesta data loader"""
    def __init__(self, name):
        self.filename = vesta[name]
        self.data = np.loadtxt(self.filename, skiprows=1)

    def get_hkl(self):
        return self.data[:, :3]

    def get_row(self, hkl):
        idx = np.argmin(np.sqrt(np.sum(np.square(self.data[:, :3] - hkl), axis=1)))
        return self.data[idx, :]

    def get_dspace(self, hkl):
        row = self.get_row(hkl)
        return row[3]

    def get_sf(self, hkl):
        row = self.get_row(hkl)
        return complex(row[4], row[5])

    def get_2theta(self, hkl):
        row = self.get_row(hkl)
        return row[7]

    def get_intensity(self, hkl):
        row = self.get_row(hkl)
        return row[8]