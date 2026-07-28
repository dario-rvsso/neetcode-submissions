class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = students
        sa = sandwiches

        c = 0
        while len(st)>0 or len(sa)>0:
            if st[0] == sa[0]:
                st.pop(0)
                sa.pop(0)
                c = 0
            else:
                t = st.pop(0)
                st.append(t)
                c += 1
            if c == len(st):
                break
        return len(st)
            