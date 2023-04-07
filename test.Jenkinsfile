pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'echo $HOME'
                    sh 'ls'
                    sh 'cat $HOME/test.html'
                    build job: 'test/main', parameters: [
                        file(name: 'HTML', file: '@$HOME/test.html')
                    ]
                }
            }
        }
    }
}
