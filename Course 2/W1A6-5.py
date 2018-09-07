text = "X-DSPAM-Confidence:    0.8475";
start = text.find(":")
end = len(text)
iresult = text[start+1:end]
print(float((iresult)))
