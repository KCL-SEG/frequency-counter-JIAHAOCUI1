"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(0, len(items)):
        items[i] = str(items[i])

        for i in items:
            frequencies[i] = items.count(i)
    return frequencies


