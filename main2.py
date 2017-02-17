print("**************************************************************************")
print("**************************  --RSA Algorithm--  ***************************")
print("***********************  Implemented by Batch-6  *************************")
print("************************  Under the guidance of  *************************")
print("*************************  Dr. T.Venugopal Sir  **************************") #no data type needed for declaration in python
print("*****************  Asst.Prof & Head of the Department  *******************")
print("******************  Computer Science and Engineering  ********************")
print("*************  JNTUH College of Engineering , Sulthanpur  ****************")
print("**************************************************************************")
print("* Let BOB has a message and wants to send to ALICE.")
print("* ALICE generates her Public and Private keys as below.")
p= input("* Any Random prime number p: ")  #takes p input
q= input("* Any Random prime number q: ") #takes q input
print("*\tCompute n = p * q")
n = p * q     #multiplies p and q and stores in n
print("*\tn = {0} * {1} = {2}".format(p,q,n))
print("*\tCompute the totient: phi(n)=({0}-1)({1}-1) ".format(p,q))
t=((p-1)*(q-1))   #performes p-1 and q-1 calculation and saves in t
print("*\tTotient:phi(n) = {0}".format(t))
print("*\tchoose e > 1 co-prime to {0}".format(t))
e= input("* Enter the co-prime number e: ")  #takes coprime input e
print("*\tChoose d to satisy de = 1 (mod phi(n))")
print("*\tHence d({0}) = 1 (mod({1}))".format(e,t))

z=e  #assign e value to z
m=t  #assign t value to m


def egcd(a, b):
    x, lastX = 0, 1    #x,lastx,y,lasty varaiables are declared with values as python does not support direct declaration
    y, lastY = 1, 0
    while (b != 0):     #checks while condition
        q = a // b      #the division of the operand where result is the quotient      ex: 9//2 = 4
        a, b = b, a % b  # a value is equals to b     and     b value is equals to a%b
        x, lastX = lastX - q * x, x      
        y, lastY = lastY - q * y, y

    return (lastX)      #returns lastx value to egcd(a,b) function  (lastx is the d value)


var = egcd(z,m)    #egcd(z,m)  is calling the function with values given in 23,24 line  #stores function returned value in var variable
f= var        #assign var value in f
if f < 0:      #checks if condition

    f+t       #if f  is in negative values   then to over come this... negative value is added tototient to get postive value
    print("*\tBy using Extended Euclidean algorithm, d = {0}".format(f+t))
    print("**************************************************************************")
    print("*\tALICE Public key=(n={0},e={1}) ".format(n,e)) 
    print("*\tALICE Private key=(n={0},d={1}) ".format(n,f+t))
    print("**************************************************************************")
    print("* ALICE hides her private key and sends her public key to BOB. ")
    print("* Received ALICE's public key to BOB : (n={0},e={1})".format(n,e))
    print("* Now BOB encrypts the message using ALICE public key.")
    num= input("* Enter the BOB's message (message < n): ")    #takes input to encrypt number
    pov = e           
    var = pow(num, pov)   #pow is a inbuilt python function which calculates power of given numbers 
    var%n          #performs modulus operations
    print("*\tc = {0} ^ {1} mod {2} = {3} ".format(num,e,n,(var%n)))
    print("* Encrypted BOB's message: {0}".format(var%n))
    print("* Now BOB sends the encrypted message to ALICE.")
    print("**************************************************************************")
    print("* ALICE receives the encrypted message from the BOB: {0}".format(var%n))
    print("* Now ALICE decrypts the received encrypted message using her private key.")
    print("* Now ALICE see's her secretly hidden private key : (n={0},d={1})".format(n,f+t))
    mun= input("* Enter the received message to decrypt: ")   #takes the cipher value
    a = mun
    b = f+t
    var = (pow(a, b))
    var%n
    print("*\tm = {0} ^ {1} mod {2} = {3} ".format(mun,f+t,n,(var%n)))
    print("* Decrypted BOB's message in hands of ALICE = {0}".format(var%n))
    print("**************************************************************************")

else:           #for negative value issue in eculidean algorithm... if and and else are written with changing (f+t) and (f) 
    print("*\tBy using Extended Euclidean algorithm, d = {0}".format(f))
    print("**************************************************************************")
    print("*\tALICE Public key=(n={0},e={1}) ".format(n,e)) 
    print("*\tALICE Private key=(n={0},d={1}) ".format(n,f))
    print("**************************************************************************")
    print("* ALICE hides her private key and sends her public key to BOB. ")
    print("* Received ALICE's public key to BOB : (n={0},e={1})".format(n,e))
    print("* Now BOB encrypts the message using ALICE public key.")
    num= input("* Enter the BOB's message (message < n): ")    #takes input to encrypt number
    pov = e           
    var = pow(num, pov)   #pow is a inbuilt python function which calculates power of given numbers 
    var%n          #performs modulus operations
    print("*\tc = {0} ^ {1} mod {2} = {3} ".format(num,e,n,(var%n)))
    print("* Encrypted BOB's message: {0}".format(var%n))
    print("* Now BOB sends the encrypted message to ALICE.")
    print("**************************************************************************")
    print("* ALICE receives the encrypted message from the BOB: {0}".format(var%n))
    print("* Now ALICE decrypts the received encrypted message using her private key.")
    print("* Now ALICE see's her secretly hidden private key : (n={0},d={1})".format(n,f))
    mun= input("* Enter the received message to decrypt: ")   #takes the cipher value
    a = mun
    b = f
    var = (pow(a, b))
    var%n
    print("*\tm = {0} ^ {1} mod {2} = {3} ".format(mun,f,n,(var%n)))
    print("* Decrypted BOB's message in hands of ALICE = {0}".format(var%n))
    print("**************************************************************************")

