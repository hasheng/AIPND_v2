<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Hashim Javed
# DATE CREATED: February 8, 2021                                 
# REVISED DATE: February 8, 2021
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

#Retrieve the filenmaes from folder pet_images/
# filename_list = listdir("pet_images/")

# Print 10 of the filenames from folder pet_images/
# print("\nPrints 10 filenames from folder pet_images/")
# for idx in range(0, 10, 1):
#     print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):

    
 
    in_files = listdir(image_dir)

    results_dic = dict()

    for i in range(len(in_files)):
        if in_files[i][0] ==".":
            continue
        word_list_pet_image = in_files[i].lower().split("_")
#            
        pet_name=""
                    
        for word in word_list_pet_image:
            if word.isalpha():
                pet_name += word + " "
        pet_name = pet_name.strip()
        
        if in_files[i] not in results_dic:
            results_dic[in_files[i]] = [pet_name]
              
        else:
            print("** Warning: Duplicate files exist in directory:", 
                     in_files[i])
                
    return results_dic


    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    return None
=======
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
#     print(in_files)
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()
#     # Determines number of items in dictionary
#     items_in_dic =len(results_dic)  
    
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
#     counter = 0
    for i in range(len(in_files)):
#        print(counter)
#        pet_name=""
#        pet_label=""
#        counter +=1
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't an pet image file
#        print(i)
#        print(in_files[0][0])
#        if in_files[i][0] != ".":
       if in_files[i].isalnum():    
           # Creates temporary label variable to hold pet label name extracted 
           pet_label=""

           # TODO: 2a. BELOW REPLACE pass with CODE that will process each 
           #          filename in the in_files list to extract the dog breed 
           #          name from the filename. Recall that each filename can be
           #          accessed by in_files[idx]. Be certain to place the 
           #          extracted dog breed name in the variable pet_label 
           #          that's created as an empty string ABOVE
           pet_label =in_files[i]
#            print(pet_label+str(i))
           # Sets string to lower case letters
           low_pet_image = pet_label.lower()
#            print(low_pet_image)
           # Splits lower case string by _ to break into words 
           word_list_pet_image = low_pet_image.split("_")
#            print(word_list_pet_image)
            
           # Create pet_name starting as empty string
           pet_name=""
#            print("1" + pet_name)
           # Loops to check if word in pet name is only
           # alphabetic characters - if true append word
           # to pet_name separated by trailing space 
           for word in word_list_pet_image:
                if word.isalpha():
                    pet_name += word + " "
#                     print("2" + pet_name)
#                 print("3" + pet_name)
#            print("4" + pet_name)
           # Strip off starting/trailing whitespace characters 
           pet_name = pet_name.strip()
#            print("5"+pet_name)
           
#             # Prints resulting pet_name
#            print("\nFilename=", pet_label, "   Label=", pet_name)
           
           
           # If filename doesn't already exist in dictionary add it and it's
           # pet label - otherwise print an error message because indicates 
           # duplicate files (filenames)
           
           
#            break
           for i in range(0, len(in_files), 1): 
                if in_files[i] not in results_dic:
                    results_dic[in_files[i]] = [pet_name]
              
                else:
                    print("** Warning: Duplicate files exist in directory:", 
                     in_files[i])
                
    return results_dic
#        print("\nFilename=", pet_label, "   Label=", pet_name)
#     print(len(in_files))
# print(pet_label)
#     print(pet_name)
#     print(len(results_dic))
#     print(counter)
    



# get_pet_labels("pet_images/")
>>>>>>> 6fb1b661fc7255bd1c92643a07cdb01b31ee7ff4
||||||| 6fb1b66
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Hashim Javed
# DATE CREATED: February 8, 2021                                 
# REVISED DATE: February 8, 2021
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

#Retrieve the filenmaes from folder pet_images/
# filename_list = listdir("pet_images/")

# Print 10 of the filenames from folder pet_images/
# print("\nPrints 10 filenames from folder pet_images/")
# for idx in range(0, 10, 1):
#     print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
#     print(in_files)
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()
#     # Determines number of items in dictionary
#     items_in_dic =len(results_dic)  
    
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
#     counter = 0
    for i in range(len(in_files)):
#        print(counter)
#        pet_name=""
#        pet_label=""
#        counter +=1
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't an pet image file
#        print(i)
#        print(in_files[0][0])
#        if in_files[i][0] != ".":
       if in_files[i].isalnum():    
           # Creates temporary label variable to hold pet label name extracted 
           pet_label=""

           # TODO: 2a. BELOW REPLACE pass with CODE that will process each 
           #          filename in the in_files list to extract the dog breed 
           #          name from the filename. Recall that each filename can be
           #          accessed by in_files[idx]. Be certain to place the 
           #          extracted dog breed name in the variable pet_label 
           #          that's created as an empty string ABOVE
           pet_label =in_files[i]
#            print(pet_label+str(i))
           # Sets string to lower case letters
           low_pet_image = pet_label.lower()
#            print(low_pet_image)
           # Splits lower case string by _ to break into words 
           word_list_pet_image = low_pet_image.split("_")
#            print(word_list_pet_image)
            
           # Create pet_name starting as empty string
           pet_name=""
#            print("1" + pet_name)
           # Loops to check if word in pet name is only
           # alphabetic characters - if true append word
           # to pet_name separated by trailing space 
           for word in word_list_pet_image:
                if word.isalpha():
                    pet_name += word + " "
#                     print("2" + pet_name)
#                 print("3" + pet_name)
#            print("4" + pet_name)
           # Strip off starting/trailing whitespace characters 
           pet_name = pet_name.strip()
#            print("5"+pet_name)
           
#             # Prints resulting pet_name
#            print("\nFilename=", pet_label, "   Label=", pet_name)
           
           
           # If filename doesn't already exist in dictionary add it and it's
           # pet label - otherwise print an error message because indicates 
           # duplicate files (filenames)
           
           
#            break
           for i in range(0, len(in_files), 1): 
                if in_files[i] not in results_dic:
                    results_dic[in_files[i]] = [pet_name]
              
                else:
                    print("** Warning: Duplicate files exist in directory:", 
                     in_files[i])
                
    return results_dic
#        print("\nFilename=", pet_label, "   Label=", pet_name)
#     print(len(in_files))
# print(pet_label)
#     print(pet_name)
#     print(len(results_dic))
#     print(counter)
    



# get_pet_labels("pet_images/")
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Hashim Javed
# DATE CREATED: February 8, 2021                                 
# REVISED DATE: February 8, 2021
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

#Retrieve the filenmaes from folder pet_images/
# filename_list = listdir("pet_images/")

# Print 10 of the filenames from folder pet_images/
# print("\nPrints 10 filenames from folder pet_images/")
# for idx in range(0, 10, 1):
#     print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
<<<<<<< HEAD
    
 
    in_files = listdir(image_dir)

    results_dic = dict()

    for i in range(len(in_files)):
        if in_files[i][0] ==".":
            continue
        word_list_pet_image = in_files[i].lower().split("_")
#            
        pet_name=""
                    
        for word in word_list_pet_image:
            if word.isalpha():
                pet_name += word + " "
        pet_name = pet_name.strip()
        
        if in_files[i] not in results_dic:
            results_dic[in_files[i]] = [pet_name]
              
        else:
            print("** Warning: Duplicate files exist in directory:", 
                     in_files[i])
                
    return results_dic

||||||| 624e7af
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    return None
=======
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
#     print(in_files)
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()
#     # Determines number of items in dictionary
#     items_in_dic =len(results_dic)  
    
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
#     counter = 0
    for i in range(len(in_files)):
#        print(counter)
#        pet_name=""
#        pet_label=""
#        counter +=1
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't an pet image file
#        print(i)
#        print(in_files[0][0])
#        if in_files[i][0] != ".":
       if in_files[i].isalnum():    
           # Creates temporary label variable to hold pet label name extracted 
           pet_label=""

           # TODO: 2a. BELOW REPLACE pass with CODE that will process each 
           #          filename in the in_files list to extract the dog breed 
           #          name from the filename. Recall that each filename can be
           #          accessed by in_files[idx]. Be certain to place the 
           #          extracted dog breed name in the variable pet_label 
           #          that's created as an empty string ABOVE
           pet_label =in_files[i]
#            print(pet_label+str(i))
           # Sets string to lower case letters
           low_pet_image = pet_label.lower()
#            print(low_pet_image)
           # Splits lower case string by _ to break into words 
           word_list_pet_image = low_pet_image.split("_")
#            print(word_list_pet_image)
            
           # Create pet_name starting as empty string
           pet_name=""
#            print("1" + pet_name)
           # Loops to check if word in pet name is only
           # alphabetic characters - if true append word
           # to pet_name separated by trailing space 
           for word in word_list_pet_image:
                if word.isalpha():
                    pet_name += word + " "
#                     print("2" + pet_name)
#                 print("3" + pet_name)
#            print("4" + pet_name)
           # Strip off starting/trailing whitespace characters 
           pet_name = pet_name.strip()
#            print("5"+pet_name)
           
#             # Prints resulting pet_name
#            print("\nFilename=", pet_label, "   Label=", pet_name)
           
           
           # If filename doesn't already exist in dictionary add it and it's
           # pet label - otherwise print an error message because indicates 
           # duplicate files (filenames)
           
           
#            break
           for i in range(0, len(in_files), 1): 
                if in_files[i] not in results_dic:
                    results_dic[in_files[i]] = [pet_name]
              
                else:
                    print("** Warning: Duplicate files exist in directory:", 
                     in_files[i])
                
    return results_dic
#        print("\nFilename=", pet_label, "   Label=", pet_name)
#     print(len(in_files))
# print(pet_label)
#     print(pet_name)
#     print(len(results_dic))
#     print(counter)
    



# get_pet_labels("pet_images/")
>>>>>>> 6fb1b661fc7255bd1c92643a07cdb01b31ee7ff4
>>>>>>> 8e7e496ddcfdc8dc43d4f87304334c53abe0b146
