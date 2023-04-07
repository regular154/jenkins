pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                stash includes: 'test.html', name: 'HTML'
                unstash 'HTML'
                build job: 'test/main', parameters: [
                    stashedFile(name: 'HTML', file: [$class: 'org.apache.commons.fileupload.DefaultFileItem', repository: [$class: 'java.io.File', pathname: 'test.html']]),
                    string(name: 'TITLE', value: 'sample of title value')
                ]
            }
        }
    }
}