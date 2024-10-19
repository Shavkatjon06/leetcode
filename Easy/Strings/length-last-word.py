def lengthOfLastWord(self, s: str) -> int:
    return len(s.strip().split(" ")[-1])  # " Hello World  ", strip() to remove spaces, split(" ") to make array
    # elements, [-1] get the last element
