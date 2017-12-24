import sys
import re
import itertools

def read(line):
    return [int(port) for port in line.split('/')]

components = [{'index':i, 'ports':read(line)} for i, line in zip(itertools.count(), sys.stdin.read().splitlines())]

strength = lambda c: sum(c['ports'])

def bridges(components, pins):
    matching = [c for c in components if c['ports'][0] == pins or c['ports'][1] == pins]
    for m in matching:
        yield [m]
        rest = [r for r in components if r['index'] != m['index']]
        out = m['ports'][1] if m['ports'][0] == pins else m['ports'][0]
        for sub_bridge in bridges(rest, out):
            yield [m] + sub_bridge

bridge_strength = lambda bridge: sum(map(strength, bridge))
cmp = lambda bridge: (len(bridge), bridge_strength(bridge))

print(bridge_strength(sorted(bridges(components, 0), key=cmp, reverse=True)[0]))