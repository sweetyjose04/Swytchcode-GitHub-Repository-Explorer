\# GitHub Repository Explorer using Swytchcode



\## 1. Project Overview



GitHub Repository Explorer is a Python-based practical application that retrieves and displays repository information from GitHub organizations using the Swytchcode CLI.



The project demonstrates how Swytchcode simplifies API integration, authentication, and API execution through reusable integration methods.



\## 2. Technology Stack



\- Python 3.10

\- Swytchcode CLI v2.25.5

\- GitHub API

\- OAuth 2.0 Authentication

\- JSON

\- PowerShell



\## 3. Integration Used



\*\*Provider:\*\* GitHub



\*\*Bundle:\*\* GitHub.github@1.1.4



\*\*Method:\*\* `github.repo.get`



\*\*API Endpoint:\*\* `GET /orgs/{org}/repos`



\*\*Authentication:\*\* OAuth2



\## 4. Features



\- Accepts a GitHub organization name.

\- Retrieves repositories using Swytchcode.

\- Displays repository names and descriptions.

\- Displays programming languages.

\- Displays star and fork counts.

\- Provides repository URLs.

\- Processes API responses in JSON format.



\## 5. Project Setup



\### Create a virtual environment



```powershell

python -m venv venv

.\\venv\\Scripts\\activate

```



\### Connect GitHub



```powershell

swytchcode auth connect GitHub

```



\### Install the integration



```powershell

swytchcode get github

```



\### Execute the API operation



```powershell

swytchcode exec github.repo.get --input org=github --param per\_page=5 --json

```



\### Run the Python application



```powershell

python app.py

```



\## 6. What Worked



\- Successfully initialized the Swytchcode project.

\- Installed the GitHub integration bundle.

\- Inspected the generated Wrekenfile.

\- Connected GitHub using OAuth2.

\- Executed a live GitHub API operation.

\- Retrieved five repository records successfully.

\- Integrated Swytchcode CLI with Python using subprocess.

\- Parsed the JSON response and displayed repository details.



\## 7. Challenges and Resolutions



| Challenge | Resolution |

|---|---|

| Missing sandbox endpoint | Configured `sandbox\_endpoint` in the integration manifest |

| Python could not launch Swytchcode | Invoked the CLI through `cmd.exe` |

| Windows Unicode decoding error | Added UTF-8 encoding and replacement handling |



\## 8. Project Structure



```text

Swytchcode-GitHub-Repository-Explorer/
│
├── .swytchcode/
│   ├── tooling.json
│   └── integrations/
│       ├── manifest.json
│       └── GitHub/
│           └── github/
│               └── 1.1.4/
│                   ├── methods.json
│                   └── wrekenfile.yaml
│
├── app.py
├── README.md
├── friction-diary.md
└── .gitignore
```



The generated Wrekenfile is located under `.swytchcode/integrations/GitHub/github/1.1.4/`.



\## 9. Conclusion



This project demonstrates how Swytchcode can simplify API integration and execution. Instead of manually implementing the GitHub API request and authentication flow, developers can use an installed integration method through the Swytchcode CLI and consume its response in a Python application.



\## 10. AI Usage Disclosure



AI assistance was used for understanding CLI commands, troubleshooting configuration and execution errors, and developing the Python demonstration. All commands and application behavior were tested locally.


## What is Swytchcode?

Swytchcode is a CLI-based tool that helps developers
integrate and execute external API operations through
a standardized workflow.

It provides integration bundles, predefined methods,
authentication management, and commands to execute API
operations. Instead of manually implementing every API
request, developers can explore available integrations,
inspect methods, configure authentication, and execute
operations using the CLI.

For this project, I used Swytchcode to integrate the
GitHub REST API. I installed the GitHub integration,
connected my GitHub account using OAuth, and executed
the `github.repo.get` method to retrieve repositories
belonging to an organization.

I then developed a Python-based GitHub Repository
Explorer that uses the Swytchcode CLI to retrieve and
display repository names, descriptions, programming
languages, stars, forks, and URLs.

Swytchcode simplifies API integration workflows and
helps developers build practical applications using
existing API operations.
