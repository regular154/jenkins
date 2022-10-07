pipeline {
    agent any
    parameters {
        string(name: 'INTROSPECTION_URL', defaultValue: '', description: 'Graphql server introspection url')
        string(name: 'TITLE', defaultValue: '', description: 'Title')
        string(name: 'DESCRIPTION', defaultValue: '', description: 'Description')
    }
    stages {
        stage('get spec') {
            agent { 
                docker { 
                    image 'python:3.10.7-alpine' 
                } 
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install -r get_spec/requirements.txt'
                    sh 'python get_spec/get_spec.py --url ${INTROSPECTION_URL} --title ${TITLE} --description ${DESCRIPTION}'
                    stash includes: 'spec.json', name: 'spec'
                    stash includes: 'config_modified.yml', name: 'config'
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
                unstash 'config'
                sh 'npx spectaql config_modified.yml'
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
