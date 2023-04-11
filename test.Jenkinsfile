pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                stash includes: 'test.html', name: 'HTML'
                build(job: 'test/main', parameters: [
                        string(name: 'TITLE', value: 'title example'),
                        stashedFile(name: 'HTML')
                    ]
                )
            }
        }
    }
}