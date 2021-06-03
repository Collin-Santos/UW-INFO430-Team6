select * from users
select * from tweets_metrics
select * from user_metrics
select * from tweets

/*
select distinct ur.name, tw.creation_date,tw.content,tm.like_count, tm.quote_count, tm.reply_count, tm.retweet_count from users ur 
left join tweets tw on tw.user_id = ur.id
left join Tweets_Metrics tm on tm.tweet_id = tw.id 
*/

select distinct ur.name, tw.content,tw.creation_date, tm.like_count from users ur 
left join tweets tw on tw.user_id = ur.id
left join Tweets_Metrics tm on tm.tweet_id = tw.id 
where ur.name = 'adidas'
order by tm.like_count desc


/* top 200 like_count rank */


select top 200 ur.name, tw.content,tw.creation_date, tm.like_count,
rank() over(order by tm.like_count desc) as like_count_rank, datename(dw, tw.creation_date) as 'posting_date'
from users ur
left join tweets tw on tw.user_id = ur.id
left join Tweets_Metrics tm on tm.tweet_id = tw.id
group by ur.name, tw.content,tw.creation_date, tm.like_count
order by tm.like_count desc




