import os
import random
import time


'''
Nicole Torres
CS2302
Lab 1A
'''

def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2
    
    return random.random() / 2


def process_dir(path):

    dir_list, file_list = get_dirs_and_files(path)
    

    #print(dir_list, file_list)

    cat_list = []
    dog_list = []

    # Your code goes here
    #base case
    if len(dir_list) == 0:
        for image in file_list:
            if classify_pic(path + "/" + image) < 0.5:
                cat_list.append(path + "/" + image)
            else:
                dog_list.append(path + "/" + image)
        return cat_list, dog_list
    else:
        # add pics of subdirectories to main lists for this directory
        for dir in dir_list:
            cl, dl = process_dir(path + "/" + dir)  # list of cat/dog pics in subdirectories
            for cat_pic in cl:
                cat_list.append(cat_pic)
            for dog_pic in dl:
                dog_list.append(dog_pic)

        # add all pics in this directory to respective lists
        for image in file_list:
            if classify_pic(image) < 0.5:
                cat_list.append(path + "/" + image)
            else:
                dog_list.append(path + "/" + image)

    return cat_list, dog_list       
 
def main():
    
    start_time = (time.time())
    start_path = './' # current directory

    cl, dl = process_dir(start_path)

    end_time = (time.time())
    
    print(cl) #cat list images with path
    print(dl) #dog list images with path
    
   
    print('\n' "<<< %s seconds >>>" '\n' % (end_time - start_time))


main()

