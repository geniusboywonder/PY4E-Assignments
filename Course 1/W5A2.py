#Prompt for a score between 0.0 and 1.0
sco = input("Enter Score:")
try:
    score = float(sco)
except:
  print("Please enter a numerical value between 0.0 and 1.0")
  quit()

# score must be between 0.0 and 1.0

if score > 1.0:
    print("Please enter a numerical value between 0.0 and 1.0")
elif score >= 0.9:
    print("Grade: A for Score of", score)
elif score >= 0.8:
    print("Grade: B for Score of", score)
elif score >= 0.7:
    print("Grade: C for Score of", score)
elif score >= 0.6:
    print("Grade: D for Score of", score)
elif score < 0.6:
    print("Grade: F for Score of", score)
elif score < 0.0:
    print("Please enter a numerical value between 0.0 and 1.0")
