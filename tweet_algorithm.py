import json

class Tweet:
    def __init__(self, name, id):
        self._tweet_dict = {}
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @name.setter
    def name(self, name):
        self._name = name
        self._tweet_dict['name'] = self.name

    @id.setter
    def id(self, id):
        self._id = id
        self._tweet_dict['id'] = self.id

    @property
    def tweet_dict(self):
        return self._tweet_dict


class Tweets ():
    def __init__(self, tweets: int):
        self.tweets = tweets
        self.__tweet_pool = []

    def create_tweet(self, name, id):
        if self.__tweet_pool.__len__ () < self.tweets:
            tweet = Tweet (name, id)
            self.__tweet_pool.append (tweet)
        else:
            print ('cannot create tweet, saturation limit has exceeded.')

    def __iter__(self):
        return iter (self.__tweet_pool)


class TweetContainer:
    def __init__(self):
        self.size = None
        self.__container = []

    def can_i_retry(self):
        retry = False
        given_value = input('do you want to retry? y/n: ')
        if given_value.lower() == 'y':
            retry = True
        return retry

    def create_tweet_containers(self):
        while True:
            try:
                value = input ('number of tweet containers: ')
                self.size = int (value)
            except Exception as e:
                print('Expect only integers, given: ', value)
                attemt_valid = self.can_i_retry()
                if attemt_valid:
                    continue
                break
            else:
                break
        for index in range (0, self.size):
            print ('Provide valid information, tweet container: {}'.format (index + 1))
            self.create_tweets ()

    def create_tweets(self):
        if self.__container.__len__ () < self.size:
            while True:
                try:
                    value = input ('tweet number: ')
                    number_of_tweets = int (value)
                except Exception as e:
                    print ('Expect only integers, given: ', value)
                    attemt_valid = self.can_i_retry ()
                    if attemt_valid:
                        continue
                    break
                else:
                    break
            tweets = Tweets (number_of_tweets)
            print ('Please provide the tweet information -')
            for index in range (number_of_tweets):
                name = input ('tweet name: ')
                id = input ('tweet id: ')
                tweets.create_tweet (name, id)
            self.__container.append (tweets)
        else:
            print ('cannot create tweet container, saturation limit has exceeded.')

    def __iter__(self):
        return iter (self.__container)


class TweetSolution (object):
    def __init__(self):
        self.tweet_cate = TweetContainer ()
        self.tweet_cat_pool = []
        self.result_pool = None

    def create_tweets(self):
        self.tweet_cate.create_tweet_containers ()

    def get_all_tweet_and_store(self):
        count = 1
        for tweets in self.tweet_cate:
            # print ('tweet category number: {}'.format (count))
            tweet_pool = []
            for tweet in tweets:
                tweet_pool.append (tweet.tweet_dict)
            self.tweet_cat_pool.append (tweet_pool)
            count += 1

    def create_tweet_and_store_local_process(self):
        self.create_tweets ()
        self.get_all_tweet_and_store ()
        self.result_pool = self.max_tweets_tweeted_by_user_in_each_slot ()

    def max_tweets_tweeted_by_user_in_each_slot(self):
        tweet_user_info_pool = []
        for tweet_cat in self.tweet_cat_pool:
            names = [tweet['name'] for tweet in tweet_cat]
            tweet_count_by_name = {name: names.count (name) for name in names}
            tweet_count_by_name_sorted = [{k[0]: tweet_count_by_name[k[0]]} for k in
                                          sorted(tweet_count_by_name.items())]
            filtered_top_users = self.filter_max_tweeted_users (tweet_count_by_name_sorted)
            filtered_top_users_sorted = sorted (filtered_top_users, key=lambda k: next (iter (k.values ())))
            tweet_user_info_pool.append (filtered_top_users_sorted)
        return tweet_user_info_pool

    def filter_max_tweeted_users(self, tweet_count_by_name_sorted):
        max_tweet = next (iter (tweet_count_by_name_sorted[0].values ()))
        filtered_value = list (filter (lambda d: next (iter (d.values ())) == max_tweet, tweet_count_by_name_sorted))
        return filtered_value

    def print_result(self):
        for result_cat in self.result_pool:
            for user_information in result_cat:
                print('{} {}'.format(next (iter (user_information.keys ())), next (iter (user_information.values ()))))


if __name__ == '__main__':
    tweet_solution = TweetSolution ()
    tweet_solution.create_tweet_and_store_local_process ()
    tweet_solution.print_result ()
