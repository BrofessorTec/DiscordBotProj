from random import choice, randint

deathrollStarted = None

def set_deathrollStarted():
    global deathrollStarted
    deathrollStarted = True

deathrollCont = 0
deathrollContHolder = 0

def get_deathrollStarted():
    return deathrollStarted


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    global deathrollCont
    global deathrollContHolder

    print(lowered)

    if lowered == '':
        return 'Well hello!'
    elif lowered[0] != '/':
        return
    elif lowered == '/help':
        return '/roll to roll a d20\n/roll [Size] to roll a die of the given size'
    elif '/roll ' in lowered:
        loweredTrim: int = int(lowered[6:])
        print(loweredTrim)
        loweredTrimNum = str(randint(1,loweredTrim))
        print(loweredTrimNum)
        return f'You rolled a {loweredTrimNum} out of {str(loweredTrim)}!'
    elif '/roll' in lowered:
        return f'You rolled a {randint(1,20)} out of 20!'
    elif '/deathroll ' in lowered:
        deathrollTrim: int = int(lowered[11:])
        print(deathrollTrim)
        deathrollTrimNum = str(randint(1,deathrollTrim))
        print(deathrollTrimNum)
        if (deathrollTrimNum == 1):
            deathrollTrimNum = 0
            return f'You rolled a 1! You lose Deathroll!'
        deathrollCont = deathrollTrim

        return f'You rolled a {deathrollTrimNum} out of {deathrollTrim}! Use "/deathroll" to continue!'
    elif '/deathroll' in lowered:
        if deathrollCont == 0:
            deathrollCont = 999
            print(deathrollCont)
        if deathrollContHolder == 0:
            deathrollTrimNum = str(randint(1,deathrollCont))
            print(deathrollTrimNum)
            deathrollContHolder = deathrollTrimNum
            if (deathrollTrimNum == 1):
                deathrollTrimNum = 0
                return f'You rolled a 1! You lose Deathroll!'
            return f'You rolled a {deathrollTrimNum} out of {deathrollCont}! Use "/deathroll" to continue!'
        else:
            deathrollTrimNum = str(randint(1,deathrollCont))
            print(deathrollTrimNum)
            deathrollContHolder = deathrollTrimNum
            if (deathrollTrimNum == 1):
                deathrollTrimNum = 0
                return f'You rolled a 1! You lose Deathroll!'
            return f'You rolled a {deathrollTrimNum} out of {deathrollCont}! Use "/deathroll" to continue!'            
    else:
        return f'There was an error.'
    


def deathroll():
    deathrollCont = 999
    deathrollTrimNum = str(randint(1,deathrollCont))
    print(deathrollTrimNum)
    if (deathrollTrimNum == 1):
        deathrollTrimNum = 0
        return f'You rolled a 1! You lose Deathroll!'
    return f'You rolled a {deathrollTrimNum} out of {deathrollCont}! Use "/deathroll" to continue!'

def deathroll(maxNum):
    deathrollCont = maxNum
    deathrollTrimNum = str(randint(1,deathrollCont))
    print(deathrollTrimNum)
    if (deathrollTrimNum == 1):
        deathrollTrimNum = 0
        return f'You rolled a 1! You lose Deathroll!'
    return f'You rolled a {deathrollTrimNum} out of {deathrollCont}! Use "/deathroll" to continue!'

