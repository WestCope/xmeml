from xmeml import VideoSequence

v1 = VideoSequence(file='examples/Conecta Test XML.xml')
v2 = VideoSequence(file='examples/Mark P XML.xml')
#print len(v1.track_items)

clip1 = v1.clip(1000, 4000, units='frames')
clip2 = v2.clip(300, 500, units='seconds')

xmldom1,dumb_uuid = v1.clips2dom([clip1])
xmldom2,dumb_uuid = v2.clips2dom([clip2])

#print xmldom1.toprettyxml() #probably won't work in Final Cut Pro
#print xmldom2.toxml()
