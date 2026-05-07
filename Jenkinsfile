pipeline {

    agent any

    environment {

        PYTHON = "python"

        VENV = "venv"

        GRID = "true"
    }

    options {

        timestamps()

        ansiColor('xterm')
    }

    stages {

        stage('Checkout') {

            steps {

                git branch: 'main',
                url: 'https://github.com/chinnalasairaghavendra/ExpandNotesTesting'
            }
        }

        stage('Create Virtual Environment') {

            steps {

                bat """
                %PYTHON% -m venv %VENV%
                """
            }
        }

        stage('Install Dependencies') {

            steps {

                bat """
                %VENV%\\Scripts\\activate && pip install --upgrade pip
                %VENV%\\Scripts\\activate && pip install -r requirements.txt
                """
            }
        }

        stage('Start Selenium Grid') {

            steps {

                bat """
                docker compose -f docker/docker-compose.yml up -d --scale chrome=4
                """
            }
        }

        stage('Wait For Selenium Grid') {

            steps {

                timeout(time: 2, unit: 'MINUTES') {

                    waitUntil {

                        script {

                            def response = bat(
                                script: 'curl http://localhost:4444/status',
                                returnStatus: true
                            )

                            return response == 0
                        }
                    }
                }
            }
        }

        stage('Run Tests') {

            steps {

                bat """
                set GRID=true && ^
                %VENV%\\Scripts\\activate && ^
                pytest -n 4 --alluredir=allure-results
                """
            }
        }

        stage('Generate Allure Report') {

            steps {

                allure(
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                )
            }
        }
    }

    post {

        always {

            archiveArtifacts(
                artifacts: 'screenshots/*.png',
                allowEmptyArchive: true
            )

            bat """
            docker compose -f docker/docker-compose.yml down
            """
        }

        success {

            echo 'Tests passed successfully!'
        }

        failure {

            echo 'Tests failed!'
        }
    }
}