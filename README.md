# Semi-Generative-CAPP
This is my undergrad assignment work in a subject called Process Planning and Cost Estimation. 
Its kinda semi-generative CAPP for shaft like components.

This code is written and tested in Google Colaboratory. Connect to local Runtime before execution.

Before using it you have to know how to code a shaft, which is the input for the program.
You can easily understand it.

For example :

code = [['ch',1,3,45,'l'],['D',1,20,30,'A'],['T',1,25,50],['T',2,50,75],['T',3,35,80],['T',4,70,90]]

 in this, taking the first element alone
 
 ['ch',1,3,45,'l']
 
 ch - chamfer,
 
 1 - first of its kind (chamfer),
 
 3 - length of chamfer,
 
 45 - angle,
 
 l - left side.
 
 the shaft is coded as per the operations to be done on it.
 From left to right.                                                                                                       ________________________T4_90______________________
                                                                                                                          |                                                    \ 
                                    _________________T2_75________________                                                |                                                    |
                                   |                                      |                                               |                                                    |
                                   |                                      |_____________________T3_80_____________________|                                                    |
                                   |                                                                                                                                           |
    ___________T1_50_______________|                                                                                                                                           |
   /                                                                                                                                                                           |
  |_  _  _ 30 _ _                                                                                                                                                              |
  |              |                                                                                                                                                             |
- - 20 - - -  -  A  -  -  25 -  -  -  -  -  -  -  - 50 -  -  -  -  -  -  -  -  -  -  -  -  -  -  35  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - 70  -  -  -  -  -  -  -  - |
  |_  _  _  _  _ |                                                                                                                                                             |
  |   Drilling                                                                                                                                                                 |
   \________________________________                                                                                                                                           |
chamfer           Turning           |                                                                                                                                          |
                                    |                                     __________________________________________________                                                   |
                                    |                                    |                     Turning                      |                                                  |
                                    |____________________________________|                                                  |                                                  |
                                                   Turning                                                                  |                                                  |
                                                                                                                            |_________________________________________________ /
                                                                                                                                                Turning                  Chamfer
                                                                                                                                                
                                                                                                                                             NOT TO SCALE
 All the data used in the code is taken from the book "Process planning" by Peter Scallan.
 
 Import all the necessary libraries before executing.
