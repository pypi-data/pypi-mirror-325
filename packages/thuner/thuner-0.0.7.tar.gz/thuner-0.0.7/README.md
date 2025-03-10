# Thunderstorm Event Reconnaissance (THUNER)

## Package description
Welcome to the Thunderstorm Event Reconnaissance (THUNER) package! 
THUNER is a flexible toolkit for multi-feature detection, tracking, tagging
and analysis of events in meteorological datasets. The intended application of 
the package is to the tracking and analysis of convective weather events. 
If you use this package in your work, consider citing the following papers;

- Leese et al. (1971), JAMC, doi: 10.1175/1520-0450(1971)010<0118:AATFOC>2.0.CO;2
- Dixon and Wiener (1993), JTECH, doi: 10.1175/1520-0426(1993)010<0785:TTITAA>2.0.CO;2
- Fridlind et al. (2019), AMT, doi: 10.5194/amt-12-2979-2019
- Raut et al. (2021), JAMC, doi: 10.1175/JAMC-D-20-0119.1
- Short et al. (2023), MWR, doi: 10.1175/MWR-D-22-0146.1

THUNER represents the consolidation and generalization of my (Ewan's) PhD work; 
before 2024 the core algorithm was called "MINT". Many excellent competitors to THUNER 
exist, for instance;

- https://github.com/FlexTRKR/PyFLEXTRKR
- https://github.com/knubez/TAMS
- https://github.com/tobac-project/tobac
- https://github.com/AndreasPrein/MOAAP

When designing a tracking based research project involving THUNER, consider performing 
sensitivity tests using these competitors.

## Installation
The THUNER repository can be cloned from github in the usual ways. Cloning the 
repository is the easiest way to access the demo, workflow and gallery folders. 

The thuner package can also be installed via conda
```sh
conda install -c conda-forge thuner
```
While installation using conda is preferred, thuner may also be installed using pip.
To install with pip, the esmpy package must first be installed manually as 
detailed [here](https://xesmf.readthedocs.io/en/latest/installation.html#notes-about-esmpy).
THUNER can then be installed using 
```sh
pip install thuner
```
Because thuner depends on xesmf for regridding, it is currently only available on Linux 
and OSX systems. Future versions will explore alternative regridding packages. 

## Examples

### GridRad
The examples below illustrate the tracking of convective systems in 
[GridRad Severe](https://gridrad.org/) radar data. Object merge events are visualized
through the "mixing" of the colours associated with each merging object. Objects that 
split off from existing objects retain the colour of their parent object. 

![GridRad Demo](./gallery/mcs_gridrad_20100804.gif)

![GridRad Demo](./gallery/mcs_gridrad_20100120.gif)

## Etymology
According to [Wikipedia](https://en.wikipedia.org/wiki/Thor), between 
the 8th and 16th centuries the storm god more commonly known as Thor 
was called "Thuner" by the inhabitants of what is now west Germany.
