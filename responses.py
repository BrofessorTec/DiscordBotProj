from random import choice, randint

deathrollCont = 0
deathrollContHolder = 0
deathrollCurrent = 0
authorRecordsForDeathroll = dict()  #this should really be a dictionary instead and one per game

def get_response(user_input: str, author: str) -> str:
    lowered: str = user_input.lower()
    global deathrollCont
    global deathrollContHolder
    global deathrollCurrent
    global authorRecordsForDeathroll
    print(author)
    print(authorRecordsForDeathroll.get(author))
    if authorRecordsForDeathroll.get(author) is None:  #contains is not valid, check for key another way
        authorRecordsForDeathroll[author] = 0  #initial value for each record should be zero

    print(authorRecordsForDeathroll[author])

    print(lowered)

    if lowered == '':
        return 'Well hello!'
    elif lowered[0] != '/':
        return
    elif len(lowered) > 300:
        return 'Woah there, that is too much info! Please use a simpler command.'
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
            authorRecordsForDeathroll[author] = authorRecordsForDeathroll[author] + 1 #keeping track of loses for this game instead
            return f'You rolled a 1! You lose Deathroll!'
        deathrollCont = deathrollTrimNum
        return f'You rolled a {deathrollTrimNum} out of {deathrollTrim}! Use "/deathroll" to continue!'
    elif '/deathroll' in lowered:
        if deathrollCont == 0:
            deathrollCont = 999
            print(deathrollCont) 
        deathrollCurrent = str(randint(1,int(deathrollCont)))
        deathrollContHolder = str(deathrollCont)
        deathrollCont = deathrollCurrent
        print(deathrollCurrent)
        if (int(deathrollCurrent) == int(1)):
            deathrollCont = 0
            print('loser')
            authorRecordsForDeathroll[author] = authorRecordsForDeathroll[author] + 1 #keeping track of loses for this game instead
            return f'You rolled a 1! You lose Deathroll!'
        return f'You rolled a {str(deathrollCurrent)} out of {str(deathrollContHolder)}! Use "/deathroll" to continue!'  
    elif '/myrecords' in lowered:
        recordStr = f"""{author}'s Records:"""
        recordStr += f"""\nDeathroll Loses: {authorRecordsForDeathroll[author]}"""
        recordStr += f"""\nOther records:"""
        return recordStr 
    elif lowered == '/help' or lowered[0] == '/':
        helpStr = """Help:
        /roll to roll a d20
        /roll [Size] to roll a die of the given size
        /deathroll [maxNum] to start a deathroll game with the given maximum. First to roll a 1 loses!
        /deathroll to continue a deathroll game or start a new one from 999"""
        # someone help me format this help string better lol. idk how to get it on multiple lines and still be one string
        return helpStr
    else:
        return f'There was an error.'
