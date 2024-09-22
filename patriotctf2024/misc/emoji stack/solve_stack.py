
with open('./input.txt', 'r') as f:
    inp = f.read().strip()
# inp = "👍🔁47💬👉👍🔁68💬👉👍🔁20💬" #test
inp=list(inp)
# print(inp)

stack = [0]
pointer = 0
curr_op = "👉"
#wttffff
prev_op = None
i=0

def right():
    global pointer
    pointer += 1
    if pointer == len(stack):
        stack.append(0)

def left():
    global pointer
    pointer -= 1

def increment():
    stack[pointer] += 1

def decrement():
    stack[pointer] -= 1

def print_char():
    print(chr(stack[pointer]), end='')


while i < len(inp):
    if inp[i] == '👉':
        prev_op = curr_op
        curr_op = "👉"
        right()
    elif inp[i] == '👈':
        prev_op = curr_op
        curr_op = "👈"
        left()
    elif inp[i] == '👍':
        prev_op = curr_op
        curr_op = "👍"
        increment()
    elif inp[i] == '👎':
        prev_op = curr_op
        curr_op = "👎"
        decrement()
    elif inp[i] == '💬':
        prev_op = curr_op
        curr_op = "💬"
        print_char()
    elif inp[i] == '🔁':
        prev_op = curr_op
        curr_op = "🔁"
        number = int(inp[i+1]+inp[i+2],16)
        for j in range(number):
            if prev_op == "👉":
                right()
            elif prev_op == "👈":
                left()
            elif prev_op == "👍":
                increment()
            elif prev_op == "👎":
                decrement()
            elif prev_op == "💬":
                print_char()
    i+=1
