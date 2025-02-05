#Rating concepts  using if elif else insted of switch case

def order_rating():
    rating = int(input("Enter 1-5 Rating:"))
    rating_list = ["Bad","Below Avg","Avg","Good","Excellent"]
        
    feedback_dict={}
    if rating == 1:
        
        feedback = input("Enter Feedback:")
        feedback_dict['feedback']=feedback
        print("{} *".format(rating_list[0]))
        print(feedback_dict)

    elif rating == 2:
        feedback = input("Enter Feedback:")
        feedback_dict['feedback']=feedback
        print("{} * *".format(rating_list[1]))
        print(feedback_dict)

    elif rating == 3:
        print("{} * * *".format(rating_list[2]))

    elif rating == 4:
        print("{} * * * *".format(rating_list[3]))

    elif rating == 5:
        print("{} * * * * *".format(rating_list[4]))

    else:
        print("{}invalid option".format(rating))

    
    
    


