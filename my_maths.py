def calculate(strg, int1, int2):
    result = 0
    if strg == "add":
        result = int1 + int2
    elif strg == "multiply":
        result = int1 * int2
    elif strg == "divide":
        result = int1 / int2
    else:
        result = "You have inserted the wrong arguments, try again."
    return result

