pipeline {
    agent any
    parameters {
        stashedFile 'HTML'
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
