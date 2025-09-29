"""Checks if a string is a palindrome, ignoring case and accents."""


def ispalindrome(p):
    """Checks if the given string is a palindrome, ignoring case and accents."""
    p = p.lower()
    table = str.maketrans({
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "à": "a", "ç": "c", "ô": "o",
        " ": "", "-": "", "'": "", ",": "",
        "!": "", "?": "", ":": "", ";": "", ".": ""
    })
    p = p.translate(table)
    return p == p[::-1]

def main():
    """Tests the ispalindrome function with various examples."""
    for i in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(i, ispalindrome(i))

if __name__ == "__main__":
    main()
