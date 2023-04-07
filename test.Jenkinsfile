pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'echo $HOME'
                    build job: 'test/main', parameters: [
                        file(name: 'HTML', value: '@$HOME/test.html')
                    ]
                }
            }
        }
    }
}
