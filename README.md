# Gene loci fluctuations organization reveal bacterial chromosome dynamical organization
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
## (A) Initial Simulations: Assembly of the Polymer Bottle-Brush Structure
- system.data: This file contains the initial input with polymer configuration. Type 1 beads are chromatin beads, and every 60th bead is Type 2, representing anchor beads.
- 1_system_min.in:  A script file for LAMMPS, intended to perform an energy minimization procedure for the system.
- 2_system_loop_create.in: LAMMPS script file responsible for introducing harmonic spring energy between loop anchors, enabling the simulation of the system as a self-avoiding polymer.
- 3_system_condensation.in: LAMMPS script file designed to incorporate condensation forces between loop anchors, allowing the system to simulate as a self-attracting polymer.
- table_bonds_stage2.dat: Table contains condensation forces.
- 4_system_cylinder_indent.in: Script file for LAMMPS that applies cylindrical indenter forces to only anchor beads to align the curved anchor regions into a linear configuration.
- 5_system_cylinder_indent_type1bead_fixtype2.in:  LAMMPS script that applies cylindrical indenter forces to all beads, fitting the bottle-brush polymer structure into its smallest volume (\( R = 13 \sigma \)), where \( \sigma \) is the bead diameter and \( R \) is the cylinder radius. Anchor regions are made rigid by excluding them from Langevin dynamics.

## (B) Final Simulation: Minimal Model Bacterial Chromosome for Anisotropic Behavior
- system.in: LAMMPS script file for the final simulation, modeling the bottle-brush complex within cylindrical confinement.
- 5_system_initial.data: This file contains the initial input with polymer configuration for the final simulation.
- command.sh: Shell script to run multiple simulations with different Lennard-Jones interaction strengths (\( \epsilon \)).


## How to run
- Refer [LAMMPS documentation](https://docs.lammps.org/Install.html) for installation. Run LAMMPS using command (make sure that the configuration file system.data is present in the same directory)
  ## (A) Initial Simulations:

```
./lmp -in 1_system_min.in
./lmp -in 2_system_loop_create.in
./lmp -in 3_system_condensation.in
./lmp -in 4_system_cylinder_indent.in
./lmp -in 5_system_cylinder_indent_type1bead_fixtype2.in
```
## (B) Final Simulation:
```
./command.sh system.in
./lmp -in system.in
```

Anticipated Outcome: The simulation generates a positional trajectory file in the lammpstrj format, utilized for visualizing simulation outcomes using [VMD](https://www.ks.uiuc.edu/Research/vmd/)  software. Furthermore, the simulation yields an msdcom_new.txt file, facilitating the computation of the mean squared displacement of the system in the x, y, and z directions.


Standard installation of the LAMMPS software usually requires approximately 30 minutes. The initial simulation run is completed in less than 8 hours, whereas the final simulation run extends over a duration of around 72 hours.
