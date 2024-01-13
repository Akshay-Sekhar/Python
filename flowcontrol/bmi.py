weight_inkg=83
height_incm=180
height_inmetre=height_incm/100
bmi=(weight_inkg)/(height_inmetre**2)
if(bmi<19):
    print("Undeer weight")
elif((bmi>20)and(bmi<24)):
    print("Normal")
elif((bmi>25)and(bmi<29)):
    print("Over weight")
elif(bmi>=30):
    print("Obesity")            
