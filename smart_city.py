city = input("enter your city name :")
s_r  = int(input("enter the number of smart roads available in " + city + " :"))
m_h  = int(input("enter the number of multinational hospitals available in " + city + " :"))
a_i  = int(input("enter the average anuual income per head : "))
p    = int(input("enter the population of " + city + " in percentage :"))
l_r  = float(input("enter the literacy rate of " + city + " in percentage :"))
i_u  = float(input("enter the no of internet users in  " + city+ " in percentage :"))
c_r  = float(input("enter the crime rate of " + city + " in percentage:"))

if l_r>=70.0 and c_r<=30.0 and p>=8000000 and a_i>=400000 and i_u>=75.0 and m_h >=50 and s_r>=500:
    print(" yess..ur city passed all the criteria for smart city")
    print(city + " is a smart city")
else:
    print("no your city can't be a smart city")
    r = input("do you want to know the reason..?(yes/no): ")
    if r == "yes":
        if (p < 8000000):
            print(city + " must have population more than 8 million to be a smart city...")
        if (m_h < 50):
            print(city + " must have multinational hospitals more than 50 to be a smart city...")
        if (s_r < 500):
            print(city + " must have smart roads greater than 500 to be a smart city...")
        if (a_i < 400000):
            print(city + "'s annual income rate is less than required(4,00,000) to be a smart city...")
        if (l_r < 70.0):
           print(city + "'s literacy rate is less than 70% to be a smart city...")
        if (c_r > 30.0):
            print(city + "'s crime rate is greater than 30% to be a smart city...")
        if (i_u < 75.0):
            print(city + "'s must have internet users more than 75% to be a smart city...")
    else:
        print("Better luck next time...")






