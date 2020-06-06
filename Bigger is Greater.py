from collections import deque


def biggerIsGreater(w):
    stack = deque()
    n = len(w)
    stack.append(-1)

    for i in range(n-2,-1,-1):
        if w[i]>= w[stack[-1]]:
            stack.append(i)
        else:
            pivot = i
            break
    else:
        return 'no answer'

    ans = list(w)
    for i in range(len(stack)):
        if ans[pivot]<ans[stack[i]]:
            ans[pivot], ans[stack[i]] = ans[stack[i]], ans[pivot]
            ans = ans[:pivot+1] + list(reversed(ans[pivot+1:]))
            return ''.join(ans)



if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)