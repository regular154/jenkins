pipeline {
    agent any
    parameters {
        stashedFile 'HTML'
        string(name: 'TITLE', defaultValue: '', description: 'Title of GraphQL specification')
        base64File(name: 'HTML64', defaultValue: '', description: 'Title of GraphQL specification')
        hidden(name: 'HTML64', defaultValue: '', description: 'Hidden parameter for base64File')
    }
    stages {
        stage('print file') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    unstash 'HTML'
                    sh 'cat HTML'
                    sh 'echo $TITLE'
                }
            }
        }
    }
}
