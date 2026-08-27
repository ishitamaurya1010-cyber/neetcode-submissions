class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # pointer for word
        j = 0  # pointer for abbr

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                # Leading zero is invalid
                if abbr[j] == '0':
                    return False

                skip = 0

                # Parse the full number
                while j < len(abbr) and abbr[j].isdigit():
                    skip = skip * 10 + int(abbr[j])
                    j += 1

                i += skip
            else:
                # The abbreviation character must match the word character
                if word[i] != abbr[j]:
                    return False

                i += 1
                j += 1

        return i == len(word) and j == len(abbr)