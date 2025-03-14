
#| وزن (گرم) | قطر (cm) | نوع میوه (Y) |
#|-----------|----------|--------------|
#| 150       | 7        | 1 (سیب)      |
#| 130       | 6        | 1 (سیب)      |
#| 170       | 8        | 1 (سیب)      |
#| 180       | 9        | -1 (پرتقال)  |
#| 200       | 10       | -1 (پرتقال)  |
#| 210       | 11       | -1 (پرتقال)  |
 #Suppose we want to build a perceptron model that can ...
 # determine whether a fruit is an apple...
 #  or an orange based on its weight and diameter.

x1 = [150,130,170,180,200,210] # vazn  first input
x2 = [7,6,8,9,10,11]           #Qotr   secound input
yb = [1,1,1,-1,-1,-1]

#intial weight
w1=0.4
w2=0.5

def sign(x):    #sign function
    if x > 0:
        r = 1
    if x <= 0:
        r = -1
    return r

def correct_w1(x1,y,yb,w1):     #First weight correction
        a = 0.1  #Farz kardim
        w1 = w1 + (a*((yb - y)*x1))
        return w1

def correct_w2(x2,y,yb,w2):     #Secound weight correction
        a = 0.1 #Farz kardim
        w2 = w2 + (a*((yb - y)*x2))
        return w2

# inner multipol w & x
y = []
w=[(0.4,0.5)]
for i in range (0,6): #This part make first Data for start training
    s = (w1*x1[i])+(w2*x2[i])
    y.append(sign(s))
for j in range (0,6): #This part start tarinng model with weight correction
    while y[j] != yb[j]:
        w1 = correct_w1(x1[j],y[j],yb[j],w1)
        w2= correct_w2(x2[j],y[j],yb[j],w2)
        s = (w1*x1[j])+(w2*x2[j])
        y[j] = (sign(s))
        if y[j] == yb[j]:
            w.append([w1,w2])
## test data (with new data test our model)
x1t = 160 #test first input
x2t = 7.5 #test secound input
w1t = w[-1][-2] #tained weight
w2t = w[-1][-1] # trianed weight
s = (w1t*x1t)+(w2t*x2t)
if sign(s) == 1 :
    print("SIIIB")
if sign(s) == -1:
    print("PORTEGHAL")