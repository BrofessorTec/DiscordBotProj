from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
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
    else:
        return f'There was an error.'