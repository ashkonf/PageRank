# PageRank
A Python implementation of Google's famous PageRank algorithm.

#### Usage

The pagerank module exports one public function:

        powerIteration(edgeWeights, rsp=0.15, maxIterations=100)
  
Arguments:

1.  edgeweights: The graph to which the PageRank algorithm is applied represented as the weights between its nodes. It should be encoded sparsely as a once nested dictionary where keys and nested keys are node names and values are weights. Other datastructures with the same nested key-value interface, such as pandas matrices, are also acceptable. 
2.  rsp: The random surfer probability that represents the probability with which the random walk through the graph will deviate from its edges and instead jump randomly to any node in the graph. 
3.  maxIterations: The number of iterations after which the power iteration process will be terminated even if it has not yet converged.


#### Dependencies: 
1.  [numpy](http://www.numpy.org/) 
2.  [pandas](http://pandas.pydata.org/)
