# HyperQuest

[![Build Status](https://github.com/brentwilder/hyperquest/actions/workflows/pytest.yml/badge.svg)](https://github.com/brentwilder/hyperquest/actions/workflows/pytest.yml)
![PyPI](https://img.shields.io/pypi/v/hyperquest)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hyperquest)
[![Downloads](https://pepy.tech/badge/hyperquest)](https://pepy.tech/project/hyperquest)


`hyperquest`: A Python package for estimating image-wide quality estimation metrics of hyperspectral imaging (imaging spectroscopy). Computations are sped up and scale with number of cpus.


## Installation Instructions

The latest release can be installed via pip:

```bash
pip install hyperquest
```


## Usage example

- see [Example Using EMIT](tutorials/example_using_EMIT.ipynb) for a recent use case.

```python
import hyperquest
import matplotlib.pyplot as plt


# Define path to envi image header file
envi_hdr_path = '/path/my_spectral_image.hdr'

# get wavelengths
wavelengths = hyperquest.read_center_wavelengths(envi_hdr_path)

# compute SNR using HRDSDC method
snr = hyperquest.hrdsdc(envi_hdr_path, n_segments=10000, 
                        compactness=0.1, n_pca=3, ncpus=3)

plt.scatter(wavelengths, snr, color='black', s=100, alpha=0.7)
```
![SNR Plot](tests/plots/demo_snr.png)



## Citing HyperQuest (STILL WORKING ON THIS TODO:)

If you use HyperQuest in your research, please use the following BibTeX entry.

```bibtex
@article{wilder202x,
  title={x},
  author={Brenton A. Wilder},
  journal={x},
  url={x},
  year={x}
}
```


## References:

- Cogliati, S., Sarti, F., Chiarantini, L., Cosi, M., Lorusso, R., Lopinto, E., ... & Colombo, R. (2021). The PRISMA imaging spectroscopy mission: overview and first performance analysis. Remote sensing of environment, 262, 112499.

- Curran, P. J., & Dungan, J. L. (1989). Estimation of signal-to-noise: a new procedure applied to AVIRIS data. IEEE Transactions on Geoscience and Remote sensing, 27(5), 620-628.

- Gao, L., Wen, J., & Ran, Q. (2007, November). Residual-scaled local standard deviations method for estimating noise in hyperspectral images. In Mippr 2007: Multispectral Image Processing (Vol. 6787, pp. 290-298). SPIE.

- Gao, L. R., Zhang, B., Zhang, X., Zhang, W. J., & Tong, Q. X. (2008). A new operational method for estimating noise in hyperspectral images. IEEE Geoscience and remote sensing letters, 5(1), 83-87.

- Roger, R. E., & Arnold, J. F. (1996). Reliably estimating the noise in AVIRIS hyperspectral images. International Journal of Remote Sensing, 17(10), 1951-1962.

- Tian, W., Zhao, Q., Kan, Z., Long, X., Liu, H., & Cheng, J. (2022). A new method for estimating signal-to-noise ratio in UAV hyperspectral images based on pure pixel extraction. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 16, 399-408.
