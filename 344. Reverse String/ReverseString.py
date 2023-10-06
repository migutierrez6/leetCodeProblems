f = ["h", "e", "l", "l", "o"]
d = ["dog", "cat", "bird", "turtle"]


def reverseString(s):
    # Two pinters one to 0 the second to the end
    left = 0
    right = len(s) - 1
    # while left pointer is less than the right I switch places and increment
    # the pointer after the switch
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    print(s)


reverseString(d)
