import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math


# Question 1
def coin_toss(p=1/2, throws=20):
    # T = 0, H = 1
    throws = random.choices([0, 1], weights=[1-p, p], k=throws)
    return sum(throws)


outcome = []
for i in range(1000):
    outcome.append(coin_toss())

plt.subplot(1, 2, 1)
plt.hist(x=outcome, bins='auto')
plt.subplot(1, 2, 2)
plt.bar([x for x in range(21)], [stats.binom.pmf(x, 20, 1/2) for x in range(21)])
plt.show()

outcome = []
for i in range(1000):
    outcome.append(coin_toss(p=1/3))

plt.subplot(1, 2, 1)
plt.hist(x=outcome, bins='auto')
plt.subplot(1, 2, 2)
plt.bar([x for x in range(21)], [stats.binom.pmf(x, 20, 1/3) for x in range(21)])
plt.show()


# Question 2
def first_head(counter=1):
    throw = random.choices([0, 1], weights=[0.6, 0.4], k=1)[0]
    if throw != 1:
        counter += 1
        first_head(counter)
    else:
        globals()["counter"] = counter


coin_results = []
for i in range(1000):
    first_head()
    coin_results.append(globals()["counter"])


def pmf(p=0.4, k=15):
    pmf_results = []
    for i in range(k):
        p_x = (1-p)**(i-1) * p
        pmf_results.append(p_x)
    globals()["pmf_results"] = pmf_results


pmf()
pmf_results

plt.subplot(1, 2, 1)
plt.hist(x=coin_results, bins='auto')
plt.subplot(1, 2, 2)
plt.bar([x + 1for x in range(len(pmf_results))], pmf_results)
plt.show()

# Question 3
# A standard normal random variable is a normally distributed random variable with mean 0 and standard deviation = 1
x = np.linspace(-4, 4, 100)
plt.plot(x, stats.norm.pdf(x))

neg_x = stats.norm.pdf([x for x in x if x < 0])
pos_x = stats.norm.pdf(list(reversed([x for x in x if x > 0])))

# len(neg_x) == len(pos_x)
symmetric = []
for i in range(len(neg_x)):
    symmetric.append(math.isclose(neg_x[i], pos_x[i], abs_tol=1e-20))

all(symmetric)

plt.plot(x, stats.norm.pdf(x))
plt.axvline(x=stats.norm.ppf(0.975), color="red")
plt.axvline(x=-stats.norm.ppf(0.975), color="red")

pos_a = stats.norm.ppf(0.975)
neg_a = -stats.norm.ppf(0.975)

size = 10000
std_norm_var = np.random.normal(loc=0, scale=1, size=size)
len([x for x in std_norm_var if neg_a <= x <= pos_a]) / size

