import praw

def init(user, password, id, secret):
    print('Logging in to reddit, please wait... ')
    # Tries to log in to reddit
    try:
        reddit = praw.Reddit(client_id=id,
                         client_secret=secret,
                         password=password,
                         user_agent='web:' + id + ':' + version + ' (created by u/tazz4843)',
                         username=user)
    # If it fails, a friendly error is given to the user
    except OAuthException:
        print('\nFailed to log in!\nCheck the username and password!')
    print('Success!')
    # Checks the authorized user against the user that's supposed to be logged in, just in case
    authUser = reddit.user.me()
    if authUser != user:
        raise LoginException('Authorized user is unequal to the inputted user!')

def getNewMentions():
    mentions = reddit.inbox.mentions(limit=150)
    new = []
    mentioned = open('done.txt', 'r')
    done = mentioned.readlines()
    mentioned.close
    for item in mentions:
        for id in done:
            if id == item.id:
                doneId = id
                break
        if item.id == doneId:
            continue
        else:
            new.append(item)
            continue
    numNew = len(new)
    print('Got ' + str(numNew) + ' new mentions.')
    return new

def postComment(text, id):
    comment = reddit.comment(id=idToReplyTo)
    try:
        comment.reply(text)
    except prawcore.exceptions.Forbidden:
        print('Failed to reply to ' + idToReplyTo + '! Do you have permissions?')
