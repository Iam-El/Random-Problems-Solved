class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        count = 1
        j = 1
        stack = [chars[0]]
        for i in range(1, len(chars)):
            if stack and stack[-1] == chars[i]:
                stack.append(chars[i])
                count = count + 1
                print(count)
            else:
                for p in range(0, count):
                    print
                    stack.pop()
                stack.append(chars[i])
            print(stack)






