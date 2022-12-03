import cv2
import numpy as np
import os
import random
import smtplib


#VanetNodesTransactions.
#N1:Nodes A sends Node B a Message.
#N2:Nodes B sends Nodes C a Message.
#N3:Nodes C sends Node D a Message.

#We use SHA256 function for hashing.
#hash function 1.
#H1("aaa",N1,N2,N3)->03gf24
#H2(N4,N5,N6,"03gf24")->458kj1.....
#then  we concatenate them all.
#VanetNodesHash()
import hashlib
class VanetNodesHash:
    
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash= previous_block_hash
        self.transaction_list= transaction_list
        
        self.block_data= "-".join(transaction_list)+"-"+previous_block_hash
        self.block_hash= hashlib.sha256(self.block_data.encode()).hexdigest()



def fingerprintCheck():
    test_original = cv2.imread("TEST_1.tif")

    found=0

    for file in os.listdir("database"):

        fingerprint_database_image = cv2.imread("./database/"+file)
	    
        sift = cv2.SIFT_create()
	    
        keypoints_1, descriptors_1 = sift.detectAndCompute(test_original, None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)

        matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10),dict()).knnMatch(descriptors_1, descriptors_2, k=2)

        match_points = []

        for p, q in matches:
           if p.distance < 0.5*q.distance:
              match_points.append(p)

        keypoints = 0
        if len(keypoints_1) <= len(keypoints_2):
           keypoints = len(keypoints_1)            
        else:
           keypoints = len(keypoints_2)
           
        if (len(match_points) / keypoints)>0.5:
            found=1
            print("Fingerprint found!")
            print("Fingerprint ID: " + str(file)) 
            break

    if(found==0):
        return False
    else:
        return True

def otpVerify(id):
    otp=''.join([str(random.randint(0,9)) for i in range(4)])
    #we will create a server of gmail and also givethe port the passit throght tls security layer
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('anjalipathak016@gmail.com','mpocusxhbdpipgkq')
    msg= 'Your Verification OTP is '+ str(otp)
    server.sendmail('anjalipathak016@gmail.com',id,msg)
    server.quit()
    check=input("Enter the OTP sent to your email id: ")
    if(otp==check):
        return True
    else:
        return False
    #(221, b'2.0.0 closing connection g38sm14638668pgg.63 - gsmtp')
    


# Function to find the gcd
def gcd1(a, b):
      
    if b == 0:
        return a
    else:
        result = a % b
        return gcd1(b, result)
      
      
# Program to find Multiplicative inverse
def multiplicativeinverse(a, b):
      
    r1 = a
    r2 = b
    s1 = int(1)
    s2 = int(0)
    # t1 and t2 is always 0 and 1
    t1 = int(0)
    t2 = int(1)
      
    while r2 > 0:
        # quotient is q and the remainder is r  
        q = r1//r2
        r = r1-q * r2
        r1 = r2
        r2 = r
        s = s1-q * s2
        s1 = s2
        s2 = s
        t = t1-q * t2
        t1 = t2
        t2 = t
          
    if t1 < 0:
        t1 = t1 % a
    # r1 should be 1 (gcd) and t1 is the value of multiplicative inverse      
    return (r1, t1)

def hybridAlgo():
    # Enter two large prime numbers p and q
    p = input("Enter first prime no:")
    p= int(p)
    print(p)
    q = input("Enter second prime no:")
    q=int(q)
    print(q)
    n = p * q
    Pn = (p-1)*(q-1)
      
    # Generate encryption key using the RSA concept in range 1<e<Pn
    key = []
    # Check if no are coprime
    for i in range(2, Pn):
          
        gcd = gcd1(Pn, i)
          
        if gcd == 1:
            key.append(i)
      
      
    # Select an encryption key from the above list
    e = input("Enter the encryption key:")
    e=int(e)
    print(e)
      
    # Obtain inverse of encryption key in Z_Pn
    r, d = multiplicativeinverse(Pn, e)
    if r == 1:
        d = int(d)
        print("decryption key is: ", d)
          
    else:
        print("Multiplicative inverse doesn't exist ")
       
       
    # Enter the message to be sent
    M = input("Enter the Message: ")
    M = int(M)
    print(M)
      
    # Signature is created by A
    S = (M**d) % n
      
    # A sends M and S both to B
    # B generates message M1 using the signature S, A public key e and product n.
    M1 = (S**e) % n
      
    # If M = M1 only then B accepts the message sent by A.
      
    if M == M1:
        print("As M = M1, Accept the node  message sent by A allow it in the VANET")
    else:
        print("As M not equal to M1 then message is not send by A and invalid node ")
        



def blockchain():
    N1="Nodes A sends Node B a Message"
    N2="Nodes B sends Nodes C a Message"
    N3="Nodes C sends Node D a Message"
    N4="Nodes D sends Node E a Message"
    N5="Nodes E sends Nodes F a Message"
    N6="Nodes F sends Node G a Message"
    first_node = VanetNodesHash("intial Message",[N1,N2])

    print(first_node.block_data)
    print(first_node.block_hash)

    second_node = VanetNodesHash("intial Message ",[N3,N4])

    print(second_node.block_data)
    print(second_node.block_hash)

    third_node = VanetNodesHash("intial Message",[N5,N6])

    print(third_node.block_data)
    print(third_node.block_hash)
        



mailid=input("Enter your email id: ")
if(otpVerify(mailid)==True):
    print("Email id verified!")
else:
    print("The OTP entered is incorrect!!!")
    quit()

# A local fingerprint image is being used here to compare it with a number of images in a local database.
if(fingerprintCheck()==False):
    print("Fingerprint not found!!!")
    quit()

hybridAlgo()
blockchain()
