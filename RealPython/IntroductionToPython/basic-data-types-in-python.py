# integers
# any length up to the memory limit of your computer
# default is decimal (base 10) - you can change the base
a_dec = 1235
a_bin = 0b101010111
a_oct = 0o454312
a_hex = 0xac4d

print(a_dec)
print(a_bin)
print(a_oct)
print(a_hex)

my_num_string = "1235"
my_num_int = int(my_num_string)

print(my_num_string)            # note that in the prompt you do NOT see the quotation marks around the printed value of this string variable
print(type(my_num_string))      
print(my_num_int)
print(type(my_num_int))

a_dec_in_bin = bin(a_dec)
a_dec_in_oct = oct(a_dec)
a_dec_in_hex = hex(a_dec)

print(a_dec_in_bin)
print(a_dec_in_oct)
print(a_dec_in_hex)

print("\n\n\n\n")
# floating-point numbers
# any number with a decimal point
# any division operation will return a float
# can be defined using scientific notation

a = 4.2
print(type(a))

b = 4.0
print(type(b))

c = 10
d = 4
e = c / d
f = c // d                                              # floor division truncates the decimal part of return and always returns a integer type
c_float = float(c)
s_scinot = 4e3                                          # scientific notation base 10 returns a float type
print("c ->", c, "\t\ttype(c) ->", type(c))
print("d ->", d, "\t\t\ttype(d) ->", type(d))
print("e = c / d ->", e, "\ttype(e) ->", type(e))
print("f = c // d ->", f, "\ttype(f) ->", type(f))
print("c_float ->", c_float, "\ttype(c_float) ->", type(c_float))

d = 5
e  = c / d
print("c ->", c, "\t\ttype(c) ->", type(c))
print("d ->", d, "\t\t\ttype(d) ->", type(d))
print("e = c / d ->", e, "\ttype(e) ->", type(e))


x = 0.2
y = 0.1
expected_res = 0.3
z = x + y
print(z)                        # note the imprecision in the result of floating point arithmetic
print(expected_res)            
print(x == expected_res)        # notice that due to the imprecision in floating point arithmetic, the expected result True actually winds up being False

print("\n\n\n\n")
# complex numbers
complex_num = 2 + 3j            # you can do complex number aritmetic with python
print(complex_num)
print(type(complex_num))

print("\n\n\n\n")
# strings
# a sequence of zero or more characters
# can be enclosed in single quotes (') or double quotes (")
# formats include raw and triple-quoted strings
string_a = "Hello World"
string_b = 'Hello World'
print(string_a)
print(string_b)
print(type(string_a))
print(type(string_b))

g = 51
string_g = str(g)
print("g ->", g, "\t\t\ttype(g) ->", type(g))
print("string_g ->", string_g, "\t\t\ttype(string_g) ->", type(string_g))

s = 'He said "I wasn\'t at school today" to me'
print(s)

d = "This is line 1.\nThis is line 2."
print(d)

e = "One\tTwo\tThree\tFour"
print(e)

# escape characters --> \'  \"  \\  \n  \r  \t  \b  \f  \v  \onn  \xnn

string_r = "One Line\nTwo!"
print(string_r)
raw_string_r = r"One Line\nTwo!"
print(raw_string_r)         # useful in regular expressions (regex)

triple_string = """This is a triple-quoted strings"""
print(triple_string)
multi_line_triple_string = """This string spans across multiple lines.
        It isn't going wrong when I do this!
Even if I do multiple empty lines...


It still works!"""
print(multi_line_triple_string)

def my_function(value):
    """Takes a value and prints it to the screen"""
    print(f"{value} is a nice value")
    return

my_function("Hello World")

print("\n\n\n\n")
# booleans
true_a = True
print(true_a)
print(type(true_a))

false_a = False
print(false_a)
print(type(false_a))

a = 1
b = 0
bool_a = bool(a)
bool_b = bool(b)

print(bool_a)
print(bool_b)

d = 5
print(d == 5)
print(d == 4)

def evaluate_truthiness(value):
    if value:
        print(f"{value} evaluates to true!")
    else:
        print(f"{value} evaluates to false!")

evaluate_truthiness(0)
evaluate_truthiness(1)
evaluate_truthiness(True)
evaluate_truthiness(False)
evaluate_truthiness("true")
evaluate_truthiness("false")
evaluate_truthiness("True")
evaluate_truthiness("False")
evaluate_truthiness([])
evaluate_truthiness([1, 2])
evaluate_truthiness({})
evaluate_truthiness({"value": False})

print("\n\n\n\n")
# built-in functions
# composite data types
a = [1, 2, 3, 4, 5]             # lists are mutable

print(a)
print(type(a))

print(a[0])
print(a[1])
print(a[-1])
print(a[1:3])

a[1] = 6
print(a)

b = (1, 2, 3, 4, 5)             # tuples are immutable
print(b)
print(type(b))

print(b[0])
print(b[1])
print(b[-1])
print(b[1:3])

a = [1, 2, 3, 3, 3, 4, 4, 5]
b = set(a)                      # a set contains unique values
print(a)
print(b)
print(type(b))
c = list(b)
print(c)

d = dict()
d["name"] = "Darren"
print(d)
print(type(d))

e = {}
e["name"] = "Darren"
e["age"] = 46
print(e)
print(type(e))
print(e["age"])
print(e.get("country"))