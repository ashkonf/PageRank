# PageRank
A Python implementation of Google's famous PageRank algorithm.

#### Usage

The pagerank module exports one public function:

     powerIteration(edgeWeights, rsp=0.15, maxIterations=100)
     
This function applies the PageRank algorithm to a provided graph to determine the steady probabilities with which a random walk through the graph will end up at each node. It does so using power iteration, an algorithm approximating steady state probabilities by iteratively improving them until convergence. This algorithm is guaranteed to converege to the correct steady state probabilities for ergodic Markov chains, which PageRank graphs are.

##### Return value:

This function returns a pandas series whose keys are node names and whose values are the corresponding steady state probabilities. This series can be treated as a dict.
  
##### Arguments:

1.  edgeWeights: The graph to which the PageRank algorithm is applied represented as the weights between its nodes. It should be encoded sparsely as a once nested dictionary where keys and nested keys are node names and values are weights. Other datastructures with the same nested key-value interface, such as pandas matrices, are also acceptable. 
2.  rsp: The random surfer probability that represents the probability with which the random walk through the graph will deviate from its edges and instead jump randomly to any node in the graph. 
3.  maxIterations: The number of iterations after which the power iteration process will be terminated even if it has not yet converged.

Note that elements of "edgeWeights" need not be probabilities (meaning its rows need not be normalized), and the random surfer probabilities should not be incorporated into it. The "powerIteration" function will perform normalization and integration of the random surfer probabilities.

#### Dependencies

The pagerank module relies on two relatively standard Python libraries:

1.  [numpy](http://www.numpy.org/) 
2.  [pandas](http://pandas.pydata.org/)
