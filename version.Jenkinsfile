pipeline {
    agent any
    stages {
        stage("Verify checkout") {
            steps {
                skipCi()
            }
        }
        stage('test') {
            steps {
                script {
                    update_version()
                }
            }
        }
    }
}

def update_version(def gitUsername = "jenkinspush") {
    def isRelease = false
    def newVersion = getIncrementedVersion("patch", true)

    writeVersionToFile(newVersion)

    sh 'git config user.email siroshtan.home@gmail.com'
    sh """
        git config user.name regular154
        git add gradle.properties
        git commit -m \"[ci skip] New version: ${newVersion}\"
    """

    if (isRelease) {
        sh "git tag ${newVersion}"
    }

    sh "git push origin HEAD:${env.BRANCH_NAME} --tags"
}

def getIncrementedVersion(def mode = "patch", def snapshot = true) {
    def currentVersion = "${getProjectVersion(false)}"
    def versionList  = currentVersion.split(/\./).toList().collect {it -> it.toInteger()}

    def major = versionList[0]
    def minor = versionList[1]
    def patch = versionList[2]

    switch (mode) {
        case "major":
            major += 1
            minor = 0
            patch = 0
            break
        case "minor":
            minor += 1
            patch = 0
            break
        case "patch":
            patch += 1
            break
    }

    return newVersion = [major, minor, patch].join(".").concat(snapshot ? "-SNAPSHOT" : "")
}

def writeVersionToFile(def version) {
    sh "sed -i \"/version=/ s/=.*/=${version}/\" gradle.properties"
}

def skipCi(def number = 1) {
    String[] keyWords = ['ci skip', 'skip ci']
    def statusCodeList = []

    keyWords.each { keyWord ->
        def statusCode = null
        if (number == "all") {
            statusCode = sh script: "git log --oneline --all | grep \'${keyWord}\'", returnStatus: true
        } else {
            statusCode = sh script: "git log --oneline -n ${number} | grep \'${keyWord}\'", returnStatus: true
        }
        statusCodeList.add(statusCode)
    }

    if (statusCodeList.contains(0)) {
        currentBuild.result = "ABORTED"
        error("Found CI skip condition, skipping build...")
    }
}

def getProjectVersion(def keepSnapshot = true) {
    def version = sh (
            script: "cat gradle.properties | grep \"version\" | cut -d'=' -f2",
            returnStdout: true
    ).trim()

    return keepSnapshot ? version : "${version}".replace("-SNAPSHOT", "")
}