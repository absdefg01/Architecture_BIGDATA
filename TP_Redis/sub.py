import redis

#Make a Redis client subscribe to new items in a specific category
r = redis.StrictRedis(host='localhost',port=6379, db=0)
client = r.pubsub()
client.subscribe('IPad')
client.subscribe('Bike')
client.subscribe('Aquarium')

while True:
    message = client.get_message()
    if message:
        print "Subscriber: %s" % message


