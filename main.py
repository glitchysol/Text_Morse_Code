import string


def main():
    chars = list(string.ascii_lowercase + string.digits)
    morse = ["*-", "-***", "-*-*", "-**", "*", "**-*", "--*", "****", "**", "*---", "-*-", "*-**", "--", "*-", "---",
             "*--*", "--*-", "*-*", "***", "-", "**-", "***-", "*--", "-**-", "-*--", "--**", "-----", "*----", "**---",
             "***--", "****-", "*****", "-****", "--***", "---**", "----*"]

    mc = {chars[i]: morse[i] for i in range(len(chars))}
    mc.update({" ": "  "})
    text = input("Text --> morse code: ").lower()
    morse_code = ""
    for letter in text:
        if letter in string.punctuation:
            raise Exception("Do not include any symbols. Try again.")
        morse_code += f"{mc[letter]}  "
    print(morse_code)


if __name__ == "__main__":
    main()
