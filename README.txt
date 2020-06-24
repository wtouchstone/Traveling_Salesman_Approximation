William Touchstone, wtouchstone3@gatech.edu  Submission date: Thu, Apr. 16 2020

Files submitted:
test.py: ignore, ensuring distance formula is accurate
tsp.py: A couple of failed attempts at previous solutions. Contains Nearest neighbor solution (final cost ~32200) and
        attempt at Christofides solution that was abandaoned as we cannot assume triangle inequality
tsp-3510.py: Final solution utilizing ant colony optimization. Works as specified in PDF.
To run the actual algorithm, do tsp-3510.py with command line args as specified in assignment PDF

Bugs and limitations: I'm not sure how well this algorithm will generalize time wise to larger sets.
It runs basically deterministically despite the fact that there is a degree of randomness involved
more info in PDF.