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


