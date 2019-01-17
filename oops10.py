#Example 1:
#No Overriding in class B or class C

class A:
	pass
	def method(self):
		print("This method belongs to class A")
	
class B(A):
	pass

class C(A):
	pass
	
class D(B,C):
	pass

d= D()
d.method()


# Example 2:
# Overriding in class B and not in class C

# Example 1:
# No Overriding in class B or class C

class A:
    def method(self):
        print("This method belongs to class A")


class B(A):
    def method(self):
        print("This method belongs to class B")


class C(A):
    pass


class D(B, C):
    pass


d = D()
d.method()




# Example 3:
# No Overriding in class C and not class B

class A:
    def method(self):
        print("This method belongs to class A")


class B(A):
    pass


class C(A):
    def method(self):
        print("This method belongs to class C")


class D(B, C):
    pass


d = D()
d.method()






# Example 4:
# No Overriding in class C and not class B

class A:
    def method(self):
        print("This method belongs to class A")


class B(A):
    def method(self):
        print("This method belongs to class B")


class C(A):
    def method(self):
        print("This method belongs to class C")


class D(B,C):  #check the order of inheritance
    pass


d = D()
d.method()


#This is because of the sequencing of inheritance. If C is inherited first, the object will display value from class C.
