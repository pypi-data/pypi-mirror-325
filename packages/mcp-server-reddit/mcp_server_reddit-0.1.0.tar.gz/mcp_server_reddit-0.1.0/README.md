# MCP Server Reddit

A Model Context Protocol server providing access to Reddit public API for LLMs. This server enables LLMs to interact with Reddit's content, including browsing frontpage posts, accessing subreddit information, and reading post comments.

This server uses [redditwarp](https://github.com/Pyprohly/redditwarp) to interact with Reddit's public API and exposes the functionality through MCP protocol.

## Available Tools

- `get_frontpage_posts` - Get hot posts from Reddit frontpage
  - Optional arguments:
    - `limit` (integer): Number of posts to return (default: 10, range: 1-1000)

- `get_subreddit_info` - Get information about a subreddit
  - Required arguments:
    - `subreddit_name` (string): Name of the subreddit (e.g. 'Python', 'news')

- `get_post_comments` - Get comments from a post
  - Required arguments:
    - `post_id` (string): ID of the post
  - Optional arguments:
    - `limit` (integer): Number of comments to return (default: 10, range: 1-1000)

- `get_subreddit_mods` - Get moderators of a subreddit
  - Required arguments:
    - `subreddit_name` (string): Name of the subreddit (e.g. 'Python', 'news')

- `get_subreddit_hot_posts` - Get hot posts from a specific subreddit
  - Required arguments:
    - `subreddit_name` (string): Name of the subreddit (e.g. 'Python', 'news')
  - Optional arguments:
    - `limit` (integer): Number of posts to return (default: 10, range: 1-1000)

- `get_post_content` - Get detailed content of a specific post
  - Required arguments:
    - `post_id` (string): ID of the post
  - Optional arguments:
    - `comment_limit` (integer): Number of top-level comments to return (default: 10, range: 1-1000)
    - `comment_depth` (integer): Maximum depth of comment tree (default: 3, range: 1-10)

## Installation

### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *mcp-server-reddit*.

### Using PIP

Alternatively you can install `mcp-server-reddit` via pip:

```bash
pip install mcp-server-reddit
```

After installation, you can run it as a script using:

```bash
python -m mcp_server_reddit
```

## Configuration

### Configure for Claude.app

Add to your Claude settings:

<details>
<summary>Using uvx</summary>

```json
"mcpServers": {
  "reddit": {
    "command": "uvx",
    "args": ["mcp-server-reddit"]
  }
}
```
</details>

<details>
<summary>Using pip installation</summary>

```json
"mcpServers": {
  "reddit": {
    "command": "python",
    "args": ["-m", "mcp_server_reddit"]
  }
}
```
</details>

### Configure for Zed

Add to your Zed settings.json:

<details>
<summary>Using uvx</summary>

```json
"context_servers": [
  "mcp-server-reddit": {
    "command": "uvx",
    "args": ["mcp-server-reddit"]
  }
],
```
</details>

<details>
<summary>Using pip installation</summary>

```json
"context_servers": {
  "mcp-server-reddit": {
    "command": "python",
    "args": ["-m", "mcp_server_reddit"]
  }
},
```
</details>

## Examples of Questions

- "What are the current hot posts on Reddit's frontpage"
- "What are the hot posts in the r/ClaudeAI subreddit"
- "Tell me about the r/ClaudeAI subreddit"
- "Who are the moderators of r/ClaudeAI"
- "Show me the top comments on this Reddit post: [post_url]"
- "Get the full content and discussion of this Reddit post: [post_url]"

## Debugging

You can use the MCP inspector to debug the server. For uvx installations:

```bash
npx @modelcontextprotocol/inspector uvx mcp-server-reddit
```

Or if you've installed the package in a specific directory or are developing on it:

```bash
cd path/to/mcp_server_reddit
npx @modelcontextprotocol/inspector uv run mcp-server-reddit
```

## License

mcp-server-reddit is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
