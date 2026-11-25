# Day 1 — Diagnostic Part A

Date: 24-11-2026

## Section 1: ML concepts (provisional score: ~30/100)

**Q1. Supervised vs unsupervised learning, with an example of each**

- My answer: Described human learning: a mentor guiding me (supervised) vs self-study with self-discipline (unsupervised). "Machine too learns this way."
- Confidence: 2/5
- Correct: Supervised = learn from data with correct answers (labels), e.g. spam vs not-spam emails. Unsupervised = no labels; find structure, e.g. customer segmentation.
- Score: ~20

**Q2. House prices: features vs label**

- My answer: "I don't know about ML yet."
- Correct: Features = inputs (size, bedrooms, location). Label = price (what we predict).
- Score: 0

**Q3. Estimate a new house's price from 1,000 past sales (common sense)**

- My answer: Find houses of the same size; compare by location (land rate, accessibility), bedrooms, and house dimensions; then give the price.
- Confidence: 3/5
- Feedback: Good intuition. This is similar to k-Nearest Neighbours, and "location → land rate" is feature engineering. Gap: I didn't say HOW to combine similar houses (e.g. average the prices of the 5 closest; what if no exact match?).
- Score: ~65

## Section 2: Math (provisional score: ~59/100)

**Q1. Solve 2(x − 3) + 4 = 3x − 8**

- My answer: 2x − 6 + 4 = 3x − 8 → 2x − 2 = 3x − 8 → 6 = x
- Confidence: 5/5 | Correct ✓ | Score: 100

**Q2. Line through (1, 3) and (4, 9): slope, equation, y at x = 10**

- My answer: "Forgot this (Class 10 syllabus). m = slope. I don't know."
- Correct: m = (9−3)/(4−1) = 2; c = 1; y = 2x + 1; at x = 10, y = 21
- Score: 0 — KEY GAP: y = mx + c is linear regression

**Q3. Mean and median of 4, 8, 6, 10, 7**

- My answer: Mean = 35/5 = 7. Median: sort → 4, 6, 7, 8, 10; pair off the ends; middle = 7 (for an even count, average the two middle numbers)
- Confidence: 5/5 | Correct ✓ | Score: 100

**Q4. Bag of 3 red, 5 blue: (a) P(red) (b) P(two reds, without replacement)**

- My answer: Total = 8 balls, then couldn't continue. "Didn't learn it deeply/practically."
- Correct: (a) 3/8 (b) 3/8 × 2/7 = 3/28
- Score: ~15

**Q5. Exponents and roots**

- My answer: 2³ × 2⁴ = 2⁷ = 128; 5⁰ = 1; √49 = 7
- Confidence: 5/5 | Correct ✓ | Score: 100

**Q6. ₹800, +25%, then −20%**

- My answer: 800 → 1000 → 1000 − 250 = ₹750; "not lower than 800". (Note: practised this type recently.)
- Confidence: 5/5
- Correct: 1000 × 20% = 200 → ₹800 (same price, because 1.25 × 0.80 = 1.00)
- Score: ~40 — arithmetic slip, and part (b) contradicted part (a)
- ⚠ Overconfidence: 5/5 but wrong. Habit to build: sanity-check before committing.

## Gaps to fix

1. ML vocabulary (supervised/unsupervised, features/labels)
2. Lines and slope (y = mx + c)
3. Basic probability
4. Checking my own answers before committing
