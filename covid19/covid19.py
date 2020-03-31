import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import geom

debug = 0

# global params
num_weeks = 2 # number of weeks
num_dpw = 7 # number of days per week
covid19_penalty = 14
horizon = num_dpw * num_weeks
days = np.arange(horizon)
# success prob to obtain supply for one day
p_supply = [0.5] * horizon
for k in range(1, horizon, num_dpw):
    p_supply[k] = 0.9
# prob of getting covid-19 on a supply run
p_covid19 = [0.1] * horizon
for k in range(1, horizon//2):
    p_covid19[k] = p_covid19[k - 1] + 0.01
for k in range(horizon//2, horizon):
    p_covid19[k] = p_covid19[k - 1] - 0.01
if debug >= 1:
    plt.figure(); plt.stem(p_supply); plt.title('Probability of a successful supply run')
    plt.figure(); plt.stem(p_covid19); plt.title('Probability of getting covid-19 in a supply run')


max_state = 14
min_state = -7
states = set(np.arange(min_state, max_state, 1))
actions = set(np.arange(2))

def reward(s):
    if s > 0:
        return 1
    else:
        return 0

def next_state_prob(s, a, p_supply_cur, p_covid19_cur):
    p_s_next = {s_next: 0 for s_next in states}
    if a == 0:
        s_next = max(min_state, s - 1)
        p_s_next[s_next] = 1
    else:
        for s_next in states:
            if s_next == max(min_state, s - covid19_penalty):
                p_s_next[s_next] = p_covid19_cur
            elif s_next >= s:
                p_s_next[s_next] = (1 - p_covid19_cur) * geom.pmf(s_next - s + 1, p_supply_cur)

        if debug >= 1:
            p_s_next_x = sorted(p_s_next.keys())
            p_s_next_y = [p_s_next[k] for k in p_s_next_x]
            plt.figure(); plt.stem(p_s_next_x, p_s_next_y)

        p_total = sum(p_s_next.values())
        for s_next in states:
            p_s_next[s_next] = p_s_next[s_next] / p_total

    return p_s_next

def visualize(day, fun):
    fun_day = {s: fun[(s, day)] for s in states}
    plt.figure(); plt.stem(fun_day.keys(), fun_day.values()); plt.title('Day %d' % day)
    return

def optimize():
    # initialize
    valfun = {(s, horizon - 1): reward(s) for s in states}
    policy = {(s, horizon - 1): 0 for s in states}

    # recursively apply Bellman's equation
    for day in range(horizon - 2, -1, -1):
        p_covid19_cur = p_covid19[day]
        p_supply_cur = p_supply[day]

        Q = {(s, a): 0 for s in states for a in actions}
        for s in states:
            for a in actions:
                p_s_next = next_state_prob(s, a, p_supply_cur, p_covid19_cur)
                Q[(s, a)] = sum([p_s_next[s_next] * valfun[(s_next, day+1)] for s_next in states])

            Q_s = {a: Q[(s,a)] for a in actions}
            policy[(s, day)] = max(Q_s, key = Q_s.get)
            valfun[(s, day)] = Q_s[policy[(s, day)]]
          
    return valfun, policy
