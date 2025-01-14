# Probability

## Probability Formulas

1. **Union Probability**:
   $$
   P(A∪B) = P(A) + P(B) − P(AB)
   $$

2. **Conditional Probability**:
   $$
   P(A|B) = \frac{P(AB)}{P(B)}
   $$

3. **Joint Probability for Multiple Events**:
   $$
   P(ABC) = P(C|AB) \times P(B|A) \times P(A)
   $$

4. **Independent Events**:
   When $ A $ and $ B $ are independent:
   $$
   P(AB) = P(A) \times P(B)
   $$

---

# Permutations and Combinations

- **Ordered**: Use $ A $ (Permutations)
- **Unordered**: Use $ C $ (Combinations)

### Formulas:
1. **Permutations**:
   $$
   nA_r = n \times (n-1) \times (n-2) \dots (n-r+1)
   $$
   Example:
   $$
   5A3 = 5 \times 4 \times 3 = 60
   $$

2. **Combinations**:
   $$
   nC_r = \frac{n \times (n-1) \times (n-2) \dots (n-r+1)}{r \times (r-1) \times \dots \times 1}
   $$
   Example:
   $$
   5C3 = \frac{5 \times 4 \times 3}{3 \times 2 \times 1} = 10
   $$

### Special Cases:
1. **0 Factorial**:
   $$
   5A0 = 5C0 = 1
   $$

---

# Example Problem: Arranging Dance and Singing Performances

**Question**: There are 4 dance performances and 2 singing performances. The two singing performances cannot be adjacent. How many arrangements are possible?

### Steps:
1. Calculate total arrangements for the dance performances:
   - \( 4! = 4 \times 3 \times 2 \times 1 = 24 $

2. Place the 4 dance performances in order, leaving 5 available slots:  
   \[ _ D _ D _ D _ D _ \]

3. Choose 2 slots from the 5 available slots for the singing performances:
   - $ 5C2 = \frac{5 \times 4}{2 \times 1} = 10 $

4. Arrange the 2 singing performances in the chosen slots:
   - $ 2! = 2 \times 1 = 2 $

5. Total arrangements:
   $$
   24 \times 10 \times 2 = 480
   $$

**Answer**: There are **480 arrangements** where the two singing performances are not adjacent.