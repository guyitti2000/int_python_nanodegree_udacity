
def ask_yn(prompt, retries=4, complaint='Enter Y/N!'):
    for i in range(retries):
        ok = input(prompt).strip()
        if ok in ('Y', 'y'):
            return True
        if ok in ('N', 'n'):
            return False
        print(complaint)
    return False

ask_yn(input())
