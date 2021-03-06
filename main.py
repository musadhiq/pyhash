import hashlib
option=int(input("""
Enter Your Option :

1 - md5
2 - sha1
3 - sha256
4 - sha384
5 - all
"""))
if option==1:
    text=input("Enter Your Text")
    hash_object = hashlib.md5(text.encode())
    md5_hash = hash_object.hexdigest()
    print("md5 hash : "+ md5_hash)
    print("   ")

elif option==2:
    text = input("Enter Your Text")
    hash_object = hashlib.sha1(text.encode())
    sha1_hash = hash_object.hexdigest()
    print("sha1 hash : " + sha1_hash)
    print("   ")

elif option==3:
    text=input("Enter Your Text :")
    hash_object=hashlib.sha256(text.encode())
    sha256 = hash_object.hexdigest()
    print("sha256 hash : " + sha256)
    print("    ")

elif option==4:
    text=input("enter your text")
    hash_object=hashlib.sha384(text.encode())
    sha384=hash_object.hexdigest()
    print("sha384 hash : "+sha384)
    print("  ")
else:
    text = input("Enter Your Text :")
    hash_object = hashlib.sha256(text.encode())
    sha256 = hash_object.hexdigest()
    print("sha256 hash : "+ sha256)
    hash_object = hashlib.md5(text.encode())
    md5_hash = hash_object.hexdigest()
    print("md5 hash  :" + md5_hash)
    hash_object = hashlib.sha1(text.encode())
    sha1_hash = hash_object.hexdigest()
    print("sha1 hash : " + sha1_hash)
    hash_object = hashlib.sha384(text.encode())
    sha384 = hash_object.hexdigest()
    print("sha384 :"+sha384)

print("Thank You!!..")