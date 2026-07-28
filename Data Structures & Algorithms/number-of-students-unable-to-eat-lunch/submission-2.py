class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = students
        sa = sandwiches

        i = 0
        j = 0
        c = 0
        while c < len(st) and j < len(sa):
            if st[i] == sa[j]:
                st[i] = -1
                i = (i + 1) % len(st)
                j += 1
                c = 0
            else:
                i = (i + 1) % len(st)
                c += 1 
        return len(sa) - j
            