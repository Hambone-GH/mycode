#!/usr/bin/env python
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
proto.append('dns') #yeet
protoa.append('dns') #yoink
print(proto)
proto2 = [22, 80,443,53] #wat
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)
