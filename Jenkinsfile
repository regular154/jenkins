pipeline {
    agent any
    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }
    stages {
        stage('build') {
            agent { 
                docker { 
                    image 'python:3.10.7-alpine' 
                } 
            }
            steps {
                sh 'python --version'
                sh 'echo Hello'
                echo "Database engine is ${DB_ENGINE}"
                echo "DISABLE_AUTH is ${DISABLE_AUTH}"
                sh 'printenv'
            }
        }
    }
    stages {
        stage('deploy') {
            agent { 
                docker { 
                    image 'siroshtan154/spectaql' 
                } 
            }
            steps {
                sh 'node --version'
                sh 'spectaql --version'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
