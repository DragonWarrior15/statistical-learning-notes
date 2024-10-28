---
title: First to call 50 wins
---

### Question: You and your opponent are to play a competitive game. You shall take turns to call out integers. The first person to call out "50" wins. 
### The rules are as follows:
### 1. The player who starts must call out an integer between one and 10, inclusive
### 2. A new number called out must exceed the most recent number called by at least one and by no more than 10. For example, if the first player calls out "nine," then the range of valid numbers for the opponent is 10 to 19, inclusive. Do you want to go first, and if so, what is your strategy?

### Solution
For you to be in a position to say `50`, your opponent must have said a number in the range `50-1` to `50-10` which is `40-49` (because that guarantees you will always be able to say `50` at your next turn).
This is only possible if you had said `39` in the turn prior.

Following the same scheme, we can form the below table (working on the turns backwards)

| Player | Number Spoken |
| --- | --- |
| You | `50` |
| Opponent | `40-49` |
| You | `39` |
| Opponent | `29-38` |
| You | `28` |
| Opponent | `18-27` |
| You | `17` |
| Opponent | `7-16` |
| You | `6` |

Thus, if you start with `6`, you are guaranteed to win.
If the opponent starts with any number other than`6`, you can form a similar winning strategy because of the following
* Opponent starts by saying anything betewen `1-5`, you can say `6` on your turn and we get the exact same table/game as above.
* Opponent starts by saying anything between `7-10`, you can say `17` on your turn and we get the exact same table/game as above.
