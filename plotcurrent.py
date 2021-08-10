import numpy as np
import matplotlib.pyplot as plt

for mgconc in [0.0, 0.5, 1.0, 2.0]:
    fstem = "pyresults/mg_{}".format(mgconc)
    spks1 = np.loadtxt("{}_celli_0.dat".format(fstem),skiprows=1)
    spks2 = np.loadtxt("{}_celli_1.dat".format(fstem),skiprows=1)
    plt.figure(figsize=(8,10))
    plt.subplot(2,1,1)
    plt.plot(spks1[:,0],0.84*spks1[:,1],'b',label='Nonpattern')
    plt.ylabel("Current (nA)")
    plt.ylim([-0.23, 0.01])
    plt.title("Pyramidal Cell at Mg = {} mM".format(mgconc))
    plt.legend(loc='upper right')
    plt.subplot(2,1,2)
    plt.plot(spks2[:,0],0.84*spks2[:,1],'r',label='Pattern')
    plt.xlabel("Time (ms)")
    plt.ylabel("Current (nA)")   
    plt.ylim([-0.23, 0.01])
    plt.legend(loc='upper right')
    plt.show()