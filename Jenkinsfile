pipeline {

    agent any

    tools {
        allure 'allure'
    }
    environment {

        PYTHON = "python3"

        VENV = "venv"

        GRID = "true"
    }

    options {

        timestamps()
    }

    stages {

        stage('Checkout Source Code') {

            steps {

                git branch: 'main',
                url: 'https://github.com/chinnalasairaghavendra/ExpandNotesTesting'
            }
        }

        stage('Install Python and Dependencies') {

            steps {

                sh '''
                python3 -m venv venv
                '''

                sh '''
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Start Selenium Grid') {

            steps {

                sh '''
                docker compose -f docker/docker-compose.yml up -d --scale chrome=2
                '''
            }
        }

        stage('Wait For Selenium Grid') {

            steps {

                timeout(time: 2, unit: 'MINUTES') {

                    waitUntil {

                        script {

                            def response = sh(
                                script: 'curl -s http://host.docker.internal:4444/status',
                                returnStatus: true
                            )

                            return response == 0
                        }
                    }
                }
            }
        }

        stage('Run Parallel Tests') {

            steps {

                sh '''
                export GRID=true

                . venv/bin/activate

                pytest -n 2 \
                --alluredir=allure-results \
                --html=report.html \
                --self-contained-html
                '''
            }
        }

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

            sh '''
            docker compose -f docker/docker-compose.yml down
            '''
        }

        success {

            echo 'Pipeline completed successfully!'
        }

        failure {

            echo 'Pipeline execution failed!'
        }
    }
}