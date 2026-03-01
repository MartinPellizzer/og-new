from lib import zimage

while True:
    with open('zimage-prompt.txt') as f: prompt = f.read()
    zimage.image_create(
        f'test.jpg', prompt, width=768, height=768, seed=-1
    )
    input('>>')

'''
food
business
plant
italy
factory
warehouse
logistics
industry
automation
Stock Photos & Images
trade
logistic
production
beverages
industry 4.0
supply
automatic
pile
automatic warehouse
bergamo
Free stock photos
'''
