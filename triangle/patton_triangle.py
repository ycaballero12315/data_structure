def patton_triangle_generate(n):
    for i in range(n):
        yield " "*(n-i-1)+'*'*(2*i+1)
        

for elm in patton_triangle_generate(8):
    print(elm)

        
