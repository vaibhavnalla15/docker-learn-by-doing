from flask import Flask
import redis
import os 

app = Flask(__name__)

# Connect to Redis service
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)


@app.route("/")
def home():

    # Increment visit count
    visits = redis_client.incr("visits")

    return f"""
    <h1>🐳 Flask + Redis Visitor Counter</h1>

    <p>
        Learning Docker to prepare for Amazon ECS and Amazon EKS deployments.
    </p>

    <h2>
        Visitor Count: {visits}
    </h2>
    """


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)