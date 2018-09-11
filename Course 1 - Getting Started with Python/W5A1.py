#Calculate gross pay based on hrs & rate
hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

OT_hrs = 40.00 #normal hour threshold
OT_rate = rate * 1.5

#calculate pay for normal hours under threshold
if hrs <= OT_hrs:
  pay = hrs * rate
#calculate OT + normal pay
else:
  pay = ((hrs - OT_hrs) * OT_rate) + (OT_hrs * rate)

print("Pay:", pay)
