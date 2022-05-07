my_dict={ "Book1": {"Name":"Think and Grow Rich I", "Author":"Napoleon Hill","Published year":1973},
          "Book2": {"Name":"Think and Grow Rich II", "Author":"Napoleon Hill","Published year":1943},
          "Book3": {"Name":"Think and Grow Rich III", "Author":"Napoleon Hill","Published year":1953},
          "Book4": {"Name":"Think and Grow Rich IV", "Author":"Napoleon Hill","Published year":1963},
          "Book5": {"Name":"Think and Grow Rich V", "Author":"Napoleon Hill","Published year":1933},
          "Book6": {"Name":"Think and Grow Rich VI", "Author":"Napoleon Hill","Published year":1923},
          "Book7": {"Name":"Think and Grow Rich VII", "Author":"Napoleon Hill","Published year":1913},
          "Book8": {"Name":"Think and Grow Rich VIII", "Author":"Napoleon Hill","Published year":1972},
          "Book9": {"Name":"Think and Grow Rich IX", "Author":"Napoleon Hill","Published year":1978},
          "Book10": {"Name":"Think and Grow Rich X", "Author":"Napoleon Hill","Published year":1979}}

print("The original dictionary: " + str(my_dict) + "\n")

result= sorted(my_dict.items(),key = lambda x:x[1]['Published year'])

print("The sorted Dictionary by Published year is :" + str(result))