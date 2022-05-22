def split(s, delimiters):
    result = []
    item = ""

    for ch in s:
        if ch not in delimiters:
            item += ch
        else:
            # s[i] is a delimiter. Send item to result
            if len(item) > 0:
                result.append(item)
                item = ""

    # The last item
    if len(item) > 0:
        result.append(item)
        item = ""

    return result

def main():
    s = input("Enter a string: ")
    delimiters = input("Enter delimiters: ")
  
    items = split(s, delimiters)
  
    for e in items:
        print(e)

main()
