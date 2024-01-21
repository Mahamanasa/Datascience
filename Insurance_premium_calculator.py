#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def insurance_premium_calc(gender,dob,smoker):
    if gender == "MALE" :
        if dob > 1990 and dob < 2000:
            if smoker == "YES":
                print("Your annual premium is Rs.35000")
            else:
                    smoker == "NO"
                    premium = 35000 - (35000 * 10/100)
                    print ("Your annual premium is Rs.  ",premium)
        elif dob >1970 and dob < 1990:
            if smoker == 'YES':
                print("Your annual premium is Rs.40000")
            else:
                    smoker =="NO"
                    premium = 40000-(40000 * 5/100)
                    print ("Your annual premium is Rs.  ",premium)
        else:
            print("Not elgible for insurance")
    elif gender == "FEMALE":
            if dob > 1990 and dob <2000:
                if smoker == "YES":
                    print("Your annual premium is Rs.30000")
                else:
                    smoker =='NO'
                    premium = 30000 - (30000 * 10/100)
                    print("Your annual premium is Rs.",premium)
            elif dob > 1970 and dob < 1990:
                if smoker == "YES":
                    print("Your annual premium is Rs.35000")
                else:
                        smoker =="NO"
                        premium = 35000 - (35000 * 5/100)
                        print("Your annual premium is Rs. ",premium)
            else:
                print("Not eligible for insurance")
    else:
            print("Not eligible for Insurance")

