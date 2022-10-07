pipeline {
    agent any
    stages {
        stage('get spec') {
            agent { 
                docker { 
                    image 'python:3.10.7-alpine' 
                } 
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    dir('get_spec') {
                        sh 'pip install -r requirements.txt'
                        sh 'python get_spec.py'
                        stash includes: 'spec.json', name: 'spec'
                    }
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
                sh 'npx spectaql config.yml'
                stash includes: 'public/**', name: 'content'
            }
        }
        stage('modify html') {
            agent { 
                docker { 
                    image 'python:3.10.7-alpine' 
                } 
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    dir('modify_html') {
                        unstash 'content'
                        sh 'pip install -r requirements.txt'
                        sh 'python modify_html.py'
                        stash includes: 'public/index.html', name: 'page'
                    }
                }                
            }
        }
        stage('push html to kong') {
            steps {
                unstash 'page'
                sh 'cp public/index.html index.html'
            }
        }
    }
}
