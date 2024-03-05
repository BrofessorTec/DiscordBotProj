# DiscordBotProj
 Discord Bot
 There has been a lot of python learning lessons such as the data typing issues we have had. In several cases, we have had to specifically type things so that the interpreter did not get confusing. A common one was when trying to use the randint function and we were getting issues about concatenating str and int together. <br>
 One simple issue to fix was ensuring all of the commands entered are lowercase so they can be interpreted correctly. We solved this by taking the inital input string and making it all lowercase before trying to execute any commands.<br>
 Some other issues were from learning how to use a global variable for the /deathroll command. These global commands allow us to start with an initial value and then overwrite it and remember it on the next execution of the game command.<br> 
 Melanie's potential project plans: 
  -to create a blacklist function that will temporarily block a user from posting to a channel if they're spamming messages
    -needs to be able to unblock users for now unless we add roles to the functionality where only certain users can reset the blacklist count of a user.<br>
  Had some issues using a dictionary in python. Searching for if a key existed or not caused a few errors. I attempted to check a ".contains" equivalent but it looks like the simplest way is to just check .get(key) = None for python and if that evaluates as true then it was not an existing key. <br>
