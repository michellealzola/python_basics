## 🧠 What is “Counting Instructions”?

**Counting Instructions** means identifying how many **primitive operations** (or steps) an algorithm performs when it runs. These operations can include:

* Assignments (`x = 1`)
* Comparisons (`if x > y`)
* Arithmetic operations (`x + y`)
* Loops and iterations
* Function calls

We do this to understand the **actual work** done by the algorithm—especially how it *scales* with input size.

---

## 🎯 Why Do We Count Instructions?

Because:

1. **It helps estimate performance**: More steps = slower algorithm.
2. **It reveals bottlenecks**: A poorly written loop or redundant operation can slow everything down.
3. **It leads us to Big-O Notation**: Once we know how the steps grow, we can summarize it with `O(n)`, `O(n^2)`, etc.

---

## 📏 How to Count Instructions: Step-by-Step

### Step 1: Identify the basic operations

These are operations you assume take **constant time**:

* Assignments
* Comparisons
* Arithmetic
* Return statements

Each of these counts as **1 instruction**.

---

### Step 2: Count each inside loop structures

Loops multiply the number of instructions:

* A loop running `n` times that does 3 operations per iteration = `3n` instructions.

---

### Step 3: Add everything together

Then simplify to the **dominant term** for Big-O.

---

## 🔍 Examples (with full step-by-step counts)

---

### 🧪 Example 1: Constant Time

```python
def add_two_numbers(a, b):
    return a + b
```

* `a + b` (1 operation)
* `return` (1 operation)

✅ **Total**: 2 steps → **O(1)**

---

### 🔁 Example 2: Linear Time

```python
def print_list(lst):
    for item in lst:
        print(item)
```

* `for item in lst:` → runs `n` times
* `print(item)` → 1 instruction per iteration

✅ **Total**: `n` instructions → **O(n)**

---

### 🔂 Example 3: Count + Arithmetic

```python
def sum_list(lst):
    total = 0              # 1
    for item in lst:       # n iterations
        total += item      # n additions
    return total           # 1
```

✅ Total = `1 (assign) + n (loop) + n (additions) + 1 (return)` = `2n + 2`
→ **O(n)**

---

### 🔄 Example 4: Nested Loop (Quadratic)

```python
def print_pairs(lst):
    for i in lst:
        for j in lst:
            print(i, j)
```

* Outer loop runs `n` times
* Inner loop also runs `n` times
* `print(i, j)` → 1 op per inner loop

✅ Total = `n * n = n²` → **O(n²)**

---

### 🔃 Example 5: Binary Search

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

* Loop halves input each time → log₂(n) times
* Each loop iteration does a few constant operations (\~4–6)

✅ Total \~ `c * log n` → **O(log n)**

---

## 📘 Guidelines for Counting Instructions

| Code Component | What to Count                        |
| -------------- | ------------------------------------ |
| Assignments    | Count each one as 1 step             |
| Arithmetic ops | Count each (`+`, `-`, `*`, `/`) as 1 |
| Conditionals   | Count comparison as 1                |
| Loops          | Multiply inner steps by iterations   |
| Nested Loops   | Multiply all levels of loops         |
| Function Calls | Count call + the instructions inside |

---

## 🧪 Practice: 10 Exercises

Try counting the number of primitive instructions for each and express the total using Big-O.

---

### **Exercise 1**

```python
def find_first(lst, target):
    for item in lst:            # n
        if item == target:      # n (comparison)
            return True         # 1 (up to 1, if condition is met)
    return False                # 1
                                # 2n + 1 --> O(n)
```                             

---

### **Exercise 2**

```python
def max_of_two(a, b):
    if a > b:                   # 1 (comparison, no n involved)
        return a                # 1
    else:                       # (only 1 branch of if or else is executed)
        return b                # (only 1 branch of if or else is executed)
                                # 2 --> O(1)
```

---

### **Exercise 3**

```python
def reverse_list(lst):
    return lst[::-1]            # 1 + n --> O(n)
```

Yes — this analysis is **mostly correct**, but let’s clarify **why** the slicing operation `lst[::-1]` takes **O(n)** time and walk through the details so it's 100% clear.

---

## ✅ Code:

```python
def reverse_list(lst):
    return lst[::-1]
```

---

## 🔍 What's Happening?

* The slicing syntax `lst[::-1]` is Python's concise way of **reversing a list**.
* It creates a **new list** with the elements in reverse order.
* Even though it’s one line, under the hood Python must:

  * **Visit every element once**
  * **Copy it into a new position**
* So, it's not `O(1)` — it's still **linear time**.

---

## 🧮 Instruction Count:

| Step                                     | Count          |
| ---------------------------------------- | -------------- |
| Create a new list (copying `n` elements) | `n` operations |
| Return the new list                      | 1 operation    |

✅ **Total** = `n + 1` → which simplifies to **O(n)**

---

## ✅ Time Complexity

Even though it **looks short**, Python must:

* Allocate memory for the new list
* Copy all items into reversed positions

So:

* **Time complexity**: `O(n)`
* **Space complexity**: also `O(n)` (because it builds a new list)

---

## 🛠 Final Verdict

The image is correct in:

* Stating that it takes `1 + n` steps
* Concluding **O(n)** time complexity

---

### **Exercise 4**

```python
def is_sorted(lst):
    for i in range(len(lst) - 1):           # n - 1 (loop runs n - 1 times) --> n = len(lst)
        if lst[i] > lst[i+1]:               # n - 1 (comparison inside loop)
            return False                    # up to 1 if triggered
    return True                             # 1 (only if not returned early)
                                            # 2(n - 1) + 1 = 2n - 1 --> O(n)
```

---

### **Exercise 5**

```python
def multiply_matrix(A, B):
    n = len(A)                                      # (1)
    result = [[0]*n for _ in range(n)]              # (n) <- outer loop, each creates n elements -> n^2 operations
    for i in range(n):                              # n
        for j in range(n):                          # n
            for k in range(n):                      # n
                result[i][j] += A[i][k] * B[k][j]   # 1 (mult + add) = 2 operations
    return result                                   # 1
                                                    # 2n^3 + n^2 + 2 --> O(n^3)
```

---

### **Exercise 6**

```python
def double_elements(lst):
    for i in range(len(lst)):               # n iterations
        lst[i] *= 2                         # 1 multiplication per iteration
                                            # n * 1 --> O(n)
```

---

### **Exercise 7**

```python
def factorial(n):
    if n == 0:                              # n + 1 (1 comparison per call)
        return 1                            # n (1 return only once)
    else:
        return n * factorial(n - 1)         # n + 1 (1 mult + 1 return per call)
                                            # 3n + 2 --> O(n)
```

No worries — let’s make this crystal clear with a **table and trace** so you can **see where `n` comes in** and **why the total operations are based on `n`.**

---

## ✅ Code:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

---

## 💡 What is `n`?

`n` is the **input value** to the function.
For example:
`factorial(4)` means `n = 4`

---

## 🔁 What Happens When You Run `factorial(4)`?

Here’s the **call stack**:

| Function Call  | What it does                       |
| -------------- | ---------------------------------- |
| `factorial(4)` | 4 \* factorial(3) → multiplication |
| `factorial(3)` | 3 \* factorial(2) → multiplication |
| `factorial(2)` | 2 \* factorial(1) → multiplication |
| `factorial(1)` | 1 \* factorial(0) → multiplication |
| `factorial(0)` | return 1 → base case               |

✅ That’s a total of **5 calls** for `n = 4` → `n + 1` calls in general.

---

## 🔎 Count the Instructions per Call

Let’s now count the **basic operations** in each call:

| Operation Type       | How many times?           | Why                                   |
| -------------------- | ------------------------- | ------------------------------------- |
| `if n == 0:`         | `n + 1` times             | Every call checks the base case       |
| `return 1`           | 1 time (only at `n == 0`) | Base case is hit once                 |
| `n * factorial(...)` | `n` times                 | Happens in all calls except base case |
| `return ...`         | `n` times                 | One return per multiplication call    |

---

## 📊 Summary of Total Operations

| Instruction       | Count    |
| ----------------- | -------- |
| Comparisons       | `n + 1`  |
| Multiplications   | `n`      |
| Return statements | `n + 1`  |
| **Total**         | `3n + 2` |

---

## ✅ Final Simplified Answer

* Total operations ≈ `3n + 2` → **We drop constants in Big-O**
* ✅ **Time Complexity = O(n)**
* ✅ **Space Complexity = O(n)** (due to recursion call stack)

---

## 🔁 Visual Summary (for `factorial(3)`)

```python
factorial(3)
 → 3 * factorial(2)     # 1 comparison + 1 mult + 1 return
    → 2 * factorial(1)  # 1 comparison + 1 mult + 1 return
        → 1 * factorial(0)  # 1 comparison + 1 mult + 1 return
            → 1            # 1 comparison + 1 return
```

✅ 4 comparisons
✅ 3 multiplications
✅ 4 returns

→ `3n + 2` total → **O(n)**



---

### **Exercise 8**

```python
def count_zeroes(matrix):
    count = 0                   # 1
    for row in matrix:          # n 
        for item in row:        # n * n = n^2
            if item == 0:       # n^2 comparisons
                count += 1      # up to n^2 increments
    return count                # 1
                                # 2n^2 + 2 --> O(n^2)
```

---

### **Exercise 9**

```python
def print_even(lst):
    for i in range(0, len(lst), 2):     # n / 2 
        print(lst[i])                   # 1 per n/2 loop
                                        # n / 2 --> O(n)
```

---

### **Exercise 10**

```python
def mystery(n):
    i = 1               # 1 operation
    while i < n:        #  log2(n) iterations
        i *= 2          # 1 operation per iteration
        print(i)        # 1 operation per iteration
                        # 2log2(n) + 1 --> O(log2(n))
```

