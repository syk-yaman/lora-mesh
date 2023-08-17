(G-CODE GENERATED BY FLATCAM v8.994 - www.flatcam.org - Version Date: 2020/11/7)

(Name: copper_bottom.gbr_cutout_cnc)
(Type: G-code from Geometry)
(Units: MM)

(Created on Wednesday, 09 August 2023 at 20:52)

(This preprocessor is the default preprocessor used by FlatCAM.)
(It is made to work with MACH3 compatible motion controllers.)

(TOOL DIAMETER: 1.0 mm)
(Feedrate_XY: 120.0 mm/min)
(Feedrate_Z: 60.0 mm/min)
(Feedrate rapids 1500.0 mm/min)

(Z_Cut: -1.8 mm)
(DepthPerCut: 0.6 mm <=>3 passes)
(Z_Move: 2.0 mm)
(Z Start: None mm)
(Z End: 15.0 mm)
(X,Y End: None mm)
(Steps per circle: 64)
(Preprocessor Geometry: default)

(X range:   20.4161 ...   89.7389  mm)
(Y range:   21.2111 ...   89.5839  mm)

(Spindle Speed: 0.0 RPM)
G21
G90
G94

G01 F120.00

M5
G00 Z15.0000
G00 X0.0000 Y0.0000
T1
M6    
(MSG, Change to Tool Dia = 1.0000)
M0
G00 Z15.0000

M03
G01 F120.00
G00 X52.6775 Y21.2111
G01 F60.00
G01 Z-0.6000
G01 F120.00
G01 X21.0161 Y21.2111
G01 X20.9573 Y21.2140
G01 X20.8990 Y21.2226
G01 X20.8419 Y21.2369
G01 X20.7865 Y21.2568
G01 X20.7333 Y21.2819
G01 X20.6828 Y21.3122
G01 X20.6355 Y21.3473
G01 X20.5918 Y21.3868
G01 X20.5523 Y21.4305
G01 X20.5172 Y21.4778
G01 X20.4869 Y21.5283
G01 X20.4618 Y21.5815
G01 X20.4419 Y21.6369
G01 X20.4276 Y21.6940
G01 X20.4190 Y21.7523
G01 X20.4161 Y21.8111
G01 X20.4161 Y52.9975
G00 X20.4161 Y52.9975
G01 F60.00
G01 Z-1.2000
G01 F120.00
G01 X20.4161 Y21.8111
G01 X20.4190 Y21.7523
G01 X20.4276 Y21.6940
G01 X20.4419 Y21.6369
G01 X20.4618 Y21.5815
G01 X20.4869 Y21.5283
G01 X20.5172 Y21.4778
G01 X20.5523 Y21.4305
G01 X20.5918 Y21.3868
G01 X20.6355 Y21.3473
G01 X20.6828 Y21.3122
G01 X20.7333 Y21.2819
G01 X20.7865 Y21.2568
G01 X20.8419 Y21.2369
G01 X20.8990 Y21.2226
G01 X20.9573 Y21.2140
G01 X21.0161 Y21.2111
G01 X52.6775 Y21.2111
G00 X52.6775 Y21.2111
G01 F60.00
G01 Z-1.8000
G01 F120.00
G01 X21.0161 Y21.2111
G01 X20.9573 Y21.2140
G01 X20.8990 Y21.2226
G01 X20.8419 Y21.2369
G01 X20.7865 Y21.2568
G01 X20.7333 Y21.2819
G01 X20.6828 Y21.3122
G01 X20.6355 Y21.3473
G01 X20.5918 Y21.3868
G01 X20.5523 Y21.4305
G01 X20.5172 Y21.4778
G01 X20.4869 Y21.5283
G01 X20.4618 Y21.5815
G01 X20.4419 Y21.6369
G01 X20.4276 Y21.6940
G01 X20.4190 Y21.7523
G01 X20.4161 Y21.8111
G01 X20.4161 Y52.9975
G00 Z2.0000
G00 X20.4161 Y57.9975
G01 F60.00
G01 Z-0.6000
G01 F120.00
G01 X20.4161 Y88.9839
G01 X20.4190 Y89.0427
G01 X20.4276 Y89.1010
G01 X20.4419 Y89.1581
G01 X20.4618 Y89.2135
G01 X20.4869 Y89.2667
G01 X20.5172 Y89.3172
G01 X20.5523 Y89.3645
G01 X20.5918 Y89.4082
G01 X20.6355 Y89.4477
G01 X20.6828 Y89.4828
G01 X20.7333 Y89.5131
G01 X20.7865 Y89.5382
G01 X20.8419 Y89.5581
G01 X20.8990 Y89.5724
G01 X20.9573 Y89.5810
G01 X21.0161 Y89.5839
G01 X52.6775 Y89.5839
G00 X52.6775 Y89.5839
G01 F60.00
G01 Z-1.2000
G01 F120.00
G01 X21.0161 Y89.5839
G01 X20.9573 Y89.5810
G01 X20.8990 Y89.5724
G01 X20.8419 Y89.5581
G01 X20.7865 Y89.5382
G01 X20.7333 Y89.5131
G01 X20.6828 Y89.4828
G01 X20.6355 Y89.4477
G01 X20.5918 Y89.4082
G01 X20.5523 Y89.3645
G01 X20.5172 Y89.3172
G01 X20.4869 Y89.2667
G01 X20.4618 Y89.2135
G01 X20.4419 Y89.1581
G01 X20.4276 Y89.1010
G01 X20.4190 Y89.0427
G01 X20.4161 Y88.9839
G01 X20.4161 Y57.9975
G00 X20.4161 Y57.9975
G01 F60.00
G01 Z-1.8000
G01 F120.00
G01 X20.4161 Y88.9839
G01 X20.4190 Y89.0427
G01 X20.4276 Y89.1010
G01 X20.4419 Y89.1581
G01 X20.4618 Y89.2135
G01 X20.4869 Y89.2667
G01 X20.5172 Y89.3172
G01 X20.5523 Y89.3645
G01 X20.5918 Y89.4082
G01 X20.6355 Y89.4477
G01 X20.6828 Y89.4828
G01 X20.7333 Y89.5131
G01 X20.7865 Y89.5382
G01 X20.8419 Y89.5581
G01 X20.8990 Y89.5724
G01 X20.9573 Y89.5810
G01 X21.0161 Y89.5839
G01 X52.6775 Y89.5839
G00 Z2.0000
G00 X57.6775 Y89.5839
G01 F60.00
G01 Z-0.6000
G01 F120.00
G01 X89.1389 Y89.5839
G01 X89.1977 Y89.5810
G01 X89.2560 Y89.5724
G01 X89.3131 Y89.5581
G01 X89.3685 Y89.5382
G01 X89.4217 Y89.5131
G01 X89.4722 Y89.4828
G01 X89.5195 Y89.4477
G01 X89.5632 Y89.4082
G01 X89.6027 Y89.3645
G01 X89.6378 Y89.3172
G01 X89.6681 Y89.2667
G01 X89.6932 Y89.2135
G01 X89.7131 Y89.1581
G01 X89.7274 Y89.1010
G01 X89.7360 Y89.0427
G01 X89.7389 Y88.9839
G01 X89.7389 Y57.9975
G00 X89.7389 Y57.9975
G01 F60.00
G01 Z-1.2000
G01 F120.00
G01 X89.7389 Y88.9839
G01 X89.7360 Y89.0427
G01 X89.7274 Y89.1010
G01 X89.7131 Y89.1581
G01 X89.6932 Y89.2135
G01 X89.6681 Y89.2667
G01 X89.6378 Y89.3172
G01 X89.6027 Y89.3645
G01 X89.5632 Y89.4082
G01 X89.5195 Y89.4477
G01 X89.4722 Y89.4828
G01 X89.4217 Y89.5131
G01 X89.3685 Y89.5382
G01 X89.3131 Y89.5581
G01 X89.2560 Y89.5724
G01 X89.1977 Y89.5810
G01 X89.1389 Y89.5839
G01 X57.6775 Y89.5839
G00 X57.6775 Y89.5839
G01 F60.00
G01 Z-1.8000
G01 F120.00
G01 X89.1389 Y89.5839
G01 X89.1977 Y89.5810
G01 X89.2560 Y89.5724
G01 X89.3131 Y89.5581
G01 X89.3685 Y89.5382
G01 X89.4217 Y89.5131
G01 X89.4722 Y89.4828
G01 X89.5195 Y89.4477
G01 X89.5632 Y89.4082
G01 X89.6027 Y89.3645
G01 X89.6378 Y89.3172
G01 X89.6681 Y89.2667
G01 X89.6932 Y89.2135
G01 X89.7131 Y89.1581
G01 X89.7274 Y89.1010
G01 X89.7360 Y89.0427
G01 X89.7389 Y88.9839
G01 X89.7389 Y57.9975
G00 Z2.0000
G00 X89.7389 Y52.9975
G01 F60.00
G01 Z-0.6000
G01 F120.00
G01 X89.7389 Y21.8111
G01 X89.7360 Y21.7523
G01 X89.7274 Y21.6940
G01 X89.7131 Y21.6369
G01 X89.6932 Y21.5815
G01 X89.6681 Y21.5283
G01 X89.6378 Y21.4778
G01 X89.6027 Y21.4305
G01 X89.5632 Y21.3868
G01 X89.5195 Y21.3473
G01 X89.4722 Y21.3122
G01 X89.4217 Y21.2819
G01 X89.3685 Y21.2568
G01 X89.3131 Y21.2369
G01 X89.2560 Y21.2226
G01 X89.1977 Y21.2140
G01 X89.1389 Y21.2111
G01 X57.6775 Y21.2111
G00 X57.6775 Y21.2111
G01 F60.00
G01 Z-1.2000
G01 F120.00
G01 X89.1389 Y21.2111
G01 X89.1977 Y21.2140
G01 X89.2560 Y21.2226
G01 X89.3131 Y21.2369
G01 X89.3685 Y21.2568
G01 X89.4217 Y21.2819
G01 X89.4722 Y21.3122
G01 X89.5195 Y21.3473
G01 X89.5632 Y21.3868
G01 X89.6027 Y21.4305
G01 X89.6378 Y21.4778
G01 X89.6681 Y21.5283
G01 X89.6932 Y21.5815
G01 X89.7131 Y21.6369
G01 X89.7274 Y21.6940
G01 X89.7360 Y21.7523
G01 X89.7389 Y21.8111
G01 X89.7389 Y52.9975
G00 X89.7389 Y52.9975
G01 F60.00
G01 Z-1.8000
G01 F120.00
G01 X89.7389 Y21.8111
G01 X89.7360 Y21.7523
G01 X89.7274 Y21.6940
G01 X89.7131 Y21.6369
G01 X89.6932 Y21.5815
G01 X89.6681 Y21.5283
G01 X89.6378 Y21.4778
G01 X89.6027 Y21.4305
G01 X89.5632 Y21.3868
G01 X89.5195 Y21.3473
G01 X89.4722 Y21.3122
G01 X89.4217 Y21.2819
G01 X89.3685 Y21.2568
G01 X89.3131 Y21.2369
G01 X89.2560 Y21.2226
G01 X89.1977 Y21.2140
G01 X89.1389 Y21.2111
G01 X57.6775 Y21.2111
G00 Z2.0000
M05
G00 Z2.0000
G00 Z15.00

