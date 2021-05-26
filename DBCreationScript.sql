CREATE TABLE Users (
	id NVARCHAR(100) PRIMARY KEY,
	name NVARCHAR(100),
	twitter_handle NVARCHAR(100),
	link NVARCHAR(200),
	location NVARCHAR(200),
	creation_date DATE,
	description NVARCHAR(2000),
	verified TINYINT
);

CREATE TABLE User_Metrics (
	user_id NVARCHAR(100),
	follower_count int,
	following_count int,
	tweet_count int,
	listed_count int,
	FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Tweets (
	id NVARCHAR(100) PRIMARY KEY,
	user_id NVARCHAR(100),
	content NVARCHAR(1000),
	creation_date DATE,
	FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Tweets_Metrics (
	tweet_id NVARCHAR(100),
	retweet_count int,
	reply_count int,
	like_count int,
	quote_count int,
	FOREIGN KEY (tweet_id) REFERENCES Tweets(id)
);