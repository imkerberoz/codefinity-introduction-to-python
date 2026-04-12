# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]
#Convert the list shelf1_update into a tuple named shelf1_update_tuple.
shelf1_update_tuple = tuple(shelf1_update)
#Concatenate
shelf1_concat = shelf1 + shelf1_update_tuple 
print("Updated Shelf #1:", shelf1_concat)
#Count "celery"
celery_count = shelf1_concat.count("celery")
celery_index = shelf1_concat.index("celery")

print("Number of Celery:", celery_count)
print("Celery Index:", celery_index)






