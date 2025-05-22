## 📘 Introduction to Algorithm Efficiency

**Why Efficiency Matters:**

* When solving problems with code, you may have multiple algorithms that work—but not all are equal.
* Some use more time (slower), others use more memory (less space-efficient).
* Efficiency becomes *critical* when dealing with large datasets or real-time applications.

---

## ⏱ 1. Measuring the Run Time of an Algorithm

**Definition:**

* This is about determining *how long* an algorithm takes to run based on the *size of the input*.

**Best Way to Express It:**

* Use **Big-O Notation** to describe how time grows:

  * Constant time → `O(1)` (e.g., accessing an array element)
  * Linear time → `O(n)` (e.g., simple loop over n items)
  * Quadratic time → `O(n²)` (e.g., nested loops)
  * Logarithmic time → `O(log n)` (e.g., binary search)

**Example:**

```python
def find_max(lst):
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val
```

* This runs in `O(n)` time—each item is checked once.

---

## 🧮 2. Counting Instructions

**What it Means:**

* You count the number of **basic operations** (like additions, comparisons, assignments) the algorithm performs.

**Why it Helps:**

* Gives a more *granular view* of how work increases with input size.

**Example:**

```python
def sum_list(lst):
    total = 0           # 1 operation
    for item in lst:    # n operations
        total += item   # n operations
    return total        # 1 operation
```

* Total operations = `2n + 2`, which simplifies to `O(n)`

**Important Concept:**

* When counting instructions, we care more about the *growth trend* rather than exact numbers.

---

## 🧠 3. Measuring the Memory Used by an Algorithm

**Definition:**

* Memory usage includes:

  * **Input data**
  * **Temporary variables**
  * **Call stack space** (for recursion)

**Memory Efficiency Example:**

```python
def add_one(lst):
    return [x + 1 for x in lst]
```

* This creates a **new list** → requires additional memory `O(n)`.

```python
def add_one_in_place(lst):
    for i in range(len(lst)):
        lst[i] += 1
    return lst
```

* Modifies the list *in place* → more memory efficient (`O(1)` additional memory)

---

## 🔁 Summary Table:

| Concept               | Measured By           | Common Big-O                      |
| --------------------- | --------------------- | --------------------------------- |
| Run Time              | Time as input grows   | O(1), O(n), O(n²), O(log n), etc. |
| Counting Instructions | Basic operation count | Converts to Big-O                 |
| Memory Usage          | Extra space used      | O(1), O(n), O(n log n), etc.      |

---

## ✅ Tips to Master This Section:

1. Focus on **how the algorithm behaves** when input size increases.
2. Practice comparing algorithms using **Big-O notation**.
3. Use real Python examples and try timing with `time` or `timeit` modules.
4. Trace memory use with tools like `sys.getsizeof()` or memory profilers.

---

Would you like practice exercises or visual examples next (like comparing linear vs binary search or memory analysis of sorting algorithms)?
