\# Swytchcode PPI – Friction Diary



| Step | Action / Command | Expected Result | Actual Result / Issue | Resolution |

|---|---|---|---|---|

| 1 | Install Swytchcode CLI | CLI installed | Installation successful | None |

| 2 | `swytchcode init` | Initialize project | Project initialized successfully | None |

| 3 | `swytchcode get github` | Install GitHub integration | GitHub bundle installed | None |

| 4 | `swytchcode list` | Discover available methods | Many methods displayed | Reviewed relevant methods |

| 5 | `swytchcode info github.repo.get` | Inspect API method | Found organization repository endpoint and inputs | Identified required `org` input |

| 6 | `swytchcode auth connect GitHub` | Authenticate GitHub | OAuth2 connection successful | None |

| 7 | Execute `github.repo.get` | Retrieve repositories | Failed because sandbox endpoint was empty | Updated sandbox endpoint in manifest |

| 8 | Retry API execution | Get repository data | HTTP 200; five repositories returned | Successful |

| 9 | Run Python application | Call Swytchcode from Python | Python could not locate CLI executable | Invoked through `cmd.exe` |

| 10 | Run Python application again | Parse JSON response | Windows UnicodeDecodeError occurred, but data was displayed | Set UTF-8 encoding and `errors="replace"` |

| 11 | Final Python execution | Display repository information | Five repositories displayed without decoding error | Successful |



\## Documentation and AI Assistance



\- Consulted Swytchcode CLI help output.

\- Used `swytchcode info` to inspect the API method schema.

\- Used `swytchcode exec --help` to understand execution options.

\- Used `swytchcode auth --help` to understand provider authentication.

\- AI assistance helped identify configuration, subprocess, and encoding issues.

\- Tested suggested fixes locally and verified the final API response.



\## Final Outcome



Successfully connected GitHub through OAuth2, executed a live GitHub API operation using Swytchcode, and developed a Python application to display repository information.

