class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # Count characters in s1
        for char in s1:
            count1[ord(char) - ord('a')] += 1

        # Create the first window in s2
        window_size = len(s1)

        for i in range(window_size):
            count2[ord(s2[i]) - ord('a')] += 1

        # Check the first window
        if count1 == count2:
            return True

        # Slide the window
        for i in range(window_size, len(s2)):
            # Add the new character
            count2[ord(s2[i]) - ord('a')] += 1

            # Remove the character leaving the window
            count2[ord(s2[i - window_size]) - ord('a')] -= 1

            # Check if frequencies are equal
            if count1 == count2:
                return True

        return False