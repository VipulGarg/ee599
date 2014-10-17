import twitter

api = twitter.Api(consumer_key='vX4zFZ2O5EvB2dvVmHKIrZX9f',
                      consumer_secret='wuh6s2tU5PCbr9XYv1s9gIb6WnykUbnuEbDSpQ9cia919NvOor',
                      access_token_key='328006955-eX4tQxmAl67Eau2EJvH11shUZzoo8Z06qKMcHgmZ',
                      access_token_secret='P2zpEcnRXjLq65Xe3aEgoOhBKJW5rxQzgAl7hU1A3YmHW')

map_followerListScreenName={}
map_followerListName={}

currCount = 1
my_followers = api.GetFollowers()
for follower in my_followers:
    map_followerListScreenName[follower.screen_name] = currCount
    map_followerListName[currCount] = follower.name
    currCount = currCount + 1

i=0
map_followerConnected={}
for follower in my_followers:
    i=i+1
    sub_followers = api.GetFollowers(screen_name=follower.screen_name)
    for sub_follower in sub_followers:
        if sub_follower.screen_name in map_followerListScreenName:
            if sub_follower.screen_name in map_followerConnected:
                map_followerConnected[sub_follower.screen_name].append(map_followerListScreenName[sub_follower.screen_name])
            else:
                map_followerConnected[sub_follower.screen_name] = [map_followerListScreenName[sub_follower.screen_name]]
        
