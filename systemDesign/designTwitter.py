database = {}
session = {}


class UserProfile:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_tweets={}
        # self.myhome=Home()
        self.following=Following()

        print("Welcome To My Profile:-")
        print("-----------------------------------")
        self.username=User(first_name,last_name)
        self.tweets=Tweets()


    def get_user_info(self):
        self.username.user_show()
        print("-----------------------------------")

    def store_user_tweets(self,tweets):
        self.tweets.user_tweets1(tweets)
        return self.tweets.store_tweets(self.first_name,tweets)

    def show_user_tweets(self):
        return self.tweets.show_tweets()


    def user_followers(self,follower):
        return  self.following.user_followers(self.first_name,follower)



    # def show_home_page_tweets_by_me(self):

    # def homePage_show_tweets(self):




class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name = last_name
        self.users_list={}


    def user_show(self):
        print("USER NAME :- ",self.first_name,"",self.last_name)


class Register:
    def __init__(self, fn,ln, email):
        self.user = User(fn,ln, email)
        database[email] = self.user




class Tweets:
    def __init__(self):
        print("Here are my Tweets:-")
        print("--------------------------------------")
        self.user_tweets={}

    def user_tweets1(self, tweets):
        print("I Tweeted:-", tweets)

    def store_tweets(self,first_name,tweets):
        if first_name not in self.user_tweets:
            self.user_tweets[first_name]=[tweets]
        else:
            self.user_tweets[first_name].append(tweets)
        return  self.user_tweets

    def show_tweets(self):
        return (self.user_tweets)
#
# class Home:
#     def __init__(self):
#         print("below is my homepage")
#
#     # def display_tweets(self):
#     #     my_profile.

class Following:

    def __init__(self):
        print("I Follow These People")
        self.user_following={}

    def user_followers(self,name,follower):
        if name not in self.user_following:
            self.user_following[name]=[follower]
        else:
            self.user_following[name].append(follower)
        return self.user_following




my_profile=UserProfile("Elsy","Fernandes")
my_profile.get_user_info()
my_profile.store_user_tweets("tweet 1")
print(my_profile.store_user_tweets("tweet 2"))

my_profile.user_followers("Monkey1")
my_profile.user_followers("Monkey2")
print(my_profile.user_followers("Monkey3"))


#
# myprofile2=UserProfile("Aaron","Pinto")
# myprofile2.get_user_info()
# myprofile2.store_user_tweets("tweet 1")
# myprofile2.store_user_tweets("tweet 2")




