import numpy as np
import matplotlib.pyplot as plt

for i in range(20):
    fstem = "pyresults/mg_5.0"
    spks = np.loadtxt("{}_celli_{}.dat".format(fstem,i),skiprows=1)
    plt.figure()
    plt.plot(spks[:,0],0.84*spks[:,1])
    plt.xlabel("Time (ms)")
    plt.ylabel("Current (nA)")    
    plt.title("Pyramidal Cell {}".format(i))
    plt.show()