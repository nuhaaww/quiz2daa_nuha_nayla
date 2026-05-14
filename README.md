# Quiz2DAA_Nuha_Nayla

# Number Guessing Game — Binary Search
**EF234405 Design & Analysis of Algorithms | Quiz 2**

---
## Group Members

| No. | Student ID | Name |
|-----|------------|------|
| 1 | 5025241005 | Nuha Usama Okbah |
| 2 | 5025241014 | Almira Nayla Felisitha |

## Overview
This is a command line number guessing game built. The core mechanic of the game is powered by the **Binary Search** algorithm, one of the most fundamental search algorithms in computer science.

The game has three modes: you can guess the computer's number manually, let the computer guess your number using binary search, or watch a live step by step demo of the algorithm working on a random target. The goal is to make binary search tangible and interactive rather than just a concept on paper.

---

## Why Binary Search?

Binary Search is a classic divide and conquer algorithm that is perfectly suited for guessing games. In a regular (linear) guessing game, you might just guess 1, 2, 3, 4... in the worst case, that's 100 guesses for a range of 1–100. Binary Search cuts that down by always guessing the **midpoint** of the remaining range.

Each guess eliminates **half** of all remaining possibilities. This is why the computer can always find any number between 1 and 100 in **at most 7 guesses**, no matter what the number is.

It's worth noting that binary search only works on a sorted (ordered) search space. In this game, the search space is the integer range [1, 100], which is naturally sorted, so binary search applies perfectly.

---

## Algorithm: Binary Search

### How it works
1. Set `low = 1`, `high = 100`
2. Calculate `mid = (low + high) // 2`
3. Compare `mid` to the target:
   - If `mid == target` → found, stop
   - If `mid < target` → target is in the upper half, set `low = mid + 1`
   - If `mid > target` → target is in the lower half, set `high = mid - 1`
4. Repeat from step 2 until found

### Complexity Analysis

| Metric | Value |
|--------|-------|
| Time Complexity | O(log n) |
| Space Complexity | O(1) |
| Best Case | O(1) ; target is exactly the midpoint on the first guess |
| Worst Case | O(log n) ; target is at the edge of the range |
| Worst case for n=100 | ⌈log₂(100)⌉ = **7 guesses** |

For comparison, a naive linear search would take up to **100 guesses** in the worst case. Binary search reduces this to just 7, that's over 14x more efficient for this range.

### Pseudocode
```
function binary_search(low, high, target):
    while low <= high:
        mid = (low + high) / 2
        if mid == target:
            return mid
        else if mid < target:
            low = mid + 1
        else:
            high = mid - 1
    return NOT FOUND
```

---

## How to Run

### Requirements
- Python 3.x
- No external libraries or dependencies needed

### Run the game
```bash
python game.py
```

You'll see a menu and can pick any of the three modes.

---

## Game Modes

### Mode 1 — You guess the computer's number
The computer picks a random number between 1 and 100. You try to guess it by typing numbers. After each guess, the game tells you if you're too high or too low. When you find the number, it shows how many guesses you took and compares it to how many steps binary search would have needed.

This mode lets you experience what it feels like to search manually, and puts binary search's efficiency into perspective.

### Mode 2 — Computer guesses YOUR number (Binary Search)
You think of a number between 1 and 100. The computer uses binary search to find it. After each guess, you respond with:
- `H` — the guess is too high
- `L` — the guess is too low
- `Y` — correct!

The computer will always find your number in at most 7 guesses. You can try to beat it by memorizing its pattern, but it's mathematically guaranteed to find the number in logarithmic time regardless.

### Mode 3 — Binary Search Demo
The computer picks a random number and immediately runs binary search on it, printing every single step: the current range, the midpoint guess, and whether it went left or right. This is the most educational mode, you can see exactly how the algorithm narrows down the range with each step.

---

## Example Output

### Mode 2 — Computer guesses your number
```
Think of a number between 1 and 100. Keep it secret!
Press Enter when you have one in mind...

Okay! I'll use Binary Search to find your number.
It should take me at most 7 guesses.

[Attempt 1] Remaining range: 1 to 100
  -> My guess: 50
  Your answer: L

[Attempt 2] Remaining range: 51 to 100
  -> My guess: 75
  Your answer: H

[Attempt 3] Remaining range: 51 to 74
  -> My guess: 62
  Your answer: L

[Attempt 4] Remaining range: 63 to 74
  -> My guess: 68
  Your answer: Y

Got it! Your number was 68.
Binary Search found it in 4 guess(es). Max possible for 1-100 is 7.
```

### Mode 3 — Binary Search Demo
```
--- Binary Search Demo ---
Target number (hidden during real game): 73
Search range starts at: [1, 100]

  Step 1: range=[1, 100], mid=50  -> 50 < 73, discard left half. New low = 51
  Step 2: range=[51, 100], mid=75 -> 75 > 73, discard right half. New high = 74
  Step 3: range=[51, 74], mid=62  -> 62 < 73, discard left half. New low = 63
  Step 4: range=[63, 74], mid=68  -> 68 < 73, discard left half. New low = 69
  Step 5: range=[69, 74], mid=71  -> 71 < 73, discard left half. New low = 72
  Step 6: range=[72, 74], mid=73  -> FOUND! 73 == 73

Finished in 6 step(s).
Worst case for n=100 is ceil(log2(100)) = 7 steps.
Algorithm: O(log n) time, O(1) space.
```

---

## Limitations & Possible Extensions
- Currently only supports the range 1–100. This could be made configurable (e.g. 1–1000), which would change the worst case to ⌈log₂(1000)⌉ = 10 guesses.
- The game is text-based; a GUI version using `tkinter` or a web version could make it more visually engaging.
- A leaderboard or score tracking system could be added to record how many guesses each player takes across sessions.
- Mode 2 relies on honest input from the player. A cheat-detection system could flag inconsistent answers (e.g. if the player's responses are logically contradictory).

---
