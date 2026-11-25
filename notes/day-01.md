
# Day 1 — Week 1 Diagnostic, Part A

- **Date:** 24-11-2026 (Tuesday; the schedule lists Day 1 as Monday 23-11-2026)
- **Phase:** Foundation · Month 1 (Python, tooling & math refresh)
- **Planned time:** 180 min
- **Learning objective:** Measure my real starting level in ML concepts, math, Python and SQL.

## Plan

| # | Dimension   | Min | Task                                             | Status |
| - | ----------- | --- | ------------------------------------------------ | ------ |
| 1 | Theory      | 30  | Diagnostic A: ML concepts                        | ✓     |
| 2 | Math        | 42  | Diagnostic A: math                               | ✓     |
| 3 | Project     | 27  | Python, VS Code, Git, GitHub, repo `ai-ml-365` | ✓     |
| 4 | Coding      | 36  | Python problems 1–5                             | ✓     |
| 5 | Assessment  | 18  | SQL (first look — no prior knowledge)           | ✓     |
| 6 | Revision    | 15  | Flashcards from today's mistakes                 | ☐     |
| 7 | Soft skills | 12  | Learning log + 5 lines on why                    | ☐     |

---

## Section 1: ML concepts (provisional score: ~30/100)

**Q1. Supervised vs unsupervised learning**

- My answer: Described human learning: a mentor guiding me (supervised) vs self-study with self-discipline (unsupervised).
- Confidence: 2/5 · Score: ~20
- Correct: **Supervised** = learn from data with correct answers (labels), e.g. spam vs not-spam emails. **Unsupervised** = no labels; find structure, e.g. customer segmentation.

**Q2. House prices: features vs label**

- My answer: "I don't know about ML yet." · Score: 0
- Correct: **Features** = inputs (size, bedrooms, location). **Label** = price (what we predict).

**Q3. Estimate a new house's price from 1,000 past sales**

- My answer: Find houses of the same size; compare by location (land rate, access), bedrooms and dimensions; then give the price.
- Confidence: 3/5 · Score: ~65
- Feedback: Good intuition. This is similar to **k-Nearest Neighbours**; "location → land rate" is **feature engineering**. Gap: I didn't say HOW to combine similar houses (e.g. average the prices of the 5 closest; what if there's no exact match?).

---

## Section 2: Math (provisional score: ~59/100)

**Q1. Solve 2(x − 3) + 4 = 3x − 8** ✓

- 2x − 6 + 4 = 3x − 8 → 2x − 2 = 3x − 8 → **x = 6** · Confidence 5/5 · Score 100

**Q2. Line through (1, 3) and (4, 9)** ✗ (forgot, Class 10 syllabus)

- m = (9 − 3)/(4 − 1) = **2**; 3 = 2(1) + c → **c = 1**; **y = 2x + 1**; at x = 10, **y = 21**
- Score 0. KEY GAP: y = mx + c is linear regression.

**Q3. Mean and median of 4, 8, 6, 10, 7** ✓

- Mean = 35/5 = **7**. Median: sort → 4, 6, 7, 8, 10 → **7** (even count → average the two middle numbers)
- Confidence 5/5 · Score 100

**Q4. Bag of 3 red, 5 blue** ✗ (counted 8 total, then stuck)

- (a) P(red) = **3/8**
- (b) Without replacement: 3/8 × 2/7 = 6/56 = **3/28**
- Score ~15

**Q5. Exponents and roots** ✓

- 2³ × 2⁴ = 2⁷ = **128**; 5⁰ = **1**; √49 = **7** · Confidence 5/5 · Score 100

**Q6. ₹800, +25%, then −20%** ✗ (practised this type recently)

- My answer: ₹750, "not lower than 800" · Confidence 5/5
- Correct: 800 → 1000 → 1000 − **200** = **₹800**. Same price, because 1.25 × 0.80 = 1.00. Percentage changes multiply; they don't add.
- Score ~40. ⚠ **Overconfidence:** 5/5 but wrong. Habit: sanity-check before committing.

---

## Section 3: Project setup ✓

- Installed Python, VS Code, Git; created GitHub account `sitharthai-ai`; repo `ai-ml-365`.
- **Separate personal Git identity on a shared Mac** (office identity stays global):

```bash
# Personal identity file
git config --file ~/.gitconfig-personal user.name "Sitharth AI"
git config --file ~/.gitconfig-personal user.email "sitharth.ai@gmail.com"

# Use it for every repo inside ~/Desktop/Personal/
git config --global "includeIf.gitdir/i:~/Desktop/Personal/.path" "~/.gitconfig-personal"

# Verify (shows the value AND which file it came from)
git config --show-origin user.email
```

- **Personal SSH key + host alias** (in `~/.ssh/config`):

```
Host github-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_personal
  IdentitiesOnly yes
  AddKeysToAgent yes
  UseKeychain yes
```

- Clone with: `git clone git@github-personal:sitharthai-ai/ai-ml-365.git`
- Lessons learned:
  - Run commands **one per line**; two on one line → `error: no action specified`.
  - `includeIf` only matches if the repo is really inside that folder; check with `pwd`.
  - "Repository not found" → the repo didn't exist on GitHub yet.
  - Check a host fingerprint against GitHub's published keys before typing `yes`.
  - SSH here goes through the office proxy (`127.0.0.1:3128`); don't bypass it. Check company policy on personal use.

---

## Section 4: Python (provisional score: ~61/100)

**P1. count_vowels** ✓ (after testing) · Score 90

```python
def count_vowels(text):
    vowels_count = 0
    for i in text:
        if i in ("a","A","e","E","i","I","o","O","u","U"):
            vowels_count += 1
    return vowels_count
```

- First version had the counter **outside** the function → `UnboundLocalError`. Testing caught it.
- Cleaner: `return sum(1 for ch in text.lower() if ch in "aeiou")`

**P2. second_largest** ✓ · O(n) time, O(n) space · Score 85

```python
def second_largest(nums):
    unique_nums = list(set(nums))
    if len(unique_nums) <= 1:
        return None
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)
```

- Single pass, O(1) extra space:

```python
def second_largest(nums):
    first = second = None
    for x in nums:
        if first is None or x > first:
            first, second = x, first
        elif x != first and (second is None or x > second):
            second = x
    return second
```

**P3. word_freq** ✗ ("Don't know") · Score 0. GAP: dictionaries and string cleaning.

```python
def word_freq(sentence):
    for p in ".,!?":
        sentence = sentence.replace(p, "")
    counts = {}
    for word in sentence.lower().split():   # split() handles extra spaces
        counts[word] = counts.get(word, 0) + 1
    return counts
```

**P4. fizzbuzz** ✓ · Score 95

```python
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
```

- `if n == 0: return []` wasn't needed: `range(1, 1)` is already empty.

**P5. two_sum** ✗ (structure right, two logic bugs) · Score ~35

- Bug 1: returned `[i, i+1]` instead of `[i, j]`.
- Bug 2: `elif j == len(nums) - 2: return None` exits too early → `[3, 2, 4]` returned None.
- Passed 4/5 tests, but 2 passes were luck. **Passing tests ≠ correct logic.**

```python
# Brute force, O(n²)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

# One pass with a dict, O(n) — standard interview answer
def two_sum(nums, target):
    seen = {}                      # value → index
    for j, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], j]
        seen[x] = j
    return None
```

**Coding patterns to fix**

- Printing inside functions → **return** instead, and test with `assert`.
- Semicolons at line ends (a JavaScript habit) → not needed in Python.
- Unused variables (e.g. `return_array` in P5).

---

## Section 5: SQL — first look (not scored; starting from zero)

- SQL is formally taught from **Day 34** (DS-SQL-001).
- A table is like an Excel sheet: columns = kinds of information, rows = records.
- `SELECT` = which columns · `FROM` = which table · `WHERE` = which rows.

```sql
SELECT name, city
FROM students
WHERE marks > 80;
```

- Output: Arun (Chennai), Priya (Madurai), Rahul (Chennai) ✓

---

## Gaps to fix

1. ML vocabulary (supervised/unsupervised, features/labels)
2. Lines and slope (y = mx + c)
3. Basic probability (counting, without replacement)
4. Checking my own answers before committing (overconfidence on Q6)
5. Python dictionaries and string processing
6. Loop exit logic (where `return None` goes)
7. SQL (scheduled from Day 34)

## Flashcards (revision, to write in my own words)

1. Supervised vs unsupervised learning, with examples
2. Slope through two points, and finding c in y = mx + c
3. P(red) from 3 red/5 blue; P(two reds) without replacement
4. Why +25% then −20% returns to the original price
5. Counting words with a dict (`counts.get(word, 0) + 1`)
6. Two Sum: where `return None` goes; why `[i, i+1]` was wrong
7. Why functions should `return`, not `print`
8. SQL: what `SELECT`, `FROM`, `WHERE` each do

## Day 1 Flashcards

**Q1:** What is supervised vs unsupervised learning? Give an example of each.
**A:** Supervised = learns from data that includes the correct answers (labels), e.g. predicting spam vs not-spam. Unsupervised = no labels; finds structure on its own, e.g. grouping customers by buying behaviour.

**Q2:** In "predict the house price", what are the features and the label?
**A:** Features = inputs (size, bedrooms, location). Label = what we predict (price).

**Q3:** How do you find the slope and the equation of a line through (x₁, y₁) and (x₂, y₂)?
**A:** m = (y₂ − y₁)/(x₂ − x₁). Substitute one point into y = mx + c to find c. Example: (1, 3) and (4, 9) → m = 2, c = 1 → y = 2x + 1.

**Q4:** A bag has 3 red and 5 blue balls. What is P(red)? What is P(two reds) without replacement?
**A:** P(red) = 3/8. Two reds = 3/8 × 2/7 = 6/56 = 3/28. The second fraction changes because one red ball has been removed.

**Q5:** Why does +25% followed by −20% return to the original price?
**A:** Percentage changes multiply: ×1.25 then ×0.80 = ×1.00. They don't add (25 − 20 ≠ 5%).

**Q6:** How do you count words with a dictionary in Python?
**A:** counts = {} ; for word in text.lower().split(): counts[word] = counts.get(word, 0) + 1. Here .get(word, 0) returns 0 when the word is new.

**Q7:** In Two Sum, where does `return None` go, and why was `[i, i+1]` wrong?
**A:** `return None` goes AFTER both loops finish, once every pair has been checked. `[i, i+1]` assumes the two numbers are next to each other; the answer is `[i, j]`.

**Q8:** Why should a function `return` its result instead of `print` it?
**A:** Returned values can be reused, tested with assert and combined with other code. Printing only shows the value on screen; the function then returns None.

**Q9:** What does each part of a SQL query do?
**A:** SELECT = which columns · FROM = which table · WHERE = which rows to keep. Example: SELECT name FROM students WHERE marks > 80;

**Q10:** What habit fixes overconfidence errors like the ₹750 mistake?
**A:** Sanity-check before committing: redo each calculation, and make sure later answers agree with earlier ones.

## Learning log

- **Learned:**
- **Struggled:**
- **Next:**

## Why I'm doing this year (5 lines)
