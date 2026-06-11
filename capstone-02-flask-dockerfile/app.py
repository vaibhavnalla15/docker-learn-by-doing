# Import Flask framework
from flask import Flask

# Create Flask application instance
app = Flask(__name__)


# Home Route
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title> Docker Journey</title>

        <style>
            body {
                background-color: #0f172a;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 40px;
            }

            .container {
                max-width: 800px;
                margin: auto;
            }

            h1 {
                color: #38bdf8;
            }

            h2 {
                color: #22c55e;
            }

            .card {
                background-color: #1e293b;
                padding: 20px;
                margin: 20px 0;
                border-radius: 12px;
            }

            ul {
                list-style: none;
                padding: 0;
            }

            li {
                padding: 8px;
            }

            .footer {
                margin-top: 40px;
                color: #94a3b8;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>🐳 Capstone 02 - Flask Docker App</h1>

            <h2>🚀 Version 3 Released</h2>

            <div class="card">
                <h3>About Me</h3>

                <p>
                    Hi, I'm learning Docker through real-world projects
                    to prepare for deploying containerized applications on
                    Amazon ECS and Amazon EKS.
                </p>
            </div>

            <div class="card">
                <h3>Skills in Progress</h3>

                <ul>
                    <li>✅ Docker Fundamentals</li>
                    <li>✅ Building Docker Images</li>
                    <li>✅ Writing Dockerfiles</li>
                    <li>✅ Containerizing Python Applications</li>
                    <li>🔄 Docker Compose</li>
                    <li>🔄 Amazon ECR</li>
                    <li>🔄 Amazon ECS</li>
                    <li>🔄 Amazon EKS</li>
                </ul>
            </div>

            <div class="card">
                <h3>Deployment Workflow</h3>

                <p>
                    Flask App
                    → Docker Image
                    → Docker Container
                    → Amazon ECR
                    → Amazon ECS / Amazon EKS
                </p>
            </div>

            <div class="footer">
                <p>
                    Version 2 • First Python Docker Application Successfully Updated 🎉
                </p>
            </div>

        </div>

    </body>
    </html>
    """


# Run the Flask application
if __name__ == "__main__":

    # host="0.0.0.0" allows access from outside the container
    # port=5000 is the Flask application port
    app.run(host="0.0.0.0", port=5000)