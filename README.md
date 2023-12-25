# Dynamics of gene loci fluctuations reveal bacterial chromosome organization

## Table of Contents  
[Overview](#overview)  
[System requirements](#system-requirements)  
[File description](#file-description)  
[How to run](#how-to-run)  

## Overview
The repository comprises scripts and code employed for the investigation of bacterial chromosome organization. We utilize the open-source LAMMPS package for simulating the bacterial chromosome.

## System requirements
- LAMMPS is an open source software. To see system requirements for LAMMPS [click here](https://docs.lammps.org/Install.html).
- The analysis codes were tested on a Linux system (Ubuntu), but codes should work on MacOS or Windows system with corresponding C-compiler.


## File description
system.data: This file contains the initial input with polymer configuration.
- 1_system_min.in: A script file designed for LAMMPS, intended to execute an energy minimization procedure for the system.
- 2_system_loop_create.in: LAMMPS script file responsible for introducing harmonic spring energy between loop anchors, facilitating the simulation of the system as a self-avoiding polymer.
- 3_system_condensation.in: LAMMPS script file designed to incorporate condensation forces between loop anchors, allowing the system to be simulated as a self-attracting polymer.
- 4_system_cylinder_indent.in: Script file for LAMMPS that applies cylindrical indenter forces to fit the system into cylindrical confinement.
- 5_system_cylinder_final.in: The final script file for LAMMPS, configured to simulate the system within a cylindrical confinement.


## How to run
- Refer [LAMMPS documentation](https://docs.lammps.org/Install.html) for installation. Run LAMMPS using command (make sure that the configuration file system.data is present in the same directory)
```
./lmp -in 1_system_min.in
./lmp -in 2_system_loop_create.in
./lmp -in 3_system_condensation.in
./lmp -in 4_system_cylinder_indent.in
./lmp -in 5_system_cylinder_final.in
```

Anticipated Outcome: The simulation generates a positional trajectory file in the lammpstrj format, utilized for visualizing simulation outcomes using [VMD](https://www.ks.uiuc.edu/Research/vmd/)  software. Furthermore, the simulation yields an msdcom_new.txt file, facilitating the computation of the mean squared displacement of the system in the x, y, and z directions.


Standard installation of the LAMMPS software usually requires approximately 30 minutes. The initial simulation run is completed in less than 30 minutes, whereas the final simulation run extends over a duration of around 24 hours.
