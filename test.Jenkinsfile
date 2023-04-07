pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                stash allowEmpty: false, includes: 'test.html', name: 'HTML'
                unstash 'HTML'
                build job: 'test/main', parameters: [
                    stashedFile(name: 'HTML', file: HTML),
                    string(name: 'TITLE', value: 'sample of title value')
                ]
            }
        }
    }
}