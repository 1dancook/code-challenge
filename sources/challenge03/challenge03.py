# ---------------------------------
# CHALLENGE 3


def generate_zipfile_password(text):
    return "".join(
        [
            chr(ord(char) - 2) if n % 2 else chr(ord(char) + 2)
            for n, char in enumerate(text)
        ]
    )


print(
    "an example password", generate_zipfile_password("aVeryStrongPassword")
)  # cTgp{QvpqliNcquuqpf

print("zipfile pass: ", generate_zipfile_password("topsecret.zip"))

from base64 import b64decode, b64encode

print(
    "encoded message: ",
    b64encode(
        b"Hey, you got it!\n\nWe'd like an extra large pepperoni pizza with extra cheese.\n\nWe'll be there in 10 minutes to pick it up."
    ).decode("utf-8"),
)

print("secret message example: ", b64decode("YW4gZXhhbXBsZQ==").decode("utf-8"))

with open("message.txt", "r") as f:
    text = f.read()
    print("top secret message: ", b64decode(text).decode("utf-8"))
