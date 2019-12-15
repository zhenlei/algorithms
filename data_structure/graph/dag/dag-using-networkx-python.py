'''Find the ordering of tasks from given dependencies
refer to python networkx lib
https://ipython.org/ipython-doc/stable/parallel/dag_dependencies.html#why-are-dags-good-for-task-dependencies

There are a total of n tasks you have to pick, labeled from 0 to n-1. Some tasks may have
prerequisites tasks, for example to pick task 0 you have to first finish tasks 1, which is
expressed as a pair: [0, 1]

Given the total number of tasks and a list of prerequisite pairs, return the ordering of tasks you
should pick to finish all tasks.

There may be multiple correct orders, you just need to return one of them. If it is impossible to
finish all tasks, return an empty array.

'''

import networkx as nx

G = nx.DiGraph()

# add 5 nodes, labeled 0-4:
map(G.add_node, range(5))
# 1,2 depend on 0:
G.add_edge(0,1)
G.add_edge(0,2)
# 3 depends on 1,2
G.add_edge(1,3)
G.add_edge(2,3)
# 4 depends on 1
G.add_edge(1,4)

# now draw the graph:
pos = { 0 : (0,0), 1 : (1,1), 2 : (-1,1),
        3 : (0,2), 4 : (2,2)}
nx.draw(G, pos, edge_color='r')


import ipyparallel as ipp
import random
from functools import partial
import time

rc = ipp.Client()
view = rc.load_balanced_view()

def randwait(t):
    time.sleep(t)
    print('sleep duration', t)

jobs = dict()
for node in G:
    jobs[node] = partial(randwait, random.random())

results = dict()
for node in nx.topological_sort(G):
   # get list of AsyncResult objects from nodes
   # leading into this one as dependencies
   deps = [ results[n] for n in G.predecessors(node) ]
   # submit and store AsyncResult object
   with view.temp_flags(after=deps, block=False):
        results[node] = view.apply(jobs[node])

print(results)
view.wait(results.values())


def validate_tree(G, results):
    """Validate that jobs executed after their dependencies."""
    for node in G:
        started = results[node].metadata.started
        for parent in G.predecessors(node):
            finished = results[parent].metadata.completed
            assert started > finished, "%s should have happened after %s"%(node, parent)

validate_tree(G, results)

from matplotlib.dates import date2num

from matplotlib.cm import gist_rainbow

pos = {}; colors = {}

for node in G:
   md = results[node].metadata
   start = date2num(md.started)
   runtime = date2num(md.completed) - start
   pos[node] = (start, runtime)
   colors[node] = md.engine_id

nx.draw(G, pos, node_list=colors.keys(), node_color=colors.values(),
   cmap=gist_rainbow)
