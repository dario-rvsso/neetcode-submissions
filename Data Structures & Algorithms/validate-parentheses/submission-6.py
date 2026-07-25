class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        molecule = []
        valid = True
        closeToOpen = {")":"(", "]":"[", "}":"{"}
        try:
            for i in range(n):
                atom = s[i]
                match atom:
                    case '(' | '[' | '{':
                        molecule.append(atom)
                    case _:
                        if atom in closeToOpen:
                            x = molecule.pop()
                            if x != closeToOpen[atom]:
                                valid = False
                                break
            if len(molecule) != 0:
                valid = False
        except IndexError:
            valid = False
        
        return valid
                            

                    