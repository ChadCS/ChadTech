whichChar=modallogic__possible
if event.key in whichChar.keys and whichChar.keys.issubset(keys):
	charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
	charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
	charray.charen[curChar-1][2].append(whichChar)

whichChar=modallogic__necessary
if event.key in whichChar.keys and whichChar.keys.issubset(keys):
	charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
	charray.charen[curChar-1][2].pop(len(charray.charen[curChar-1][2])-1)
	charray.charen[curChar-1][2].append(whichChar)