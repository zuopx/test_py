
def func1():
    str1 = '\section'
    str2 = '\\section'
    str3 = '\\\\section'
    print(str1, str2, str3, sep='\n')

def func2():
    str1 = r'\section'
    str2 = r'\\section'
    str3 = r'\\\\section'
    print(str1, str2, str3, sep='\n')

if __name__ == "__main__":
    func1()
    func2()