class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
        mag_counter = Counter(magazine)
        note_counter = Counter(ransomNote)

        return mag_counter & note_counter == note_counter
