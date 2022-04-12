print([x for x in range(5)])
vec=[[1,2,3],[4,5,6],[7,8,9]]
flatvec=[num for elem in vec for num in elem]
print(flatvec)

myStringList = [
' Hello how are you?',
'I\'m good ',
' I\'m good too ']
myStrings = [s.strip() for s in myStringList]
print(myStrings)
