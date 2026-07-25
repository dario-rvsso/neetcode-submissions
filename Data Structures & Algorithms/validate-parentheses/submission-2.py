class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        molecule = []
        valid = True
        try:
            for i in range(n):
                atom = s[i]
                match atom:
                    case '(' | '[' | '{':
                        molecule.append(atom)
                    case ')':
                        x = molecule.pop()
                        if x != '(':
                            valid = False
                            break
                    case ']':
                        x = molecule.pop()
                        if x != '[':
                            valid = False
                            break
                    case '}':
                        x = molecule.pop()
                        if x != '{':
                            valid = False
                            break
            if len(molecule) != 0:
                valid = False
        except IndexError:
            valid = False
        finally:
            pass
        
        return valid
                            

                    