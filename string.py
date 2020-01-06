text = "X-DSPAM-Confidence:    0.8475"

where = text.find('0')
flt = float(text[where:])
print(flt)
