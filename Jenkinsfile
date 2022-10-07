pipeline {
    agent any
    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }
    stages {
        stage('get spec') {
            agent { 
                docker { 
                    image 'python:3.10.7-alpine' 
                } 
            }
            steps {
                dir('get_spec') {
                    sh 'pip install -r requirements.txt'
                    sh 'python get_spec.py'
                    stash includes: 'spec.json', name: 'spec'
                }
            }
        }
        stage('generate static content') {
            agent { 
                docker { 
                    image 'siroshtan154/spectaql' 
                } 
            }
            steps {
                unstash 'spec'
                dir('get_spec') {
                    sh "pwd"
                }
                sh 'npx spectaql config.yml'
                stash includes: 'public/*', name: 'content'
            }
        }
        stage('modify html') {
            agent { 
                docker { 
                    image 'python:3.10.7-alpine' 
                } 
            }
            steps {
                unstash 'content'
                sh 'python modify_html.py'
                stash includes: 'public/index.html', name: 'page'
            }
        }
        stage('push html to kong') {
            agent { 
                docker { 
                    image 'python:3.10.7-alpine' 
                } 
            }
            steps {
                unstash 'page'
                sh 'echo todo push'
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
