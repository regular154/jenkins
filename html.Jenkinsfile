pipeline {
    agent any
    parameters {
        stashedFile 'HTML'
        string(name: 'TITLE', defaultValue: '', description: 'Title of GraphQL specification')
        hidden(name: 'HTML64', defaultValue: 'asdasdasd', description: 'Hidden parameter for base64File')
    }
    stages {
        stage('print file') {
            steps {
//                 script {
//                     if (sh(script: 'if test -f "$HTML64"; then return 1; fi', returnStdout: true)) {
//                         unstash 'HTML'
//                     } else {
//                         sh 'echo $HTML64 >> HTML'
//                     }
//                 }
                sh 'echo ${HTML64}'
                unstash 'HTML'
                sh 'cat HTML'
                sh 'echo $TITLE'
            }
        }
    }
}
