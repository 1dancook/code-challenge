# -------------------------------------
# CHALLENGE 2

restaurant_name = "The Best Pizza"


def generate_login_password(text):
    return "".join([chr(ord(c) + 1) for c in text])


print("login pass: ", generate_login_password(restaurant_name))
