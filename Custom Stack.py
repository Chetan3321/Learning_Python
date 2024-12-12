glassStack = list() #crea

def isEmpty(glassStack):
    if len(glassStack) == 0:
        return True
    else:
        return False
    
def opPush(glassStack,element):
    glassStack.append(element)
    
def size(glassStack):
    retun len(glassStack)
    
def top(glassStack);
if isEmpty(glassStack):
    print('Stck is empty')
    return None
else:
    x = len(glassStack)
    element = glassStack[x-1]
    return element

def opPop(glassStack):
    if isEmnpty(glassStack):
        print('underflow')
        return None
    else:
        return(glassStack.pop())
    
def display(glassStack):
    x = len(glassStack)
    print("Current Elements in the stack are: ")
    for i in range(x-1,-1,-1):
        print(glassStack[i])

