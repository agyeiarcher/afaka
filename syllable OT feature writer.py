syllables=[]
for i in Glyphs.font.glyphs: #Glyphs specific - would be good to include the FontParts equiv.
	if i.color==3:
		listname=i.name.encode("utf-8")
		syllables.append(listname)

for i in syllables:
	print("sub "+(" ".join(i))+" by " + i+";")