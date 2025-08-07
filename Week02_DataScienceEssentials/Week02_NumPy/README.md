# Week 02 - NumPy Basics

## ✅ Key Concepts

### 🧱 Creating Arrays
- `np.array([1, 2, 3])`: Convert Python list to array
- `np.zeros((2,3))`, `np.ones`, `np.arange`, `np.linspace`

### 📐 Indexing, Slicing, Shape
- Arrays use 0-based indexing: `arr[0,1]`
- Reshaping with `.reshape((rows, cols))`

### ⚙️ Element-wise Operations
- Addition: `a + b`
- Multiplication: `a * b`
- Exponentiation: `a ** 2`

### 🔁 Broadcasting
- Smaller arrays automatically stretch to match shape
- Powerful alternative to writing loops

### 📊 Useful Functions
- `np.sum()`, `np.mean()`, `np.dot()`
- Use `axis=0` (columns) or `axis=1` (rows)

### 🎯 Boolean Indexing
- Create masks to filter data: `arr[arr > 2]`

### 🚀 Performance Comparison
- NumPy is significantly faster than native Python lists for numerical tasks

---

## 🧪 Practice Exercises
- Create a 3x3 matrix with random integers (0–10)
- Normalize an array (subtract mean, divide by std)
- Use boolean masking to filter even numbers
- Compare dot product with matrix multiplication

---

## 🛠 Requirements
Add the following to your `requirements.txt`:


# 📊 NumPy Advanced Tutorial (Week 2 - Extended)

This section covers **advanced NumPy concepts** through focused, copy-paste ready `.py` files. These scripts build on the basics and explore practical use cases, performance optimization, and mini-projects.

---

## 📁 Files Overview

| Filename                            | Description |
|-------------------------------------|-------------|
| `09_axis_operations.py`             | Demonstrates sum/mean operations across rows and columns using `axis` |
| `10_stacking_splitting.py`          | Combines and splits arrays using `vstack`, `hstack`, `hsplit`, `vsplit` |
| `11_fancy_indexing.py`              | Shows how to access elements using advanced (fancy) indexing techniques |
| `12_matrix_operations.py`           | Covers dot product, transpose, and matrix inverse |
| `13_random_generation.py`           | Explores random number generation including integers, floats, and normal distributions |
| `14_performance_benchmark.py`       | Benchmarks NumPy vectorized operations against native Python list operations |
| `15_mini_project_student_grades.py` | A mini-project to analyze student marks: compute averages, rank students, and grade performance |

---

## 💡 Learning Outcomes

By going through this section, you will:

- Learn how to manipulate array dimensions efficiently using `axis`
- Master array merging and splitting strategies
- Apply linear algebra operations for practical purposes
- Use random number generation for simulations and testing
- Benchmark and optimize array-based code using NumPy
- Practice data analysis in a mini-project format

---

## 🧠 Prerequisites

Make sure you have NumPy installed:

```bash
pip install numpy