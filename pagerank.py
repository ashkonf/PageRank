import os
import sys
import copy

import numpy
import pandas

def __extractNodes(matrix):
    nodes = set()
    for key1 in matrix:
        nodes.add(key1)
        for key2 in matrix[key1]:
            nodes.add(key2)
    return nodes

def __makeSquare(matrix, keys, default=0.0):
    matrix = copy.deepcopy(matrix)
    for key1 in keys:
        for key2 in keys:
            if not key1 in matrix:
                matrix[key1] = {}
            if not key2 in matrix[key1]:
                matrix[key1][key2] = 0.0
    return matrix

def __startState(nodes):
    if len(nodes) == 0: raise ValueError("There must be at least one node.")
    startProb = 1.0 / float(len(nodes))
    return pandas.Series({node : startProb for node in nodes})

def __calculateAlpha(numNodes, rsp):
    return 1.0 / float(numNodes) * rsp

def __integrateRandomSurfer(nodes, transitionProbs, rsp):
    alpha = __calculateAlpha(len(nodes), rsp)
    new = transitionProbs.copy()
    return new.multiply(1.0 - float(len(nodes)) * alpha) + alpha

def __exponentiateMatrix(matrix, exponent):
    for _ in range(exponent - 1):
        matrix = matrix.dot(matrix)
    return matrix

def __normalizeRows(matrix):
    return matrix.div(matrix.sum(axis=1), axis=0)

def powerIteration(edgeWeights, rsp=0.15, maxIterations=100):
    # Clerical work:
    nodes = __extractNodes(edgeWeights)
    edgeWeights = __makeSquare(edgeWeights, nodes)
    edgeWeights = pandas.DataFrame(edgeWeights).T.fillna(0.0)

    # Setup:
    state = __startState(nodes)
    transitionProbs = __normalizeRows(edgeWeights)
    transitionProbs = __integrateRandomSurfer(nodes, transitionProbs, rsp)
    
    # Power iteration:
    for iteration in range(maxIterations):
        oldState = state.copy()
        state = state.dot(transitionProbs)
        if (state == oldState).all(): break

    return state
