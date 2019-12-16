if __name__ == '__main__':
    s = input()
  # t=type(s)
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(method(c) for c in s))
