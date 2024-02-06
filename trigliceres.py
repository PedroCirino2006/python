j = input ("Você esta em jejum s/n?" )
t = input("Trigliceres? ")
t = int(t) # converter pra int
if j == 's':
    if t > 150:
       print("está alto")
    else:
       print("está normal!")
else:
    if t > 175:
       print("está alto")
    else:       
       print("está normal!")

