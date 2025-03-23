# Task 1
def hello():
    return "Hello!"
hello()

# Task 2
def greet(name):
    return f"Hello, {name}!"
print(greet("Ibrahim"))

# Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc(5, 6)) 
print(calc(10, 2, "add"))  
print(calc(10, 0, "divide"))  
print(calc("hello", 3, "multiply")) 


# Task 4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "_":
                return "Invalid data type!"
    except ValueError:
        return f"You can't convert {value} into a {data_type}."

print(data_type_conversion("120", "int"))
print(data_type_conversion("10.5", "float")) 
print(data_type_conversion(2, "float"))
print(data_type_conversion(85.5, "str"))
print(data_type_conversion("apple", "int"))

# Task 5
def grade(*args):
    try:
        if not args:
            return "Invalid data was provided."

        average = sum(args) / len(args)

        match average:
            case avg if avg >= 90:
                return "A"
            case avg if avg >= 80:
                return "B"
            case avg if avg >= 70:
                return "C"
            case avg if avg >= 60:
                return "D"
            case _:
                return "F"
    except TypeError:
        return "Invalid data was provided."

print(grade(75,85,95))

# Task 6
def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result

print(repeat("up,", 4))

# Task 7
def student_scores(mode, **kwargs):
    try:
        if not kwargs:
            return "No scores were provided."
        match mode:
            case "best":
                return max(kwargs, key=kwargs.get)
            case "mean":
                return sum(kwargs.values()) / len(kwargs)
            case _:
                return "Invalide mode!"
    except TypeError:
        return "invalid data provided!"

print(student_scores("mean", Tom=75, Dick=89, Angela=91))
print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50 ))

# Task 8
def titleize(nameToBeTiteize):
    small_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = nameToBeTiteize.lower().split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1 or word not in small_words:
            words[i] = word.capitalize()
    return " ".join(words)

print(titleize("war and peace"))
print(titleize("a separate peace"))
print(titleize("after on"))

# Task 9
def hangman(secret, guess):
    return "".join(letter if letter in guess else "_" for letter in secret)

print(hangman("difficulty","ic"))

# Task 10
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    pig_latin_words = []

    for word in words:
            if word[0] in vowels:
                pig_latin_words.append(word + "ay")
            elif word.startswith("squ"):  # Special handling for "squ"
                pig_latin_words.append(word[3:] + "squay")
            elif word.startswith("qu"):  # Special handling for "qu"
                pig_latin_words.append(word[2:] + "quay")
            else:

                for i, letter in enumerate(word):
                    if letter in vowels or word[i:i+2] == "qu":
                        pig_latin_words.append(word[i:] + word[:i] + "ay")
                        break

    return " ".join(pig_latin_words)

print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("cherry"))
print(pig_latin("quiet"))
print(pig_latin("square"))
print(pig_latin("the quick brown fox"))