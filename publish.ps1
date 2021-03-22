pytest -v -o junit_family=xunit1 `
       --cov=src/ --cov=test/ `
       --cov-report xml:test-results/coverage.xml `
       --cov-report html:test-results/cov_html `
       --junitxml=test-results/results.xml

sonar-scanner -D"project.settings=sonar-project.properties"