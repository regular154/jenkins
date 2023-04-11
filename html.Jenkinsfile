pipeline {
    agent any
    parameters {
        stashedFile 'HTML'
        string(name: 'TITLE', defaultValue: '', description: 'Title of GraphQL specification')
        hidden(name: 'HTML64', defaultValue: '', description: 'Hidden parameter for base64File')
    }
    stages {
        stage('print file') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    if ( sh 'if test -f "$HTML"; then return 1; fi') {
                        unstash 'HTML'
                    } else {
                        sh 'echo $HTML64 >> HTML'
                    }
                    sh 'cat HTML'
                    sh 'echo $TITLE'
                }
            }
        }
    }
}
