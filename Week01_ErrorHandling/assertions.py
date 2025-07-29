def convert_to_celsius(fahrenheit):
    assert isinstance(fahrenheit, (int, float)), "Input must be a number"
    return (fahrenheit - 32) * 5/9

# Test
print("✅ Celsius:", convert_to_celsius(100))
print("✅ Celsius:", convert_to_celsius(32))

# This will raise an assertion error
print("✅ Celsius:", convert_to_celsius("hot"))
