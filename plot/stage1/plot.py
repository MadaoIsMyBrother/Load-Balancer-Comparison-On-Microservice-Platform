import matplotlib.pyplot as plt
import math

def plot_percentile(path):
    lines = open(path).readlines()
    x = []
    y = []
    for line in lines:
        content = line.split()
        x.append(float(content[1]))
        y.append(math.log(float(content[0])))
    l = path.split('.')[0]
    plt.plot(x, y, label=f'{l}')  

# plot_percentile("r=5 c=10.txt")
# plot_percentile("r=10 c=10.txt")
plot_percentile("r=10 c=1 t=1.txt")
plot_percentile("r=100 c=1 t=1.txt")
plot_percentile("r=1000 c=1 t=1.txt")
plot_percentile("r=10000 c=1 t=1.txt")
plot_percentile("r=10000 c=100 t=1.txt")
plot_percentile("r=10000 c=100 t=2.txt")
plot_percentile("r=10000 c=100 t=100.txt")
# plot_percentile("r=100 c=10.txt")
plt.xlabel("percentile")
plt.ylabel("log(latency) (ms)")
plt.grid(True)
plt.legend()
plt.savefig("percentile.png")