# -------------------------------------
# CHALLENGE 1

strange_sign = "#h3 *3!# =+$$a"

strange_sign = strange_sign.replace("3", "e")
strange_sign = strange_sign.replace("$", "z")
strange_sign = strange_sign.replace("%", "j")
strange_sign = strange_sign.replace("+", "i")
strange_sign = strange_sign.replace("=", "p")
strange_sign = strange_sign.replace("(", "l")
strange_sign = strange_sign.replace("#", "t")
strange_sign = strange_sign.replace("*", "b")
strange_sign = strange_sign.replace("!", "s")

print(strange_sign.title())


# Alternate for Challenge 1

swap = {
    "e": "3",
    "z": "$",
    "j": "%",
    "i": "+",
    "p": "=",
    "l": "(",
    "t": "#",
    "b": "*",
    "s": "!",
}

strange_sign = "#h3 *3!# =+$$a"
for key, value in swap.items():
    strange_sign = strange_sign.replace(value, key)
restaurant_name = strange_sign.title()
print("restaurant name: ", restaurant_name)


# Alternate for Challenge 1
swap = {
    "3": "e",
    "$": "z",
    "%": "j",
    "+": "i",
    "=": "p",
    "(": "l",
    "#": "t",
    "*": "b",
    "!": "s",
}

normal_sign = "".join(swap.get(char, char) for char in strange_sign).title()
print("normal sign: ", normal_sign)
