f=[];  %copy the excel column containing your frequency points, position the cursor between the square brackets, and paste right there

Vin=[]; %copy the excel column containing your Vin values, position the cursor between the square brackets, and paste right there

Vout_P=[];  % copy the excel column containing your Vout values, position the cursor between the square brackets, and paste right there
Vout_N=[];

phase_diff_P=[];  % copy the excel column containing the phase difference between i/p and o/p voltage, position the cursor between the square brackets, and paste right there
phase_diff_N=[];  
simu_gain = [];
simu_phase = [];


%% LOG PLOT of AMPLITUDE AND PHASE OF THE TRANSFER FUNCTION

% You do NOT need to change this code

H_amp_P = Vout_P./Vin;
H_amp_N = Vout_N./Vin;
H_amp_P_dB = 20*log10(H_amp_P);
H_amp_N_dB = 20*log10(H_amp_N);

%figure  
%semilogx(f,H_amp_P, "Linewidth", 1);
%hold on
%semilogx(f,H_amp_N, "Linewidth", 1);
%xlabel('Frequency (Hz)')
%grid;
%legend("Prototype", "Non-Switched")
%title('Magnitude of the transfer function')

figure
semilogx(f,H_amp_N_dB, "green", "Linewidth", 1);
hold on
semilogx(f,H_amp_P_dB, "red", "Linewidth", 1);
semilogx(simu_gain(:,1),simu_gain(:,2), "blue","Linewidth", 1);
ylabel('dB')
xlabel('Frequency (kHz)')
grid;
legend("Non-Switched", "Prototype", "Simulation")
title('Prototype Passive Circuit Evaluation (Gain)')


figure
semilogx(f,phase_diff_N, "green", "Linewidth", 1);
hold on
semilogx(f,phase_diff_P, "red", "Linewidth", 1);
semilogx(simu_phase(:,1),simu_phase(:,2),"blue", "Linewidth", 1);
xlabel('Frequency (kHz)')
ylabel('deg')
grid;
legend("Non-Switched", "Prototype", "Simulation")
title('Prototype Passive Circuit Evaluation (Phase)')
