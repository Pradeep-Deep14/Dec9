nums=list(range(1,21)) #include 20

filtered_elements = list(filter(lambda x:(x%2==0),nums))
print(filtered_elements)