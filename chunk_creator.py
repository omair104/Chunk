import os
import math
from shutil import copyfile
#import numpy
#from numpy import  chararray




'''
#Creating the input files
a=["%04d" % x for x in range(1000)]
for i in a:
    file_name = "img_" + str(i) + ".jpg"
    copyfile(os.path.join(input_location, "img_0001.jpg"), os.path.join(output_location, file_name))
'''


def main(input_location, output_location, images_per_chunk, overlap_size):
    #input_location= "C:\Temp\images\input"
    #output_location = "C:\Temp\images\output"
    #images_per_chunk= 100
    #overlap_size= 20
    
    list_of_files = os.listdir(input_location) 
    number_of_files = len(list_of_files)
    #print(number_of_files)
    
    number_of_chunks = math.ceil(number_of_files / (images_per_chunk - overlap_size))
    #number_of_chunks = int(number_of_files / (images_per_chunk - overlap_size)) + (number_of_files % (images_per_chunk - overlap_size) >0)
    print(number_of_chunks)
    
    
    
    #empty_lists = [[] for i in range(number_of_chunks)]
    #print(empty_lists)
    #print(empty_lists[0])
    
    #a = chararray((number_of_chunks,20), itemsize=12)
    #print(a)
    foo='placeholder.jpg'
    chunk_array = [[foo for i in range(images_per_chunk)] for j in range(number_of_chunks)]
    
    
    n=0
    for j in range(number_of_chunks):
        for i in range(images_per_chunk):
            chunk_array[j][i] = list_of_files[n]
            n=n+1
            if n == number_of_files:
                break
            
        n = n - overlap_size
        
    #print(chunk_array[0])
    for i in range(number_of_chunks):
        chunk_ouput_location = os.path.join(output_location, "Chunk" +str(i))
        if not os.path.exists(chunk_ouput_location):
            os.makedirs(chunk_ouput_location)
        for j in range(images_per_chunk):
        #print(chunk_array[0][i])
            if chunk_array[i][j] != "placeholder.jpg":
                #print(chunk_array[i][j])
                copyfile(os.path.join(input_location, chunk_array[i][j]), os.path.join(chunk_ouput_location, chunk_array[i][j]))
                

if __name__ == '__main__':
    main()