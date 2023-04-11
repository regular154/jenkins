pipeline {
    agent any
    parameters {
        stashedFile 'HTML'
        string(name: 'TITLE', defaultValue: '', description: 'Title of GraphQL specification')
        hidden(name: 'HTML64', defaultValue: '', description: 'Hidden parameter for base64File value from testing pipeline')
    }
    stages {
        stage('print file') {
            steps {
                script {
                    if (sh(script: 'if [ ! -z "$HTML64" ]; then return 1; else return 0; fi', returnStatus: true)) {
                        sh(script: 'echo "$HTML64" | base64 -d > HTML', returnStdout: true)
                        stash includes: 'HTML', name: 'HTML'
                    }
                }
                sh 'echo $TITLE'
                unstash 'HTML'
                sh 'cat HTML'
            }
        }
    }
}
