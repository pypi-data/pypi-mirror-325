from TweetCatcherPy import TweetCatcher, CreateTaskArgs, PingRegex, PingKeywords
import asyncio

api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3aG9wVXNlcklkIjoidXNlcl9QbDhWdHFnbldRSG1HIiwidHlwZSI6ImFwaS1rZXkiLCJpYXQiOjE3Mzg2Mjk0NjB9.-pUj8iHV59lrqZ6Y-rm-COu2BDAEaZUQK_sMWY7X2ts"
tweet_catcher = TweetCatcher(api_token)

async def get_tasks():
    tasks = await tweet_catcher.get_tasks()
    print("Tasks:", tasks)

if __name__ == "__main__":
    asyncio.run(get_tasks())