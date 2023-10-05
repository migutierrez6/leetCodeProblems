w = "MCCVII"


def romanToInt(word):
    # larget to smallest: add them up
    # smaller before larger: substract smaller

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0

    for i in range(len(word)):
        # check if the value is not out of bounds i + 1 < len(word)
        # whats the value of the caracter at index i = roman[word[i]]
        # and check if that value is smaller of = <
        # the next caracter = roman[word[i + 1]]:

        if i + 1 < len(word) and roman[word[i]] < roman[word[i + 1]]:
            # if its smaller we substract the value to res
            res -= roman[word[i]]
        else:
            # if its larger we add the value to res
            res += roman[word[i]]

    return res


print(romanToInt(w))
