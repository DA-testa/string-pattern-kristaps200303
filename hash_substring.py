# Python 3

def obtain_input():
    choice = input()

    if choice[0] == 'I':
        keyword = input().strip()
        content = input().strip()

    elif choice[0] == 'F':
        with open('./tests/' + '06', 'r') as file:
            keyword = file.readline().strip()
            content = file.readline().strip()

    if 1 <= len(keyword) <= len(content) <= (5 * 10**5):
        return content, keyword
    else:
        exit()

def display_results(results):
    print(' '.join(map(str, results)))

def find_occurrences(target, data):
    temp_target = target
    index = 0
    shift = 0
    found_occurrences = []

    while shift < len(target):
        index = temp_target.find(data)
        if index < 0:
            break
        found_occurrences.append(index + shift)

        temp_target = temp_target[index + 1:]
        shift = shift + index + 1

    return found_occurrences

if __name__ == '__main__':
    display_results(find_occurrences(*obtain_input()))
