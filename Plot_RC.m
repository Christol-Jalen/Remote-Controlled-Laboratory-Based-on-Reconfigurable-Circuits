f=[0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
2
3
4
5
6
7
8
9
10
20
30
40
50
60
70
80
90
100
];  %copy the excel column containing your frequency points, position the cursor between the square brackets, and paste right there

Vin=[4.13
4.1
4.08
4.08
4.07
4.07
4.07
4.06
4.06
4.06
3.99
3.95
3.92
3.92
3.9
3.9
3.9
3.9
3.89
3.89
3.89
3.89
3.89
3.89
3.88
3.89
3.89
3.88
]; %copy the excel column containing your Vin values, position the cursor between the square brackets, and paste right there

Vout_P=[4.12
4.09
4.05
3.98
3.9
3.74
3.63
3.54
3.5
3.43
2.48
1.88
1.5
1.24
1.07
0.935
0.81
0.73
0.664
0.37
0.266
0.227
0.187
0.176
0.165
0.15
0.135
0.12
]  % copy the excel column containing your Vout values, position the cursor between the square brackets, and paste right there
Vout_N=[4.12
4.1
4.04
4
3.93
3.87
3.8
3.69
3.59
3.51
2.65
2.02
1.63
1.37
1.19
0.994
0.867
0.793
0.694
0.374
0.266
0.199
0.164
0.138
0.122
0.11
0.097
0.09
]

phase_diff_P=[-3.41
-6.98
-10.39
-13.86
-17.21
-21.76
-24.12
-26.48
-30.07
-32.01
-49.05
-58.35
-65.52
-68.99
-71.46
-73.7
-74.26
-74.45
-73.79
-73.32
-72.52
-65.97
-61.77
-56.85
-50.83
-44.31
-39.21
-33.33
]  % copy the excel column containing the phase difference between i/p and o/p voltage, position the cursor between the square brackets, and paste right there
phase_diff_N=[-3.3
-6.6
-10.49
-13.2
-16.1
-18.89
-22.88
-24.77
-28.13
-30.58
-48.35
-59.02
-66.97
-70.53
-73.46
-77.13
-79.55
-79.96
-80.85
-83.31
-83.86
-84.54
-84.95
-85.4
-85.86
-86.22
-86.81
-87.14
]  % you can use degrees or radians. I recommend that you use
                 % degrees
simu_gain = [0.1	-0.0171115
0.112202	-0.0215311
0.125893	-0.0270887
0.141254	-0.0340753
0.158489	-0.0428548
0.177828	-0.0538824
0.199526	-0.0677257
0.223872	-0.0850908
0.251189	-0.106854
0.281838	-0.134098
0.316228	-0.168155
0.354813	-0.210654
0.398107	-0.263572
0.446684	-0.329288
0.501187	-0.41063
0.562341	-0.510914
0.630957	-0.633958
0.707946	-0.784063
0.794328	-0.965944
0.891251	-1.18459
1	-1.44507
1.12202	-1.75223
1.25893	-2.11038
1.41254	-2.52294
1.58489	-2.99214
1.77828	-3.51877
1.99526	-4.10214
2.23872	-4.74013
2.51189	-5.4294
2.81838	-6.16568
3.16228	-6.94416
3.54813	-7.75977
3.98107	-8.60752
4.46684	-9.48265
5.01187	-10.3808
5.62341	-11.2982
6.30957	-12.2315
7.07946	-13.1777
7.94328	-14.1345
8.91251	-15.0999
10	-16.0722
11.2202	-17.0501
12.5893	-18.0325
14.1254	-19.0184
15.8489	-20.0072
17.7828	-20.9982
19.9526	-21.9911
22.3872	-22.9855
25.1189	-23.981
28.1838	-24.9774
31.6228	-25.9746
35.4813	-26.9723
39.8107	-27.9705
44.6684	-28.9691
50.1187	-29.968
56.2341	-30.9671
63.0957	-31.9664
70.7946	-32.9658
79.4328	-33.9653
89.1251	-34.965
100	-35.9647
];

simu_phase = [0.1	-3.59527
0.112202	-4.03259
0.125893	-4.52271
0.141254	-5.07185
0.158489	-5.68687
0.177828	-6.37536
0.199526	-7.14566
0.223872	-8.00686
0.251189	-8.96881
0.281838	-10.0421
0.316228	-11.2378
0.354813	-12.5678
0.398107	-14.0437
0.446684	-15.6773
0.501187	-17.4795
0.562341	-19.4598
0.630957	-21.6255
0.707946	-23.9802
0.794328	-26.5234
0.891251	-29.2484
1	-32.1419
1.12202	-35.1833
1.25893	-38.3442
1.41254	-41.5898
1.58489	-44.8799
1.77828	-48.1716
1.99526	-51.4219
2.23872	-54.5903
2.51189	-57.6414
2.81838	-60.5465
3.16228	-63.2842
3.54813	-65.8409
3.98107	-68.2095
4.46684	-70.3888
5.01187	-72.3824
5.62341	-74.1973
6.30957	-75.8428
7.07946	-77.3299
7.94328	-78.67
8.91251	-79.8751
10	-80.9569
11.2202	-81.9266
12.5893	-82.7948
14.1254	-83.5714
15.8489	-84.2656
17.7828	-84.8857
19.9526	-85.4394
22.3872	-85.9336
25.1189	-86.3745
28.1838	-86.7679
31.6228	-87.1188
35.4813	-87.4317
39.8107	-87.7107
44.6684	-87.9594
50.1187	-88.1812
56.2341	-88.3788
63.0957	-88.5551
70.7946	-88.7121
79.4328	-88.8522
89.1251	-88.977
100	-89.0882
];


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
