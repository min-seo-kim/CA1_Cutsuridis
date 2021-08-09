import numpy as np

volthresh = -55
avgvolthresh = -56
StepBy = 50

for mgconc in [0.0, 0.1, 0.5, 1.0, 1.5, 2.0, 5.0]:
    fstem = "pyresults/mg_{}".format(mgconc)
    print("Now investigating simulation", fstem)
    for i in range(20):
        v_overtime = np.loadtxt("{}_cellv_{}.dat".format(fstem,i),skiprows=1)
        for t in range(StepBy,1550,StepBy):
            v_last_300 = v_overtime[int(t//0.025)-300:int(t//0.025),1]
            # print("Checking time interval from index", int(t//0.025)-300, "to", int(t//0.025))
            mean = np.mean(v_last_300)
            mini = np.min(v_last_300)
            
            if (mini > volthresh):
                print("Cell ", i, " died at t = ", t, " due to mini = ", mini)
                break
            elif (mean > volthresh):
                print("Cell ", i, " died at t = ", t, " due to mean = ", mean)
                break
            else:
                # print("Cell ", i, " lives at t = ", t)
                pass
                