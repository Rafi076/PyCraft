import re
pattern = r"[A-Z]+yclone" # to find any word with [a-z]yclone 
text = ''' 
In meteorology, a cyclone (/ˈsaɪ.kloʊn/) is a large air mass that rotates around a strong center of low atmospheric pressure, counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Cyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4] The largest low-pressure systems are polar vortices and extratropical cyclones of the largest scale (the synoptic scale). Warm-core cyclones such as tropical cyclones and subtropical cyclones also lie within the synoptic scale.[5] Mesocyclones, tornadoes,Dyclone and dust devils lie within the smaller mesoscale.[6]
'''

matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]: match.span()[1]])