import math
#TEST ERROR - I had my elif and else swapped with defining the new midpoint
#work in progress, commentys ;ater
def search(list_of_lists, query):
    search_start_index = 0
    search_end_index = len(list_of_lists)-1

    while search_start_index <= search_end_index:
        midpoint = int((search_start_index + search_end_index) / 2)
        print(midpoint)
        if math.isclose(list_of_lists[midpoint][0], query, rel_tol=0.01):
            return list_of_lists[midpoint][1]

        elif list_of_lists[midpoint][0] < query:
            search_start_index = midpoint + 1

        else:
            search_end_index = midpoint - 1

    return -1
imageresults = [(86.36783854166666, '6.7/9.png'), (85.59104938271605, '6.7/10.png'), (68.10368441358024, '6.7/8.png'), (60.08607951005003, '6.7/7.png'), (57.01145833333333, '6.7/6.png'), (39.59722860205176, '6.7/3.png'), (39.32125, '6.7/1.png'), (33.154761904761905, '6.7/5.png'), (23.513551401869158, '6.7/4.png'), (20.169370229007633, '6.7/2.png')]
print("=====")
print(imageresults)
print("=====")

print(search(imageresults, 39.32125))
print(search(imageresults, 6.7/2))