import matplotlib.pyplot as plt
import pandas as pd
import sys
import glob

files = glob.glob("./results/results_*.csv")
files = glob.glob("./results/results_1*.csv") #tu samo bez acera

for file in files:
    name = file.split("./results/results_")[1][:-4]
    df = pd.read_csv(file)
    x = df["time_step"]
    y = df["eval_return_mean"]
    y_err = df["eval_std_mean"]
    plt.plot(x, y, '-', label=name)
    plt.fill_between(x, y - y_err, y + y_err, alpha=0.2)


plt.xlabel("Timestamps")
plt.ylabel("Evaluation function values")
plt.legend(loc='lower right')
plt.grid()
if len(sys.argv)>1:
    plt.savefig("./results/"+sys.argv[1])
else:
    plt.savefig("./results/plot")

