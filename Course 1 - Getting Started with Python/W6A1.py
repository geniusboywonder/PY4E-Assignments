#Function to calculate gross pay based on hrs & rate
def computepay(h,r):
    OT_hrs = 40.00
    OT_rate = r * 1.5

    #calculate pay for normal hours under threshold
    if h <= OT_hrs:
        pay = h * r
    #calculate OT + normal pay
    else:
        pay = ((h - OT_hrs) * OT_rate) + (OT_hrs * r)

    return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

print(computepay(hrs,rate))
