print("**************************************************************************")
print("**************************  --RSA Algorithm--  ***************************")
print("***********************  Implemented by Batch-6  *************************")
print("************************  Under the guidance of  *************************")
print("*************************  Dr. T.Venugopal Sir  **************************") #no data type needed for declaration in python
print("*****************  Asst.Prof & Head of the Department  *******************")
print("******************  Computer Science and Engineering  ********************")
print("*************  JNTUH College of Engineering , Sulthanpur  ****************")
print("**************************************************************************")
print("**************************************************************************")
print("****************** Text Encryption using ASCII values ********************")
print("**************************************************************************")
p= input("* Enter the Public Key n value: ")
q= input("* Enter the Public Key e value: ")
print("*\tPublic key (n={0},e={1}) <<Shared on the server for EVERYONE >> ".format(p,q))

message = raw_input("* Enter plain text : ")

print"* Cipher text <<Data going to be SENT >> :"
for ch in message:
   rav = ord(ch)
   var = pow(rav, q) 
   print(var%p),
print "\n"

print("******************************************************************************************************")
print("**************************  Decryption to text using ASCII values ************************************")
print("******************************************************************************************************")
message = raw_input("* Enter Cipher text << RECEIVED data >> :")
n = input("* Enter the Private Key n value: ")
b = input("* Enter the Private Key d value: ")
print("*\tPrivate key (n={0},d={1})   <<Shared between TARGETS only like Whatsapp Security Code >> ".format(n,b))


decodedMessage = ""

for item in message.split():
  item= int(item)
  b =int(b)
  n =int(n)
  var = pow(item, b)
  t = var%n
  decodedMessage += str(unichr(t))

print "* Plaintext :", decodedMessage
print("*******************************************************************************************************")






