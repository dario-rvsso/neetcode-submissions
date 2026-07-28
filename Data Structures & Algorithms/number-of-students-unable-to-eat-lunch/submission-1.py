class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = students[::-1]
        sa = sandwiches[::-1]

        c = 0
        while len(st)>0 or len(sa)>0:
            if st[len(st)-1] == sa[len(sa)-1]:
                st.pop()
                sa.pop()
                c = 0
            else:
                t = st.pop()
                st.insert(0,t)
                c += 1
            if c == len(st):
                break
        return len(st)
            