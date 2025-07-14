% This script visualizes the step-like potential and force applied between anchor beads
% based on a defined cutoff distance. The potential becomes active when the distance
% between beads exceeds the specified cutoff (distance = 3 in this case).

% We generate the potential $U^{\mathrm{anchor}}(r^{\mathrm{anchor}})$ and its derivative
% $F(r^{\mathrm{anchor}})$ using this MATLAB script. This produces a table that can be
% saved (e.g., as 'table_bonds_stage2.dat') containing columns for $r^{\mathrm{anchor}}$,
% $U^{\mathrm{anchor}}$, and $F$, which can be used in LAMMPS simulations with the
% `pair_style table` command.

% Clear all existing variables and workspace
clear;
% Define the cutoff distance for the anchor interaction
distance = 3;
% Create an index array for data output (not used in calculation)
n = (1:4001)';
% Define the range of distances to evaluate the potential and force
d = (0:0.05:4000*0.05)';

% Define a step function: 1 when d >= cutoff distance, else 0
heaviside_step = double(d >= distance);

% Compute the potential: linear increase after cutoff distance
U = heaviside_step .* abs(d - distance) * 10;
% Compute the force as the negative derivative of potential
DU = -10 * heaviside_step;

% Plot potential and force
figure('Position', [100, 100, 1000, 400]);

% Plot potential vs. distance
subplot(1, 2, 1)
plot(d, U, 'b', 'LineWidth', 4);
hold on
xline(distance, '--k', 'LineWidth', 1.5)
xlabel('$r^{\mathrm{anchor}}$', 'Interpreter', 'latex', 'FontSize', 20)
ylabel('$U^{\mathrm{anchor}}(r^{\mathrm{anchor}})$', 'Interpreter', 'latex', 'FontSize', 20)
title('Potential Function', 'FontSize', 16)
set(gca, 'FontSize', 20)
xlim([-1 10])
ylim([0 80])
grid on
legend({'$U^{\mathrm{anchor}}$', '$r^{\mathrm{anchor}}_0 = 3$'}, 'Interpreter', 'latex', 'FontSize', 20)

% Plot force vs. distance
subplot(1, 2, 2)
plot(d, DU, 'Color', [1 0.5 0], 'LineWidth', 4);
hold on
xline(distance, '--k', 'LineWidth', 1.5)
xlabel('$r^{\mathrm{anchor}}$', 'Interpreter', 'latex', 'FontSize', 20)
ylabel('$F(r^{\mathrm{anchor}})$', 'Interpreter', 'latex', 'FontSize', 20)
title('Force Function', 'FontSize', 20)
set(gca, 'FontSize', 20)
xlim([-1 10])
ylim([-15 1])
grid on
legend({'$F(r^{\mathrm{anchor}})$', '$r^{\mathrm{anchor}}_0 = 3$'}, 'Interpreter', 'latex', 'FontSize', 12)

% Combine data into a single matrix for saving or further analysis
final = [n, d, U, DU];
