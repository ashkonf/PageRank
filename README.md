# PageRank
A Python implementation of Google's famous PageRank algorithm.

### Usage

The pagerank module exports one public function:

     powerIteration(transitionWeights, rsp=0.15, epsilon=0.00001, maxIterations=1000)
     
This function applies the PageRank algorithm to a provided graph to determine the steady probabilities with which a random walk through the graph will end up at each node. It does so using power iteration, an algorithm approximating steady state probabilities by iteratively improving them until convergence. This algorithm is guaranteed to converege to the correct steady state probabilities for ergodic Markov chains, which PageRank graphs are.
  
##### Arguments:

1.  **transitionWeights**: The graph to which the PageRank algorithm is applied represented as the weights between its nodes. It should be encoded sparsely as a once nested dictionary or a once nested list. If encoded sparsely as a once nested dictionary, keys and nested keys should correspond to node names and values to weights. Other datastructures with the same nested key-value interface, such as certain Pandas matrices, are also acceptable. If encoded as a once nested list, node names are assigned as the indices corresponding to locations in the nested list. Again, other datastructures with the same nested indexed interface, such as Numpy matrices and certain Pandas matrices, are also acceptable.
2.  **rsp**: The random surfer probability that represents the probability with which the random walk through the graph will deviate from its edges and instead jump randomly to any node in the graph. 
3.  **epsilon**: The threshold of convergence. If the Euclidean norm of the difference between the approximations of the steady state vector before and after an iteration of power iteration is smaller than epsilon, the algorithm will consider itself to have converged and will terminate.
4.  **maxIterations**: The number of iterations after which power iteration will be terminated even if it has not yet converged.

Note that elements of "transitionWeights" need not be probabilities (meaning its rows need not be normalized), and the random surfer probabilities should not be incorporated into it. The "powerIteration" function will perform normalization and integration of the random surfer probabilities.

##### Return value:

This function returns a Pandas series whose keys are node names and whose values are the corresponding steady state probabilities. This Pandas series can be treated as a dict.

### TextRank Example

An implementation of TextRank and three stories one can apply it to are included as a sample usage of the PageRank module. TextRank is an unsupervised keyword significance scoring algorithm that applies PageRank to a graph built from words found in a document to determine the significance of each word. The textrank module, located in the TextRank directory, implements the TextRank algorithm.

The textrank module's main method applies TextRank to three fairy tales, Rapunzel, Cinderalla and Beauty and the Beast. It then prints out the results, an ordered list of keywords and their associated significance scores. To run this example, simply navigate to the TextRank directory and run textrank.py:

     cd TextRank/
     python textrank.py
     
For more information about TextRank, see the [original paper](https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf) that proposed it.

### Dependencies

This module relies on two relatively standard Python libraries:

1.  [Numpy](http://www.numpy.org/) 
2.  [Pandas](http://pandas.pydata.org/)
