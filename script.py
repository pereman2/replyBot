
#api_key = {api_key
#api_secret = {api_secret}
#token = {token_key}
#token_secret = {token_secret}




#robo = {link}
#robo_id = {link_id}

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token, token_secret)




def randomString(stringLength):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#reply to tweet
def send(msg):

    payload = "@twitter_account " + msg
    try:
        api = tweepy.API(auth)
        api.update_status(payload, robo_id)
    except tweepy.error.TweepError:
        print('nope')
        

while(True):
    size = random.randint(20,200)
    msg = randomString(size)
    send(msg)
    sleep = random.randint(100,150)
    time.sleep(sleep)
