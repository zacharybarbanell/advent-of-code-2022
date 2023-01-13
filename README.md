# Advent of Code 2022

This repo contains my solutions to the 2022 Advent of Code programming puzzles (https://adventofcode.com/2022), in which I placed 77th overall.  The actual code is included in exactly the state it was in when I correctly submitted (except for an expunged session key), but since the objective is to try to solve the puzzles as quickly as possible, the code is difficult to read, and in many cases is incomplete as code for part 1 was deleted for part 2, among other reasons, so below is a text description of my solution to each problem, as well as notes on potential improvements, issues encountered, and such.  The two numbers next to each problem are my placement on part 1 and part 2, respectively.

# Puzzles

## [Day 1: Calorie Counting](https://adventofcode.com/2022/day/1) - 109/553

Nothing particularly clever going on here.  The input processing code is boilerplate I copied from the previous year, designed to read input pasted into the console with a manual terminator, since I didn't want to deal with putting it in a file.  Initially, I intended to only store the highest three totals seen so far, but sorting the whole list is only a log factor slower and was shorter to write.

## [Day 2: Rock Paper Scissors](https://adventofcode.com/2022/day/2) - 18/57

This is the first day I got on the leaderboard.  The code uses modular arithmetic, taking advantage of the fact that the result of a game is a win/draw/loss if the indices of the two moves played differ by 1/0/-1, respectively.  There's nothing else particularly interesting going on here, but the modulus-based approach was much faster to write than the decision tree with 9 cases, so I was able to get a pretty decent spot on the leaderboard.

## [Day 3: Rucksack Reorganization](https://adventofcode.com/2022/day/3) - 35/222

Another fairly straightforward early day.  I went with the O(n^3) iteration based approach over the O(n) hash set intersections because the input was short enough that it didn't matter (and, I suspect, with the overheads present in python the set approach may actually be slower on an input this small).

## [Day 4: Camp Cleanup](https://adventofcode.com/2022/day/4) - 910/1757

There's not a lot to say about a lot of these early puzzles - this one's pretty straightforward, simply parsing the input takes about as much effort as actually doing the math.

## [Day 5: Supply Stacks](https://adventofcode.com/2022/day/5) - 245/171

The main challenge of this one was parsing, which in my case (as with most other solutions I've seen) was simply done by hardcoding a few constants.  The actual implementation is a little awkward, since it's using lists, so there's some excessive copying going on - ideally, I'd want to use an actual stack implementation.  Also, this is the day I started using the `aocd` package to automatically download puzzle inputs.

## [Day 6: Tuning Trouble](https://adventofcode.com/2022/day/6) - 382/338

One of the easiest days, even easier than the previous few puzzles, judging by solve times.  Again, this implementation is a factor slower than the optimal one, which would be to maintain a count for each type of letter, updating it as a single character is added or removed at each step.  Also, the input on this is hardcoded for some reason, I'm not really sure why.  The `colorama` package added here is to fix an ANSI issue that `aocd` causes in certain terminals.

## [Day 7: No Space Left On Device](https://adventofcode.com/2022/day/7) - 213/132

Another problem that doesn't admit a lot of variability in solving, since it straightforwardly asks you to simulate the system it describes.  This could be made asymptotically faster by using an actual tree structure instead of string comparison, but it's nearly instantaneous either way.

## [Day 8: Treetop Tree House](https://adventofcode.com/2022/day/8) - 287/2458

Nothing clever going on here, just a fairly direct implementation of the system described in the problem.  My worst rank of the event, due to several misreadings of the part 2 specification.

## [Day 9: Rope Bridge](https://adventofcode.com/2022/day/9) - 214/63

Another fairly direct implementation of the specification.  I managed to get on the leaderboard, which I think is due to carefully implementing the movement logic as specified in the problem statement during part 1.

## [Day 10: Cathode-Ray Tube](https://adventofcode.com/2022/day/10) - 1918/1618

This day was tough because of a lot of off by one errors - there's three different counters, some of which are zero-indexed and some of which are one-indexed.  Also, I accidentally deleted the code for this day when setting up the next day's file, but there's nothing that interesting in it.

## [Day 11: Monkey in the Middle](https://adventofcode.com/2022/day/11) - 630/356

This is the first day that required doing something beyond simply simulating the system as described in the problem, since the squaring operation means that the numbers would quickly become too large to store in memory at all.  The solution to this is to store only the remainder of the numbers modulo the lcm of the monkeys' divisibility checks, since that fully determines their behavior.  (The variable named `gcd` in my code stores the lcm, or rather a common multiple that could be excessively large).

## [Day 12: Hill Climbing Algorithm](https://adventofcode.com/2022/day/12) - 407/249

This day is the first shortest-path problem of many.  The code here is a fairly straightforward queue-based BFS.

## [Day 13: Distress Signal](https://adventofcode.com/2022/day/13) - 145/149

Another fairly straightforward one, this asks you to implement a simple recursive comparator.  The code for this is much bulkier than it needs to be, since I wrote the comparator for part 1 where it is allowed to destroy its input - then in part 2 had to change it, since you're comparing some elements more than once.

## [Day 14: Regolith Reservoir](https://adventofcode.com/2022/day/14) - 32/35

This is the first day where a direct implementation, which was what I did, was noticeably slow (but only on the second part).  A faster part 2 implementation would have been to use a DFS, reducing the runtime from O(n^3) to O(n^2), or to do something smarter that involved eliminating the vast regions that aren't near enough to any walls to be worth thinking too hard about.

## [Day 15: Beacon Exclusion Zone](https://adventofcode.com/2022/day/15) - 538/115

Here, the key insight is that the space must be on the boundary of a beacon's range.  I missed this insight, but I think my solution still has the same asymptotic behavior up to a log factor despite not explicitly using that.

## [Day 16: Proboscidea Volcanium](https://adventofcode.com/2022/day/16) - 95/57

The first difficult problem of the set, judging by leaderboard solve times. The solution for part 1 is fine - a fairly simple DP approach, the only nontrivial step is collapsing the graph to take advantage of the fact that the nonzero nodes are sparse.  The second part is pretty slow - it iterates over every possible partition of the nonzero nodes into subsets, which is excessive - since many partitions are unachievable, we only need to check each achievable set and its complement.  The memoization could also have been improved, by combining the set of nodes which have already been visited with the set of nodes which are disallowed due to the other agent's claim.

## [Day 17: Pyroclastic Flow](https://adventofcode.com/2022/day/17) - 72/233

The first part of this problem is a simple simulation.  The second part requires detecting a cycle, which I did in a straightforward but not infallible way - checking if the top 100 rows match their arrangement at some prior point in time where all the other cyclic parts of the simulation align.  This isn't entirely rigorous - it's possible, if implausible, that some difference 100 rows down could lead to a false positive, but in practice, it doesn't seem to.  There are a couple of approaches to make this more rigorous - tempting is to do a floodfill of empty space from the top of the map, as anything that's not exposed can't affect anything, but that might not detect a cycle if, for instance, there's one column that always stays open, since there would be more reachable spaces every time.  A better way would be to keep track of how far the deepest piece dropped ever goes - if the whole structure, down at least that far, is repeating, then it is actually guaranteed to repeat, though this is potentially very expensive to compute, and could still miss certain very complex cycles where states don't repeat exactly, but things change modulo the length of the input - I'm not certain that in the general version of this problem, there actually exists an algorithm that can efficiently solve this for fully adversarial inputs.

## [Day 18: Boiling Boulders](https://adventofcode.com/2022/day/18) - 75/59

This is a fairly simple solution, running a BFS on the air in the bounding cuboid, with the additional cute trick of counting exposed faces while searching the outside, instead of saving which spaces are outside and doing another pass.  This solution was written after looking at the input data to see that the coordinates of every point are small, but it's not particularly efficient in general - ignoring discontinuities in the range of coordinates, which are easy to account for, it's still O(n^3) in the worst case.  A more efficient solution would be to find each connected component, count its external surfaces by searching only points near the component, and then eliminate all connected components contained fully within another - which runs in O(n log n), with the log factor being a consequence of needing to sort something at some point to do the containment checks.

## [Day 19: Not Enough Minerals](https://adventofcode.com/2022/day/19) - 2/38

My best score, and in fact it could have been better - I could have gotten third place on part 2 if not for an unfortunate typo, since there were no important changes in my code from part 1 to part 2, although I did spend a lot of time writing the large decorator in the middle of the file, which isn't called anywhere and wouldn't have worked anyways.  Most peoples' approaches to this problem were BFS-based, but I went with the recursive DFS, which was simpler to write (and, more importantly, I thought of it first).  Most DFS-based solutions had trouble due to the very large statespace, but I had a few optimizations that let mine run fairly fast.  The first was simply limiting constructions of machines that would push production past what could possibly be used, but the other was that instead of tracking geodes and geode robots, I simply added all the geodes a robot would ultimately produce when I constructed it.  This saved me a lot of runtime due to memoization - without that, there would be orders of magnitude more distinct calls, resulting in a slowdown of hundreds of times.  There's several possible optimizations I didn't come up with - you should never build something if you could have built it on the previous turn but built nothing, for instance, and you can also easily loosely bound the maximum possible geodes from a state - which can let you discard certain branches early.  I also suspect that BFS is fundamentally faster, since with a BFS you can throw out any state which is strictly worse than a different state reachable at the same level.

## [Day 20: Grove Positioning System](https://adventofcode.com/2022/day/20) - 84/127

Not much to say about this one, it feels like an early day since you're basically just implementing the system described in the problem.  I used a doubly linked list instead of an array, which has exactly the same asymptotic behavior, as it turns out. The fast way to solve this problem is with a binary search tree - specifically an order statistic tree - since that lets you move elements arbitrarily far in logarithmic time instead of linear.

## [Day 21: Monkey Math](https://adventofcode.com/2022/day/21) - 218/42

This is not my proudest solution.  For part 1, I simply blindly execute lines of input in an arbitrary order, catching name errors, until I've executed everything, and read the value saved to root.  For the second part, I actually took the list of statements and moved them into Mathematica, which can handle them symbolically, and had it solve the equation for me.

## [Day 22: Monkey Map](https://adventofcode.com/2022/day/22) - 52/832

Nothing too interesting here - my part 1 was very straightforward, and for part 2, in addition to having trouble doing the casework by eye, I took some shortcuts that took a while to debug later.  Not a very interesting problem, in any case.

## [Day 23: Unstable Diffusion](https://adventofcode.com/2022/day/23) - 422/380

Another fairly straightforward day where running the simulation as described in the problem is all you need to do.  I got tripped up on this one due to missing an important sentence while reading the problem statement, so was fairly slow.

## [Day 24: Blizzard Basin](https://adventofcode.com/2022/day/24) - 102/78

One more straightforward BFS problem.  The one interesting thing that my code for this does is that it calculates where all of the blizzards will be at every turn while parsing input, since the whole board repeats itself based on the lcm of its dimensions.  This turned out to be excessive, since the actual shortest paths are shorter than the precomputed table, so it doesn't actually speed things up.  The better thing to do would have been to either have separate precomputed tables for height and width, with different moduluses, or to not store future blizzard positions at all, but instead, to check if a cell is occupied on a turn, go backwards and check the four spaces a blizzard could have been at turn 0 to be there on that turn.  Ultimately, even my relatively slow solution was still easily fast enough.

## [Day 25: Full of Hot Air](https://adventofcode.com/2022/day/25) - 420/363

This code is a fairly simple implementation of conversion from/to balanced quinary - the conversion into the base checks against the maximum value that could be reached if a less extreme choice were made, though I imagine there's a more efficient way to convert into a balanced base in general.
