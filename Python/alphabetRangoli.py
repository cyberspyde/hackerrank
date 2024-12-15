import string
def alphabetRangoli(n):
    alphabet = string.ascii_lowercase[:n][::-1]
    
    lines = []
    for i in range(n):
        pattern = "-".join(alphabet[:i+1])
        lines.append((pattern + pattern[-2::-1]).center(n*4-3, "-"))

    print("\n".join(lines + lines[-2::-1]))

alphabetRangoli(5)