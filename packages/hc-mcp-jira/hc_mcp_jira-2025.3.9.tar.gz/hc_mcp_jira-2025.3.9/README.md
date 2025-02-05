# hc-mcp-jira

MCP server for Jira integration, providing tools to interact with Jira through the Model Context Protocol (MCP).

## Overview

This server enables seamless integration with Jira, allowing you to perform common Jira operations through MCP tools. It supports comprehensive issue management, project exploration, and user operations.

## Features

The server provides the following Jira integration tools:

- `get_current_user`: Get information about the currently authenticated user
- `create_issue`: Create a new Jira issue with customizable fields
- `update_issue`: Update an existing issue's fields and status
- `get_issue`: Get complete issue details
- `search_issues`: Search for issues in a project using JQL
- `add_comment`: Add a comment to a Jira issue
- `list_projects`: List all accessible Jira projects
- `delete_issue`: Delete a Jira issue
- `create_issue_link`: Create a link between two issues

## Installation

The package supports multiple installation methods:

### Using uvx (Recommended)
```bash
uvx hc-mcp-jira
```

### Using pip
```bash
pip install hc-mcp-jira
```

## Configuration

### Required Environment Variables

- `JIRA_URL`: Your Jira instance URL (e.g., "https://your-domain.atlassian.net")
- `JIRA_USERNAME`: Your Jira username/email
- `JIRA_API_TOKEN`: Your Jira API token

### Claude Desktop Configuration

There are two options to make the server available in Claude Desktop:

1. Using the CLI:
   ```bash
   uvx hc-mcp-jira --add-to-claude
   ```
   If environment variables are not already set, you can specify them:
   ```bash
   uvx hc-mcp-jira --add-to-claude --env JIRA_URL=your-jira-url --env JIRA_USERNAME=your-username --env JIRA_API_TOKEN=your-api-token
   ```
   Any environment variables not explicitly set in the command will be taken from the current environment.

2. Manual configuration:
   - Location:
     - MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
     - Windows: `%APPDATA%/Claude/claude_desktop_config.json`
   
   ```json
   {
     "mcpServers": {
       "hc-mcp-jira": {
         "command": "uvx",
         "args": ["hc-mcp-jira"],
         "env": {
           "JIRA_URL": "your-jira-url",
           "JIRA_USERNAME": "your-username",
           "JIRA_API_TOKEN": "your-api-token"
         }
       }
     }
   }
   ```

### Cline Configuration

There are two options to make the server available in Cline:

1. Using the CLI:
   ```bash
   uvx hc-mcp-jira --add-to-cline
   ```
   If environment variables are not already set, you can specify them:
   ```bash
   uvx hc-mcp-jira --add-to-cline --env JIRA_URL=your-jira-url --env JIRA_USERNAME=your-username --env JIRA_API_TOKEN=your-api-token
   ```
   Any environment variables not explicitly set in the command will be taken from the current environment.

2. Manual configuration:
   - Location:
     - MacOS: `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
     - Cloud9: `~/.vscode-server/data/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

   ```json
   {
     "mcpServers": {
       "hc-mcp-jira": {
         "command": "uvx",
         "args": ["hc-mcp-jira"],
         "env": {
           "JIRA_URL": "your-jira-url",
           "JIRA_USERNAME": "your-username",
           "JIRA_API_TOKEN": "your-api-token"
         }
       }
     }
   }
   ```

## Usage Examples

Here are common usage patterns for the available tools:

### Issue Management
```
1. Create an issue:
   "Create a Jira issue in project KEY with title 'Implement feature X' and type 'Task'"

2. Update an issue:
   "Update issue KEY-123 to add the comment 'Work in progress'"

3. Search issues:
   "Find all open bugs in project KEY assigned to me"

4. Link issues:
   "Create a 'blocks' link between KEY-123 and KEY-456"
```

### Project Management
```
1. List projects:
   "Show me all Jira projects I have access to"

2. Search specific project:
   "Find all issues in project KEY with label 'urgent'"
```

## Development

### Building and Publishing

1. Prepare development environment:
```bash
make prepare
```

2. Build package:
```bash
make build
```

3. Upload to CodeCommit:
```bash
make publish
```


### Debugging

Since MCP servers run over stdio, debugging can be challenging. For the best debugging experience:

1. Use the [MCP Inspector](https://github.com/modelcontextprotocol/inspector):
```bash
npx @modelcontextprotocol/inspector uvx hc-mcp-jira
```

2. Enable debug logging:
```bash
export MCP_DEBUG=1
uvx hc-mcp-jira
```

## Error Handling

The server implements comprehensive error handling:

- Authentication errors: Validates credentials before operations
- API errors: Provides detailed error messages from Jira API
- Input validation: Verifies required fields and formats
- Rate limiting: Handles Jira API rate limits gracefully

## Troubleshooting

Common issues and solutions:

1. Authentication Failed
   - Verify JIRA_URL, JIRA_USERNAME, and JIRA_API_TOKEN are correct
   - Ensure API token has required permissions

2. Rate Limiting
   - Implement exponential backoff in requests
   - Consider batching operations when possible

3. Permission Issues
   - Verify user has required project permissions
   - Check issue-level security settings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
