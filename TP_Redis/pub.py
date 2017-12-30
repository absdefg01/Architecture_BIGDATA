import redis
import time
r = redis.StrictRedis(host='localhost',port=6379, db=0)


# creation of a database of item on sale
r.hmset('IPad',{'name' : 'IPad 2', 'price' : 500, 'color' : 'Red'})
r.hmset('Bike',{'name' : 'OFO', 'price' : 300, 'color' : 'Black'})
r.hmset('Aquarium',{'name' : 'JIDI', 'price' : 20, 'color' : 'Blue'})


#Make items expire after a while
r.expire('IPad',10)
r.expire('Bike',10)
r.expire('Aquarium',10)


channel = r.pubsub()

#r.publish('',)


iPad = r.hgetall('IPad')
bike = r.hgetall('Bike')
aquarium = r.hgetall('Aquarium')


r.publish('IPad', iPad)
time.sleep(1)

r.publish('Bike', bike)
time.sleep(1)

r.publish('Aquarium', aquarium)
time.sleep(1)


'''
import redis
import time

r = redis.StrictRedis(host='localhost',port=6379, db=0)


# creation of a database of item on sale
r.lpush('IPad',[{'name' : 'IPad 1', 'price' : 500, 'color' : 'Red'},{'name' : 'IPad 2', 'price' : 600, 'color' : 'Black'},
				{'name' : 'IPad mini', 'price' : 300, 'color' : 'Red'}])
r.lpush('Bike',[{'name' : 'Bike 1', 'price' : 1500, 'color' : 'Red'},{'name' : 'Bike 2', 'price' : 1600, 'color' : 'Black'},
				{'name' : 'Bike 2', 'price' : 300, 'color' : 'Red'}])
r.lpush('Aquarium',[{'name' : 'Aquarium 1', 'price' : 1500, 'color' : 'Red'},{'name' : 'Aquarium 2', 'price' : 1600, 'color' : 'Black'},
					{'name' : 'Aquarium 3', 'price' : 300, 'color' : 'Red'}])

IPad_len = r.llen('IPad')
Bike_len = r.llen('Bike')
Aquarium_len = r.llen('Aquarium')


#Make items expire after a while
r.expire('IPad',10)
r.expire('Bike',10)
r.expire('Aquarium',10)


channel = r.pubsub()
IPad = r.lrange('IPad',1,-1)
Bike = r.lrange('IPad',1,-1)
Aquarium = r.lrange('IPad',1,-1)

r.publish('IPad',IPad)
time.sleep(1)

r.publish('Bike',Bike)
time.sleep(1)

r.publish('Aquarium',Aquarium)
time.sleep(1)
'''
