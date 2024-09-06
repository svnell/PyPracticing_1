g#num = int(input())
#shift = int(input())
#facts = [True] * num
#step = 1
#index = 0
#counter = num
#print(facts[2])
#while counter - 1:
#    if facts[index % num] and step < shift:
#
#        print('number survived:', index % num + 1, f'(index: {index % num}), step: {step}')
#        step += 1
#        index += 1
#    elif not facts[index % num] and step <= shift:
#        print('dead number appeared', index % num + 1, f'step = {step}')
#        index += 1
#    else:
#        step = 1
#        facts[index % num] = False
#        print('number killed', index % num + 1)
#
#        counter -= 1
#        index += 1

def recurs(n, k):
    return 0 if n == 0 else (recurs(n - 1, k) + k) % n


n = int(input())
k = int(input())
print(recurs(n, k) + 1)