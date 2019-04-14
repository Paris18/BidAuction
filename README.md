# BidAuction
bidding and Auction


#advertisement is the property which we are auctining
#admin will controll this property
#it will contains all adslot with open for bid or not column
we can interact with below api's

get : http://127.0.0.1:8000/ads/advertisement/

get corresponding ad

POST:insert new Slot(primary key manually taking we can also automate it)
PUT:Update Ad data
DELETE:delete ad(actually we are invalidating data

# BIDDING App

#model contains bidding data(including adid(forienkey),bid_price)

http://127.0.0.1:8000/ads/action/

get:get bid

POST: put my bid if bid price is less than max bid_price it will reject with 204

DELETE:delete my bid

Update:Update my bid


# Auction App

#model contains bidding data(including adid(forienkey),bid_price)

http://127.0.0.1:8000/auction/action/

get:get all bid

http://127.0.0.1:8000/auction/adproperty/

get: all available bid property

http://127.0.0.1:8000/auction/getauction/

post:finalise bid property











