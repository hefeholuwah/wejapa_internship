reservoir_vol = 4.445e8

rainfall = 5e6

#decrement by 10%

rainfall*= 0.9

#adding rainfall to reservoir_volume

reservoir_vol = (rainfall + reservoir_vol)

#increasing new reservoir volume by 5%

reservoir_vol *= 1.05

#decreasing new_reserv_vol by 5%

reservoir_vol *= 0.95

#subtracting 2.5e5 cubic meters

new_vol_val = (reservoir_vol - 2.5e5)

print (new_vol_val)
