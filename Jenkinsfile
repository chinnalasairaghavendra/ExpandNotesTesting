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

        /*
        1. Checkout Source Code
        */
        stage('Checkout Source Code') {

            steps {

                git branch: 'main',
                url: 'https://github.com/chinnalasairaghavendra/ExpandNotesTesting'
            }
        }

        /*
        2. Install Python and Dependencies
        */
        stage('Install Python and Dependencies') {

            steps {

                bat """
                %PYTHON% -m venv %VENV%
                """

                bat """
                %VENV%\\Scripts\\activate && pip install --upgrade pip
                """

                bat """
                %VENV%\\Scripts\\activate && pip install -r requirements.txt
                """
            }
        }

        /*
        Start Selenium Grid
        */
        stage('Start Selenium Grid') {

            steps {

                bat """
                docker compose -f docker/docker-compose.yml up -d --scale chrome=4
                """
            }
        }

        /*
        Wait For Selenium Grid
        */
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

        /*
        3. Parallel Test Execution
        Using pytest-xdist
        */
        stage('Run Parallel Tests') {

            steps {

                bat """
                set GRID=true && ^
                %VENV%\\Scripts\\activate && ^
                pytest -n 4 ^
                --alluredir=allure-results ^
                --html=report.html ^
                --self-contained-html
                """
            }
        }

        /*
        4. Publish Reports
        HTML + Allure
        */
        stage('Publish Reports') {

            steps {

                publishHTML([
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report'
                ])

                allure(
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                )
            }
        }

        /*
        5. Upload Artifacts
        Screenshots, Logs, Reports
        */
        stage('Upload Artifacts') {

            steps {

                archiveArtifacts(
                    artifacts: '''
                        screenshots/*.png,
                        logs/*.log,
                        allure-results/**/*,
                        report.html
                    ''',
                    allowEmptyArchive: true
                )
            }
        }
    }

    post {

        always {

            bat """
            docker compose -f docker/docker-compose.yml down
            """
        }

        success {

            echo 'Pipeline completed successfully!'
        }

        failure {

            echo 'Pipeline execution failed!'
        }
    }
}