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
                        stashedFile(name: 'HTML', file: [
                            $class: 'org.apache.commons.fileupload.disk.DiskFileItem'
                            repository: [
                                $class: 'java.io.File'
                                pathname: '/test.html'
                            ]
                        ])
                    ]
                }
            }
        }
    }
}
