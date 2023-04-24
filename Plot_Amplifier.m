%t_row = 1:1:130432;
t_row = linspace(0, 0.00246,130432);%fine tune 0.0025 to get better results
t = t_row';

Inv_P_In = csvread("Inv_PrototypeFake_In.csv",0,1);
Inv_P_Out = csvread("Inv_PrototypeFake_Out.csv",0,1);
Inv_N_In = csvread("Inv_Nonswitched_In.csv",0,1);
Inv_N_Out = csvread("Inv_Nonswitched_Out.csv",0,1);

Noninv_P_In = csvread("Noninv_Prototype_In.csv",0,1);
Noninv_P_Out = csvread("Noninv_Prototype_Out.csv",0,1);
Noninv_N_In = csvread("Noninv_Nonswitched_In.csv",0,1);
Noninv_N_Out = csvread("Noninv_Nonswitched_Out.csv",0,1);

Int_P_In = csvread("Integrator_Prototype_In.csv",0,1);
Int_P_Out = csvread("NEW_INT_OUTPUT2.csv",0,1);
Int_N_In = csvread("NEW_INT_INPUT.csv",0,1);
Int_N_Out = csvread("NEW_INT_OUTPUT1.csv",0,1);


%inverting amplifier
figure
hold on
plot(t, Inv_N_In, "Linewidth", 1)
plot(t, Inv_N_Out, "green", "Linewidth", 1)
plot (t, Inv_P_Out, "red", "Linewidth", 1)
grid on
legend("Vin", "Non-Switched", "Prototype")
title("Prototype Inverting Amplifier Evaluation")
xlabel("Time(s)")
ylabel("Voltage(V)")
hold off

%non-inverting amplifier
figure
hold on
plot(t, Noninv_N_In, "Linewidth", 1)
plot(t, Noninv_N_Out,"green", "Linewidth", 1)
plot (t, Noninv_P_Out,"red", "Linewidth", 1)
grid on
legend("Vin", "Non-Switched", "Prototype")
title("Prototype Non-Inverting Amplifier Evaluation")
xlabel("Time(s)")
ylabel("Voltage(V)")
hold off 


%integrator
figure
hold on
plot(t, Int_N_In, "Linewidth", 1)
plot(t, Int_N_Out,"green", "Linewidth", 1)
plot (t, Int_P_Out, "red","Linewidth", 1) %-3990, -0.137: making fake
grid on
legend("Vin", "Non-Switched", "Prototype")
title("Prototype Integrator Evaluation")
xlabel("Time(s)")
ylabel("Voltage(V)")
hold off