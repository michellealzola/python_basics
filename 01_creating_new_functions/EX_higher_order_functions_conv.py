#%% md
# # Higher-Order Functions
# 
# ### How to load the data
# 
# ```python
# import pickle
# 
# with open("electroless_plating.pkl", "rb") as f:
#     data = pickle.load(f)
# ```
# 
# ## What Are Higher-Order Functions?
# 
# They’re functions that:
# 
# 1. **Take other functions as input**, or
# 2. **Return functions**
# 
# Python has built-in higher-order functions that help you write **concise, readable** code.
# 
# 
# 
# ## 1. `map(function, iterable)`
# 
# ### Use When:
# 
# You want to **transform** every item in a list (or any iterable).
# 
# ### Think: “Apply this function to each item.”
# 
# ### Example:
# 
# ```python
# nums = [1, 2, 3, 4]
# squares = list(map(lambda x: x**2, nums))
# print(squares)  # [1, 4, 9, 16]
# ```
# 
# 
# 
# ## 2. `filter(function, iterable)`
# 
# ### Use When:
# 
# You want to **select a subset** of items based on a condition.
# 
# ### Think: “Keep only the items that pass this test.”
# 
# ### Example:
# 
# ```python
# nums = [1, 2, 3, 4, 5]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)  # [2, 4]
# ```
# 
# 
# 
# ## 3. `reduce(function, iterable)` (from `functools`)
# 
# ### Use When:
# 
# You want to **reduce a list to a single value** (like sum, product, max, etc.).
# 
# ### Think: “Combine items step by step.”
# 
# ### Example:
# 
# ```python
# from functools import reduce
# 
# nums = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, nums)
# print(product)  # 24
# ```
# 
# 
# 
# ## 4. `sorted(iterable, key=function)`
# 
# ### Use When:
# 
# You want to **sort** a list based on a custom rule.
# 
# ### Example:
# 
# ```python
# words = ['apple', 'banana', 'fig']
# by_length = sorted(words, key=lambda w: len(w))
# print(by_length)  # ['fig', 'apple', 'banana']
# ```
# 
# 
# ## When to Use These
# 
# | Function            | Use Case Example                                                     |
# | ------------------- | -------------------------------------------------------------------- |
# | `map()`             | Apply a transformation to every element (e.g., Fahrenheit → Celsius) |
# | `filter()`          | Keep only the elements that meet a condition (e.g., is even)         |
# | `reduce()`          | Collapse a list into a single value (e.g., multiply all numbers)     |
# | `sorted()` with key | Sort by a rule (e.g., by name length or score)                       |
# 
# 
# 
# ## Why Use Them?
# 
# * They make your code **cleaner** and **more expressive**
# * Often used in **data processing**, **pipelines**, **machine learning**, and **web APIs**
# * Replace repetitive `for` loops with single-line logic
#%%
import operator
import pickle
from functools import reduce
from itertools import chain
#%%
with open('electroless_plating.pkl', 'rb') as electroless_file:
    data = pickle.load(electroless_file)
#%%
data[0].keys()
#%% md
# ## Higher-Order Function Exercises
# 
# 
# 
# ### **1. Use `map()` to extract all `Batch ID`s**
# 
# ```python
# # Output: ['ELP5726', 'ELP8081', ...]
# ```
# 
#%%
batch_id_list = list(map(lambda record: record['Batch ID'], data))
#%%
batch_id_list
#%% md
# ### **2. Use `map()` to compute temperature in Fahrenheit**
# 
# ```python
# # Formula: F = C * 9/5 + 32
# # Output: [192.92, 188.06, ...]
# ```
# 
#%%
f_temp_list = list(map(lambda record: round(record['Bath Temperature (°C)'] * 9 / 5 + 32, 2), data))
#%%
f_temp_list[:5]
#%% md
# ### **3. Use `filter()` to get only batches with 'Pass' in 'Pass/Fail'**
# 
# ```python
# # Output: [record1, record2, ...] where 'Pass/Fail' == 'Pass'
# ```
# 
#%%
pass_list = list(filter(lambda record: record['Pass/Fail'] == 'Pass', data))
#%%
pass_list[:5]
#%% md
# ### **4. Use `filter()` to find all Nickel-plated components**
# 
# ```python
# # Output: records where 'Plating Type' == 'Electroless Nickel'
# ```
# 
#%%
nickel_plating_type_list = list(filter(lambda record: record['Plating Type'] == 'Electroless Nickel', data))
#%%
nickel_plating_type_list[:5]
#%% md
# ### **5. Use `map()` to create a summary list of format:**
# 
# ```python
# # "Batch ELP5726 plated with Nickel at 89.4°C"
# ```
# 
#%%
summary_list = list(map(
    lambda record: f'Batch {record["Batch ID"]} plated with {record["Plating Type"].split()[1]} at {record["Bath Temperature (°C)"]}', 
    data
))
#%%
summary_list[:5]
#%% md
# ### **6. Use `filter()` to get all records with Surface Roughness > 1.0**
# 
# ```python
# # Output: list of records with 'Surface Roughness (Ra μm)' > 1.0
# ```
#%%
ra_list_filtered_1 = list(filter(
    lambda record: record['Surface Roughness (Ra μm)'] > 1.0, 
    data
))
#%%
ra_list_filtered_1[:5]
#%% md
# ### **7. Use `reduce()` to calculate total plating time of all records**
# 
# ```python
# from functools import reduce
# # Output: total number in minutes
# ```
# 
#%%
total_plating_time_min = reduce(
    lambda acc, record: round(acc + record['Plating Time (min)'], 2),
    data,
    0  # starting value
)
#%%
total_plating_time_min
#%% md
# ### **8. Use `map()` to round thickness to 1 decimal place**
# 
# ```python
# # Output: [22.1, 14.2, ...]
# ```
# 
#%%
rounded_thickness_list = list(map(
    lambda record: round(record['Thickness (μm)'], 1),
    data
))
#%%
rounded_thickness_list[:5]
#%% md
# ### **9. Use `filter()` + `map()` to find all Copper-plated records with pH > 5, return only their `Batch ID`s**
# 
# ```python
# # Output: ['ELP1234', 'ELP4567', ...]
# ```
#%%
filtered_copper_list = list(filter(
    lambda record: record['Plating Type'] == 'Electroless Copper' and record['pH Level'] > 5, 
    data
))
#%%
batch_ids_with_filtered_copper_list = list(map(
    lambda record: record['Batch ID'], 
    filtered_copper_list
))
#%%
batch_ids_with_filtered_copper_list[:5]
#%% md
# ### **10. Bonus: Use `reduce()` to find the thickest plated component (i.e., max 'Thickness (μm)')**
# 
# ```python
# # Output: record with highest thickness
# ```
# 
#%%
thickest_plate = reduce(
    lambda acc, record: acc if acc['Thickness (μm)'] > record['Thickness (μm)'] else record,
    data
)
#%%
thickest_plate['Batch ID']
#%% md
# ## **5 Problems Using `reduce()`**
# 
# 
# 
# ### **1. Find the record with the lowest surface roughness**
# 
# ```python
# # Goal: Use reduce() to return the record with the smallest value in 'Surface Roughness (Ra μm)'
# # Output: One dictionary (record)
# ```
# 
#%%
sr_smallest = reduce(
    lambda acc, record: acc if acc['Surface Roughness (Ra μm)'] < record['Surface Roughness (Ra μm)'] else record,
    data
)
#%%
sr_smallest
#%% md
# ### **2. Count how many batches passed both 'Visual Inspection' and 'Corrosion Test'**
# 
# ```python
# # Goal: Return an integer count of records where both tests are 'Pass'
# # Output: Total count (e.g., 128)
# ```
#%%
passed_vi_ct_count = reduce(
    lambda acc, record: acc + (
            record['Pass/Fail'] == 'Pass' and 
            record['Visual Inspection'] == 'Pass' and 
            record['Corrosion Test'] == 'Pass'
    ), 
    data,
    0
)
#%%
passed_vi_ct_count
#%% md
# ### **3. Calculate the average adhesion strength (MPa)**
# 
# ```python
# # Goal: Sum all adhesion values, divide by count
# # Use reduce() to get total, then len(data)
# # Output: Average value (float)
# ```
#%%
total_as_mpa = reduce(
    lambda acc, record: acc + (record['Adhesion Strength (MPa)']),
    data,
    0
)
#%%
total_as_mpa
#%%
average_as_mpa = round(total_as_mpa / len(data), 2)
#%%
average_as_mpa
#%% md
# ### **4. Build a comma-separated string of all Operator IDs**
# 
# ```python
# # Goal: Return a single string: "TECH101, TECH202, TECH303, ..."
# # Output: One string
# ```
#%%
operator_id_list = reduce(
    lambda id_, record: id_ + [record['Operator ID']], 
    data, 
    []
)
#%%
operator_id_list[:5]
#%%
# single string
', '.join(operator_id_list[:5])
#%% md
# ### **5. Find the maximum phosphorus content (excluding NaN)**
# 
# ```python
# # Goal: Return the highest numeric value for 'Phosphorus Content (%)'
# # Be sure to skip if value is NaN
# # Output: Float (e.g., 11.96)
# ```
# 
#%%
import math

max_phosphorus = reduce(
    lambda acc, record: max(acc, record['Phosphorus Content (%)'])
    if not math.isnan(record['Phosphorus Content (%)']) else acc,
    data,
    0
)
#%%
max_phosphorus
#%% md
# # Creating custom higher-order functions that:
# 
# 
# 
# ## 1. **Take Other Functions as Input**
# 
# ### Example:
# 
# ```python
# def apply_to_batch(record, func):
#     return func(record['Batch ID'])
# ```
# 
# You can then do:
# 
# ```python
# result = apply_to_batch({'Batch ID': 'ELP1234'}, lambda x: f"Batch: {x}")
# ```
# 
# 
# ## 2. **Return Functions (Closures)**
# 
# ### Example:
# 
# ```python
# def make_temperature_adjuster(offset):
#     def adjust(temp):
#         return temp + offset
#     return adjust
# ```
# 
# Then:
# 
# ```python
# adjust_up = make_temperature_adjuster(5)
# print(adjust_up(90))  # → 95
# ```
# 
# 
#%% md
# ## **Custom Higher-Order Function Problems**
# 
# ### **1. Write a function `apply_to_all_batches(data, func)`**
# 
# It should apply the given function `func` to every record in the dataset and return a list of results.
#%%
def apply_to_all_batches(record, func):
    return [func(record) for record in data]
#%%
result = apply_to_all_batches(
    data, 
    lambda x: f'Record {x["Batch ID"]}, {x["Operator ID"]}, {x["Pass/Fail"]}'
)
#%%
result[:5]
#%% md
# ### **2. Write a function `is_property_above(field, threshold)`**
# 
# It should return another function that checks if `record[field] > threshold`.
# 
# Example:
# 
# ```python
# check_temp = is_property_above("Bath Temperature (°C)", 90)
# ```
# 
#%%
def is_property_above(field, threshold):
    return lambda record: record[field] > threshold
#%%
check_temp = is_property_above('Bath Temperature (°C)', 90)
#%%
check_temp(data[0])
#%%
data[0]
#%%
# apply to all batch
hot_batches = list(filter(check_temp, data))
#%%
hot_batches[:5]
#%% md
#  ### **3. Write a function `format_report(field)`**
# 
# It should return a function that takes a record and returns a string:
# `"Batch ELP1234: Thickness = 22.3 μm"`
#%%
def format_report(field):
    return lambda record: f'Batch {record[field]}: {record['Thickness (μm)']} μm'
#%%
formated_list = list(map(format_report('Batch ID'), data))
#%%
formated_list[:5]
#%% md
# ### **4. Write a function `filter_records(data, condition_func)`**
# 
# It should take a function and return only the records where that function returns `True`.
# 
#%%
def filter_records(record, condition_func):
    return [record for record in data if condition_func(record)]
#%%
filtered_records = filter_records(
    data,
    lambda record: record['Bath Temperature (°C)'] < 90
)
#%%
filtered_records[:5]
#%% md
# ### **5. Write a function `report_generator(fields)`**
# 
# It should return a function that, when given a record, returns a summary string of all those fields.
#%%
def report_generator(fields):
    return lambda record: ', '.join(str(record[field]) for field in fields)
    
#%%
report_string = report_generator(['Batch ID', 'Machine ID', 'Pass/Fail'])
#%%
formatted = list(map(report_string, data))
#%%
formatted[:3]
#%% md
# ### **6. Write a function `compose(f, g)`**
# 
# It should return a new function that combines `f(g(x))`.
# 
# Test it on simple math:
# 
# ```python
# add3 = lambda x: x + 3
# square = lambda x: x * x
# square_then_add3 = compose(add3, square)
# print(square_then_add3(2))  # Output: 7
# ```
# 
#%%
def compose(f, g):
    return lambda x: f(g(x))    
    
#%%
add_2_to_temp = lambda x: x + 2
#%%
square_temp = lambda x: x ** 2
#%%
square_then_add_to_temp = compose(add_2_to_temp, square_temp)
#%%
composed_list = list(map(
    lambda record: round(square_then_add_to_temp(record['Bath Temperature (°C)']), 2), 
    data
))
#%%
composed_list[:5]
#%% md
# ### **7. Write a function `plating_analyzer(field)`**
# 
# It returns a function that takes a record and returns `"HIGH"` if `record[field] > 20`, else `"LOW"`.
# 
#%%
def plating_analyzer(field):
    return lambda record: 'HIGH' if record[field] > 20 else 'LOW'
#%%
plating_analyzed_list = list(map(
    plating_analyzer('Adhesion Strength (MPa)'), 
    data
))
#%%
plating_analyzed_list[:5]
#%% md
# ### **8. Write a function `make_scaler(field, factor)`**
# 
# It returns a function that scales `record[field]` by `factor`.
#%%
def make_scaler(field, factor):
    return lambda record: round(record[field] / factor, 2)
#%%
scaled_list = list(map(
    make_scaler('pH Level', 1.01),
    data
))
#%%
scaled_list[:5]
#%% md
# ### **9. Write a function `apply_many(funcs)`**
# 
# It returns a function that applies a list of functions to a single input and returns a list of outputs.
# 
#%%
def apply_many(funcs):
    return lambda x: [func(x) for func in funcs]
#%%
func1 = lambda record: round(record['Adhesion Strength (MPa)'] *1.01, 2)
#%%
import math as m
func2 = lambda record: (
    0 if m.isnan(record['Phosphorus Content (%)']) 
    else
    round(record['Phosphorus Content (%)'] + 1.01, 2)
)

#%%
outputs_list = list(map(
    apply_many([func1, func2]),
    data
))
#%%
outputs_list[:5]
#%% md
# ### **10. Write a function `make_condition_checker(field, op, value)`**
# 
# It returns a function that compares `record[field]` to `value` using the given operator (`>`, `<`, `==`, etc.).
# 
#%%
import operator

ops = {
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '>': operator.gt,
    '>=': operator.ge,
    '<=': operator.le,
}
 
#%%
def make_condition_check(field, op, value):
    if op not in ops:
        raise ValueError(f'Operator {op} not supported')
    return lambda record: ops[op](record[field], value)
#%%
temp_cond_list = list(map(
    make_condition_check('Bath Temperature (°C)' , '>', 90),
    data
))
#%%
temp_cond_list[:5]
#%% md
# # More Practice Problems
#%% md
# ## A. **Functions that Take Other Functions as Input**
# 
# ### **1. `apply_twice(func, value)`**
# 
# Apply a function `func` twice to a `value`.
# 
# ```python
# # Example: apply_twice(lambda x: x + 2, 5) ➜ 9
# ```
#%%
def apply_twice(func, value):
    result1 = func(value)
    return round(func(result1), 2)
#%%
func = lambda x: x + 1.02
#%%
twice_value_list = list(map(
    lambda record: apply_twice(func, record['Bath Temperature (°C)']),
    data
))
#%%
twice_value_list[:5]
#%% md
# ### **2. `filter_and_transform(data, condition, transform)`**
# 
# Filter the data using `condition`, then apply `transform`.
# 
# ```python
# # Example: filter_and_transform(data, lambda x: x > 5, lambda x: x * 2)
# ```
#%%
def filter_and_transform(data, condition, transform):
    return [transform(record) for record in data if condition(record)]
#%%
condition = lambda record: record['Adhesion Strength (MPa)'] > 20
#%%
transform = lambda record: 'OK' if record['Pass/Fail'] else 'NOT OK'
#%%
result = filter_and_transform(data, condition, transform)
#%%
result[:10]
#%% md
# ### **3. `chain_functions(f1, f2, f3)`**
# 
# Return a function that applies `f1(f2(f3(x)))`.
# 
# ```python
# # Example: f = chain_functions(add3, square, halve)
# # f(2) ➜ add3(square(halve(2)))
# ```
#%%
def chain_functions(f1, f2, f3):
    return lambda record: f1(f2(f3(record)))
#%%
function1 = lambda x: round(x * 1.5, 1)
#%%
function2 = lambda x: round(x * 2, 2)
#%%
function3 = lambda record: round(record['Phosphorus Content (%)'], 2) if not math.isnan(record['Phosphorus Content (%)']) else 0
#%%
chain_func_results = list(map(
    chain_functions(function1, function2, function3),
    data
))
#%%
chain_func_results[:5]
#%% md
# ### **4. `batch_apply(funcs, value)`**
# 
# Takes a list of functions and applies all of them to the same value.
# 
# ```python
# # Example: batch_apply([square, double, negate], 3) ➜ [9, 6, -3]
# ```
# 
#%%
def batch_apply(funcs, value):
    return [round(func_(value), 2) for func_ in funcs]
#%%
square = lambda x: x ** 2
#%%
double = lambda x: x * 2
#%%
negate = lambda x: x * (-1)
#%%
batch_list = list(map(
    lambda record: batch_apply([square, double, negate], record['Adhesion Strength (MPa)']),
    data
))
#%%
batch_list[:5]
#%% md
# ### **5. `custom_map(data, transformer)`**
# 
# Implement your own version of `map()` using a loop.
# 
# ```python
# # Example: custom_map([1, 2, 3], lambda x: x * 10)
# ```
#%%
def custom_map(data_, transform_):
    list_ = []
    for item in data_:
        list_.append(transform_(item))
    return list_
#%%
transformer = lambda x: x
#%%
custom_map_list = custom_map(data, transformer)
#%%
custom_map_list[:5]
#%% md
# ## B. **Functions That Return Other Functions**
# 
# ### **6. `make_divider(divisor)`**
# 
# Returns a function that divides any input by `divisor`.
# 
# ```python
# # f = make_divider(5)
# # f(25) ➜ 5.0
# ```
#%%
def make_divider(divisor):
    def divider(field):
        return lambda record: round(record[field] / divisor, 2)
    return divider
#%%
f = make_divider(2)
#%%
f_divided_2 = list(map(
    f('Thickness (μm)'),
    data
))
#%%
f_divided_2[:5]
#%% md
# ### **7. `make_power_func(n)`**
# 
# Returns a function that raises input to the power of `n`.
# 
# ```python
# # square = make_power_func(2)
# # square(4) ➜ 16
# ```
#%%
def make_power_func(n):
    def power(field):
        return lambda record: round(record[field] ** n, 2)
    return power
#%%
power_func = make_power_func(3)
#%%
power_func_list = list(map(
    power_func('Surface Roughness (Ra μm)'),
    data
))
#%%
power_func_list[:5]
#%% md
# ### **8. `make_filter_func(threshold)`**
# 
# Returns a function that checks if a number is greater than `threshold`.
# 
# ```python
# # f = make_filter_func(100)
# # f(120) ➜ True
# ```
# 
#%%
def make_filter_func(threshold):
    def filter_func(field):
        return lambda record: record[field] > threshold
    return filter_func
#%%
filter_function = make_filter_func(90)
#%%
filtered_list = list(map(
    filter_function('Bath Temperature (°C)'),
    data
))
#%%
filtered_list[:5]
#%% md
# ### **9. `compose_all(func_list)`**
# 
# Returns a function that applies all functions in `func_list` in order.
# 
# ```python
# # f = compose_all([double, square, add3])
# # f(2) ➜ add3(square(double(2)))
# ```
# 
#%%
def apply_all(funcs, value):
    for func_ in funcs:
        value = func_(value)
    return value
#%%
def compose_all(func_list):
    def composed_func(field):
        return lambda record: round(
            apply_all(func_list, record[field]),
            2
        )
    return composed_func
#%%
func1 = lambda x: x * 2
#%%
func2 = lambda x: x ** 2
#%%
f = compose_all([func1, func2])
#%%
composed_func_list = list(map(
    f('Bath Temperature (°C)'),
    data
))
#%%
composed_func_list[:5]
#%% md
# ### **10. `make_record_checker(field, op_func, value)`**
# 
# Returns a function that checks if `record[field]` satisfies `op_func(..., value)`.
# 
# ```python
# # f = make_record_checker('pH', operator.gt, 4.9)
# # f({'pH': 5.0}) ➜ True
# ```
#%%
pH_data = [{'pH Level': record['pH Level']} for record in data]
#%%
pH_data[:5]
#%%
def make_record_checker(field, op_function, value):
    return lambda record: op_function(record[field], value)
#%%
f = make_record_checker('pH Level', operator.gt, 4.9)
#%%
filtered = list(filter(
    f,
    pH_data
))
#%%
filtered[:5]
#%%
