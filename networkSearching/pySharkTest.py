import pyshark 

capture = pyshark.LiveCapture(interface='en0')
capture.sniff(timeout=5)
print(capture)
print(len(capture))
print(capture[len(capture)-1])
for packet in capture.sniff_continuously(packet_count=len(capture)):
    print('Just arrived:', packet.ip.field_names)
    print('Packet length:', packet.length)