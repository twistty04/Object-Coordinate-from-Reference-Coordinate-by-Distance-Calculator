import math

ref_lat = 50.434108001
ref_long = -104.663650374

obj_lat = input("Y-axis distance?")
obj_long = input("X-axis distance?")

final_lat = ((float(obj_lat)/101)/3600) + ref_lat

print(f"The object's latitude is: {final_lat}")

long_ref = ((math.cos(final_lat * math.pi/180.0 ) * 24902.0/360.0) * 5280)/3600

final_long = ((float(obj_long)/long_ref)/3600) + ref_long

print(f"The object's longitude is: {final_long}")