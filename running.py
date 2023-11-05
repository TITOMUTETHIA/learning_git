def raindrops(number):
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if result == "":
        result = str(number)
    return result

# Example usage
print(raindrops(28)) # Output: Plong
print(raindrops(30)) # Output: PlingPlang
print(raindrops(34)) # Output: 34