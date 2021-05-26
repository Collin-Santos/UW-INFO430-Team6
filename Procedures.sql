CREATE PROCEDURE [dbo].[insert_user]
	@ID NVARCHAR(100),
	@Name NVARCHAR(100),
	@Handle NVARCHAR(100),
	@Link NVARCHAR(200),
	@Location NVARCHAR(200),
	@Date DATE,
	@Description NVARCHAR(2000),
	@Verified TINYINT,
	@Followers INT,
	@Following INT,
	@TweetCount INT,
	@Listed INT
AS
BEGIN
	BEGIN TRY
		BEGIN TRAN T1
			INSERT INTO [dbo].[Users] (id, name, twitter_handle, link, location, creation_date, description, verified)
			VALUES (@ID, @Name, @Handle, @Link, @Location, @Date, @Description, @Verified);
			INSERT INTO [dbo].[User_Metrics] (user_id, follower_count, following_count, tweet_count, listed_count)
			VALUES (@ID, @Followers, @Following, @TweetCount, @Listed);
		COMMIT TRAN T1
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN T1
	END CATCH
END;

GO
CREATE PROCEDURE [dbo].[insert_tweet]
	@ID NVARCHAR(100),
	@UserID NVARCHAR(100),
	@Content NVARCHAR(1000),
	@Date DATE,
	@Retweet INT,
	@Reply INT,
	@Like INT,
	@Quote INT
AS
BEGIN
	BEGIN TRY
		BEGIN TRAN T1
			INSERT INTO [dbo].[Tweets] (id, user_id, content, creation_date)
			VALUES (@ID, @UserID, @Content, @Date);
			INSERT INTO [dbo].[Tweets_Metrics] (tweet_id, retweet_count, reply_count, like_count, quote_count)
			VALUES (@ID, @Retweet, @Reply, @Like, @Quote);
		COMMIT TRAN T1
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN T1
	END CATCH
END;