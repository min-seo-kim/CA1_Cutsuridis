import numpy as np
import matplotlib.pyplot as plt
    
mgconcs = [round(0.2*i,1) for i in list(range(11))]
nonpattern_avg = []
pattern_avg= []

for mgconc in mgconcs: 
    nonpattern_spks = np.loadtxt("pyresults/mgf_{}_celli_0.dat".format(mgconc),skiprows=1)
    nonpattern_cot = nonpattern_spks[:,1]
    nonpattern_avg.append(np.mean(nonpattern_cot))
    pattern_spks = np.loadtxt("pyresults/mgf_{}_celli_1.dat".format(mgconc),skiprows=1)
    pattern_cot = pattern_spks[:,1]
    pattern_avg.append(np.mean(pattern_cot))

x = np.arange(len(mgconcs))
plt.figure(figsize=(12,10))
plt.plot(x,nonpattern_avg,'o-',label='Nonpattern')
plt.plot(x,pattern_avg,'s-',label='Pattern')
plt.xticks(x,mgconcs)
plt.xlabel('Magnesium Concentration (mM)')
plt.ylabel('Average Current (nA)')
plt.legend(loc='upper left')
plt.title('Average Current vs. Mg Concentration')
plt.show()

    