pipeline {
    agent any  // Runs on your Jenkins node directly

    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Pull your project from Git
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python -m pip install --upgrade pip
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
                fi
                '''
            }
        }

        stage('Stop Existing App') {
            steps {
                sh '''
                # Kill any running Flask app on port 5000
                PID=$(lsof -t -i:5000)
                if [ ! -z "$PID" ]; then
                    kill -9 $PID
                fi
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                export FLASK_APP=app.py
                nohup flask run --host=0.0.0.0 --port=5000 > flask.log 2>&1 &
                echo "Flask app started on port 5000"
                '''
            }
        }
    }

    post {
        success {
            echo 'Flask app deployed successfully!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
