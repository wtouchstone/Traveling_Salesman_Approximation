# Traveling_Salesman_Approximation


## Summary of files:

* test.py: ignore, ensuring distance formula is accurate
* tsp.py: A couple of failed attempts at previous solutions. Contains Nearest neighbor solution (final cost ~32200) and attempt at Christofides solution that was abandaoned as we cannot assume triangle inequality
* tsp-3510.py: Final solution utilizing ant colony optimization. Works as specified in PDF.
* mat-test.txt: Example of input format, small sample. This algorithm assumes that the graphs between the locations specified here are fully connected.
* mat_output.txt: Output of the algorithm running on mat-test.txt


To run the actual algorithm, do tsp-3510.py with command line args as following:
* First arg: name of input file (In the format of mat-test.txt)
* Second arg: name of ouput file 
* Third arg: Time in seconds to allow the algorithm to run for

Bugs and limitations: I'm not sure how well this algorithm will generalize time wise to larger sets.
It runs basically deterministically despite the fact that there is a degree of randomness involved.
more info in PDF.
