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
