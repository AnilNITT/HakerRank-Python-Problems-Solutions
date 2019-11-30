def count_substring(string, sub_string):
//Write code here
    result=sum(string[i:].startswith(sub_string) for i in range(len(string)))
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
