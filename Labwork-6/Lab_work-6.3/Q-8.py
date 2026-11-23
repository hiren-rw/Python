# Q.8: Temperature conversion with errors and assertions

class HighTemoretureError(Exception):
    pass

def convert_temp(c):

    if type(c) not in(int,float):
        raise TypeError("Tempreture must be a Number!")

    assert -273 <= c <= 10000, "Tempreture out of range (-273 to 10000)!"

    if c > 1000:
        raise HighTemoretureError("Tempreture exceeds 1000 C !")

    f = (c *9/5) +32
    print("Fahrenhit : ",f)

convert_temp(816)