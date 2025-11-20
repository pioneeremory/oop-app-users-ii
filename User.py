# Add a method to your User class that allows for creating a new user post.
# Add any necessary instance properties to make step 1 work. What data structure should you use?
# Add a class variable that stores the posts from every user. What data structure should you use?
# Make sure that the the information stays in sync!
# Add a method that allows for deleting a post. Again, make sure that your information stays in sync.

class User:
    all_posts = {}
    # Each user has a dict = post title:post_content
    # Class variable is dict = user:post

    def __init__(self, name, email_address, dl_num):
        #make name unique in order to avoid user posts being overwritten, or consider using username or DL# in dict
        self.name = name
        self.email_address = email_address
        self.dl_num = dl_num 
    def __str__(self):
        return(f'The user name is {self.name}, and their email address is {self.email_address}. The DL# is {self.dl_num}')
    def user_post(self, author):
        self.author = author

        author = self.name
        content = input('Write a comment below: \n')

        #this method only support 1 post per user, otherwise a new post overwrites the existing one store as dict value
        User.all_posts.update({author:content})
        return('Your content has been submitted')
    def del_post(self, post):
        self.post = post

        post = str(input('Which user post would you like to delete? (username: )'))
        del(User.all_posts[post])
        return(f'The post by {User.name} was deleted!')

logan = User("Logan", "address@email.com", 123123123) 
print(logan)

notlogan = User("notlogan", "address2@email.com", 987987987)
print(notlogan)

print(User.user_post(logan, logan))
print(User.all_posts)

