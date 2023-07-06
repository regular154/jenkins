pipeline {
    agent any
    parameters {
            string(name: 'TITLE', defaultValue: '', description: 'Title of GraphQL specification')
            string(name: 'DESCRIPTION', defaultValue: '', description: 'Description of GraphQL specification')
            stashedFile 'HTML'
            string(name: 'TAGS', defaultValue: '', description: 'Tag list comma separated')
            string(name: 'CATEGORIES', defaultValue: '', description: 'Category list comma separated')
            booleanParam(name: 'SANDBOX', defaultValue: false, description: 'Toggle this value to deploy to sandbox')
            booleanParam(name: 'DEVELOPMENT', defaultValue: false, description: 'Toggle this value to deploy to development')
            booleanParam(name: 'QA', defaultValue: false, description: 'Toggle this value to deploy to qa')
            booleanParam(name: 'STAGING', defaultValue: false, description: 'Toggle this value to deploy to staging')
            booleanParam(name: 'PRODUCTION', defaultValue: false, description: 'Toggle this value to deploy to production')
            string(name: 'WS', defaultValue: 'default', description: 'Please leave the default value here unless you know exactly what you are doing')
            hidden(name: 'HTML64', defaultValue: '', description: 'Hidden parameter for base64File value from testing pipeline')
        }
    stages {
        stage('print') {
            steps {
                script {
                    unstash 'HTML'
                    sh 'echo $HTML'
                }
            }
        }
    }
}