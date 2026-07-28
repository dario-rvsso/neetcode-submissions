class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = students
        sa = sandwiches

        st_0 = st.count(0)
        st_1 = st.count(1)

        i = 0
        while i < len(sa):
            t = sa[i]
            if t == 0 and st_0 > 0:
                st_0 -= 1
            elif t == 1 and st_1 > 0:
                st_1 -= 1
            else:
                break
            i += 1
        return len(sa) - i
            