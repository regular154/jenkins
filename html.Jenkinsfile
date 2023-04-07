pipeline {
    agent any
    parameters {
        stashedFile 'HTML'
        string(name: 'TITLE', defaultValue: '', description: 'Title of GraphQL specification')
    }
    stages {
        stage('print file') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    unstash 'HTML'
                    sh 'cat HTML'
                }
            }
        }
    }
}
