class User:

    def __init__(self,fn,ln,email):
        self.fn=fn
        self.ln=ln
        self.email=email
        self.tweets=[]
        self.follow=[]
        self.follower=[]

    def get_firstName(self):
        return self.fn

    def get_lastName(self):
        return self.ln

    def get_email(self):
        return self.email

    def add_tweets(self,tweet):
        self.tweets.append(tweet)

    def display_user_tweets(self):
        return self.tweets

    def add_following(self,follow):
        self.follow.append(follow)

    def display_following(self):
        return (self.follow)

    def add_follower(self, follower):
        self.follower.append(follower)

    def display_follower(self):
        return (self.follower)



class Tweet:

    def __init__(self, message):
        self.message = message

    def get_tweets(self):
        print(self.message)


# class Tweets:
#     def __init__(self, message):
#         self.tweets = []
#
#     def get_tweets(self):
#         print(self.message)


class Following:
    def __init__(self,follow):
        self.follow=follow

    def get_following(self):
        print (self.follow)


class Follower:
    def __init__(self,follower):
        self.follower=follower

    def get_follower(self):
        print (self.follower)


class Twitter:

    def __init__(self):
        self.database = {}
        self.session = {}

    # User Registration to self.database

    def register(self, fn, ln, email):
        user_name=User(fn, ln, email)
        if email not in self.database:
            self.database[email]=user_name
            print("Registered Successfully!!!!!!!!")
        else:
            print("You are registered already!!!")
        # print(self.database)
        return self.database

    # User login fetches from the database

    def login(self, email):
        if email not in self.database:
            print("Please Register to Login")
        else:
            self.session = self.database[email]
        print("-------------------")
        print("Login Sucessfull")
        print(self.session)


    # User tweets are stored in the database

    def tweet(self, message):
        my_tweets = Tweet(message)
        email=self.session.get_email()
        self.database[email].add_tweets(my_tweets)


    # show user tweets

    def show_tweets(self):
        email=self.session.get_email()
        user_tweets=self.database[email].display_user_tweets()
        for i in user_tweets:
            i.get_tweets()



    def timeline(self):
        pass

    def logout(self):
        pass

    def show_followers(self):
        pass

    def follow(self, user):
        following=Following(user)
        email=self.session.get_email()
        self.database[email].add_following(following)

    def show_follow(self):
        email=self.session.get_email()
        follow=self.database[email].display_following()

        for i in follow:
            i.get_following()


    def followers(self,user):
        followers = Follower(user)
        email = self.session.get_email()
        self.database[email].add_follower(followers)

    def show_followers(self):
        email = self.session.get_email()
        follow = self.database[email].display_follower()

        for i in follow:
            i.get_follower()


    def user_profile(self):
        print("*************************************")
        print("Welcome to my profile!!!!")
        email=self.session.get_email()
        fn=self.session.get_firstName()
        ln=self.session.get_lastName()
        print(fn +" "+ ln +" "+ email)


        print("*********** Here are my tweets ***********")

        email = self.session.get_email()
        user_tweets = self.database[email].display_user_tweets()
        for i in user_tweets:
            i.get_tweets()

        print("**************** Here are the people following me*********")

        email = self.session.get_email()
        follower = self.database[email].display_follower()

        for j in follower:
            j.get_follower()


        print("********************I an following these people **************")

        email = self.session.get_email()
        follow = self.database[email].display_following()

        for i in follow:
            i.get_following()



    def print_database(self):
        print(self.database)


#--------------------------------Twittere insrance-------------------------------#

twitter = Twitter()
twitter.register("Aaron", "Pinto", "abc@g.com")
twitter.login("abc@g.com")

#--------------------------------My tweets---------------------------------------#

twitter.tweet("Hi How are ou")
twitter.tweet("Aaron is an idiot")


# ------------------------------- Add peoplr i am following----------------------#
twitter.follow("Aaron")
twitter.follow("Kothi")


#---------------------------------My followers----------------------------------#

twitter.followers("pinky")
twitter.followers("ponky")


#---------------------------------Display user profile-----------------------------#


twitter.user_profile()

# twitter.show_follow()
# twitter.print_database()

# twitter.user_profile()
# twitter.timeline()
# print(twitter.register("Elsy", "Fernandes", "abcd@g.com"))


