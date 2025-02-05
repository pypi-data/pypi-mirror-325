"""Confluence MCP server providing integration with Confluence's REST API.

This server enables interaction with Confluence through MCP tools, supporting operations like:
- Page management (create, update, delete)
- Space management and listing
- Content search using CQL
- Label and attachment handling
"""
import json
import os
import logging
from typing import Optional, List, Dict, Any, Union

from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio
from atlassian import Confluence

# Define server-specific configuration
SERVER_NAME = "hc-mcp-confluence"
REQUIRED_ENV_VARS: List[str] = ["CONFLUENCE_URL", "CONFLUENCE_USERNAME", "CONFLUENCE_API_TOKEN"]

# Set logging level to WARNING by default
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

def initialize_confluence_client() -> Confluence:
    """Initialize and return Confluence client using environment variables.
    
    Raises:
        ValueError: If required environment variables are missing
    """
    env_vars = {var: os.getenv(var) for var in REQUIRED_ENV_VARS}
    if not all(env_vars.values()):
        raise ValueError(f"Missing required environment variables: {[var for var in REQUIRED_ENV_VARS if not env_vars[var]]}")
    
    return Confluence(
        url=env_vars["CONFLUENCE_URL"],
        username=env_vars["CONFLUENCE_USERNAME"],
        password=env_vars["CONFLUENCE_API_TOKEN"],
        cloud=True  # Assuming cloud instance, set to False for server
    )

# Initialize Confluence client
confluence = initialize_confluence_client()

server = Server(SERVER_NAME)

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available Confluence tools."""
    return [
        types.Tool(
            name="get_page",
            description="Get content and metadata of a specific Confluence page. Returns page content, version info, space details, and other metadata based on expanded fields.",
            inputSchema={
                "type": "object",
                "properties": {
                    "page_id": {
                        "type": "string",
                        "description": "Unique identifier of the Confluence page (required). Found in page URL or API responses."
                    },
                    "expand": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of properties to expand in the response (e.g., ['body.storage', 'version', 'space', 'ancestors']). Controls response detail level."
                    }
                },
                "required": ["page_id"]
            }
        ),
        types.Tool(
            name="create_page",
            description="Create a new Confluence page with specified content, space, title, and optional parent page. Supports XHTML content format. Note: Labels are added in a separate operation after page creation - if label addition fails, the page will still be created but a warning will be included in the response.",
            inputSchema={
                "type": "object",
                "properties": {
                    "space_key": {
                        "type": "string",
                        "description": "Unique key identifier of the Confluence space (required). Usually appears in space URLs (e.g., 'AWS' for 'Chapter Amazon Web Services')."
                    },
                    "title": {
                        "type": "string",
                        "description": "Title for the Confluence page (required). Will be used in page URLs and navigation."
                    },
                    "body": {
                        "type": "string",
                        "description": "Page content in Confluence storage format (XHTML). Must be valid XHTML markup with Confluence macros support."
                    },
                    "parent_id": {
                        "type": "string",
                        "description": "ID of the parent page to create hierarchical structure. Optional - if not provided, page will be created at space root level."
                    },
                    "labels": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of string labels to associate with the page after creation. Labels are case-insensitive and help with organization and searching. Note: Labels are added in a separate operation after page creation."
                    }
                },
                "required": ["space_key", "title", "body"]
            }
        ),
        types.Tool(
            name="update_page",
            description="Update content, title, or version comment of an existing Confluence page. Maintains version history and supports XHTML content format.",
            inputSchema={
                "type": "object",
                "properties": {
                    "page_id": {
                        "type": "string",
                        "description": "Unique identifier of the page to update (required). Must be an existing page ID."
                    },
                    "title": {
                        "type": "string",
                        "description": "New title for the page (optional). If not provided, keeps existing title."
                    },
                    "body": {
                        "type": "string",
                        "description": "New content for the page in Confluence storage format (XHTML) (required). Must be valid XHTML markup."
                    },
                    "version_comment": {
                        "type": "string",
                        "description": "Optional comment describing the changes in this version. Helps track page history and modifications."
                    }
                },
                "required": ["page_id", "body"]
            }
        ),
        types.Tool(
            name="delete_page",
            description="Permanently delete a Confluence page by ID. Use with caution as this operation cannot be undone.",
            inputSchema={
                "type": "object",
                "properties": {
                    "page_id": {
                        "type": "string",
                        "description": "Unique identifier of the page to delete (required). Warning: This operation is permanent and cannot be reversed."
                    }
                },
                "required": ["page_id"]
            }
        ),
        types.Tool(
            name="search_content",
            description="Search Confluence content using CQL (Confluence Query Language). Supports pagination, content filtering, and field expansion. Returns matching pages with metadata.",
            inputSchema={
                "type": "object",
                "properties": {
                    "cql": {
                        "type": "string",
                        "description": "Confluence Query Language (CQL) search string. Supports complex queries with space, type, label, and text criteria. Example: 'space = AWS AND label = documentation'"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 25). Use for pagination and controlling response size.",
                        "default": 25
                    },
                    "expand": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of properties to expand in the results (e.g., ['body.storage', 'version', 'space']). Controls detail level of returned items."
                    }
                },
                "required": ["cql"]
            }
        ),
        types.Tool(
            name="get_space",
            description="Get comprehensive details about a Confluence space including metadata, permissions, and settings. Supports field expansion for additional details.",
            inputSchema={
                "type": "object",
                "properties": {
                    "space_key": {
                        "type": "string",
                        "description": "Unique key identifier of the space (required). Found in space URLs (e.g., 'AWS' for 'Chapter Amazon Web Services')."
                    },
                    "expand": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of properties to expand in response (e.g., ['description', 'homepage', 'metadata']). Controls detail level."
                    }
                },
                "required": ["space_key"]
            }
        ),
        types.Tool(
            name="list_spaces",
            description="List all accessible Confluence spaces with pagination support. Returns space details including key, name, description, and metadata.",
            inputSchema={
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of spaces to return (default: 25). Use for pagination when there are many spaces.",
                        "default": 25
                    },
                    "expand": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of properties to expand in response (e.g., ['description', 'homepage', 'metadata']). Controls detail level."
                    }
                }
            }
        ),
        types.Tool(
            name="add_page_labels",
            description="Add one or more labels to a Confluence page for categorization and organization. Labels improve searchability and content management.",
            inputSchema={
                "type": "object",
                "properties": {
                    "page_id": {
                        "type": "string",
                        "description": "Unique identifier of the page to label (required). Must be an existing page ID."
                    },
                    "labels": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of string labels to add (required). Labels are case-insensitive and can contain spaces."
                    }
                },
                "required": ["page_id", "labels"]
            }
        ),
        types.Tool(
            name="get_page_labels",
            description="Retrieve all labels associated with a Confluence page. Returns label names and metadata.",
            inputSchema={
                "type": "object",
                "properties": {
                    "page_id": {
                        "type": "string",
                        "description": "Unique identifier of the page to get labels from (required). Must be an existing page ID."
                    }
                },
                "required": ["page_id"]
            }
        ),
        types.Tool(
            name="get_page_attachments",
            description="Retrieve all attachments associated with a Confluence page. Returns attachment metadata including filename, size, and download links.",
            inputSchema={
                "type": "object",
                "properties": {
                    "page_id": {
                        "type": "string",
                        "description": "Unique identifier of the page to get attachments from (required). Must be an existing page ID."
                    }
                },
                "required": ["page_id"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle Confluence tool execution requests."""
    try:
        if not arguments:
            raise ValueError("Arguments are required")

        if name == "get_page":
            page_id = arguments.get("page_id")
            expand = arguments.get("expand", ["body.storage", "version"])
            
            if not page_id:
                raise ValueError("page_id is required")
                
            page = confluence.get_page_by_id(
                page_id,
                expand=",".join(expand)
            )
            
            return [types.TextContent(
                type="text",
                text=json.dumps(page, indent=2)
            )]

        elif name == "create_page":
            space_key = arguments.get("space_key")
            title = arguments.get("title")
            body = arguments.get("body")
            parent_id = arguments.get("parent_id")
            labels = arguments.get("labels", [])
            
            if not all([space_key, title, body]):
                raise ValueError("space_key, title, and body are required")
            
            try:
                # First create the page
                page = confluence.create_page(
                    space=space_key,
                    title=title,
                    body=body,
                    parent_id=parent_id,
                    representation="storage"
                )
                
                # If labels are provided, add them with a small delay to ensure page is fully created
                if labels:
                    try:
                        # Get the page again to ensure it's fully created
                        created_page = confluence.get_page_by_id(
                            page["id"],
                            expand="version"
                        )
                        
                        # Now add labels
                        label_result = confluence.set_page_labels(
                            page_id=created_page["id"],
                            labels=labels
                        )
                        
                        # Add label info to response
                        page["labels"] = label_result
                    except Exception as label_error:
                        # If label addition fails, return page with warning
                        page["warning"] = f"Page created successfully but labels could not be added: {str(label_error)}"
                
                return [types.TextContent(
                    type="text",
                    text=json.dumps(page, indent=2)
                )]
            except Exception as e:
                raise ValueError(f"Failed to create page: {str(e)}")

        elif name == "update_page":
            page_id = arguments.get("page_id")
            body = arguments.get("body")
            title = arguments.get("title")
            version_comment = arguments.get("version_comment")
            
            if not all([page_id, body]):
                raise ValueError("page_id and body are required")
            
            # Get current page info
            page = confluence.get_page_by_id(
                page_id,
                expand="version"
            )
            
            # Update the page
            updated_page = confluence.update_page(
                page_id=page_id,
                title=title or page["title"],
                body=body,
                parent_id=page.get("parent", {}).get("id"),
                version_comment=version_comment,
                representation="storage"
            )
            
            return [types.TextContent(
                type="text",
                text=json.dumps(updated_page, indent=2)
            )]

        elif name == "delete_page":
            page_id = arguments.get("page_id")
            
            if not page_id:
                raise ValueError("page_id is required")
            
            confluence.delete_page(page_id)
            
            return [types.TextContent(
                type="text",
                text=json.dumps({"message": "Page deleted successfully"}, indent=2)
            )]

        elif name == "search_content":
            cql = arguments.get("cql")
            limit = arguments.get("limit", 25)
            expand = arguments.get("expand", ["body.storage", "version"])
            
            if not cql:
                raise ValueError("cql is required")
            
            results = confluence.cql(
                cql,
                limit=limit,
                expand=",".join(expand)
            )
            
            return [types.TextContent(
                type="text",
                text=json.dumps(results, indent=2)
            )]

        elif name == "get_space":
            space_key = arguments.get("space_key")
            expand = arguments.get("expand", ["description"])
            
            if not space_key:
                raise ValueError("space_key is required")
            
            space = confluence.get_space(
                space_key,
                expand=",".join(expand)
            )
            
            return [types.TextContent(
                type="text",
                text=json.dumps(space, indent=2)
            )]

        elif name == "list_spaces":
            limit = arguments.get("limit", 25)
            expand = arguments.get("expand", ["description"])
            
            spaces = confluence.get_all_spaces(
                limit=limit,
                expand=",".join(expand)
            )
            
            return [types.TextContent(
                type="text",
                text=json.dumps(spaces, indent=2)
            )]

        elif name == "add_page_labels":
            page_id = arguments.get("page_id")
            labels = arguments.get("labels", [])
            
            if not all([page_id, labels]):
                raise ValueError("page_id and labels are required")
            
            result = confluence.set_page_labels(
                page_id=page_id,
                labels=labels
            )
            
            return [types.TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]

        elif name == "get_page_labels":
            page_id = arguments.get("page_id")
            
            if not page_id:
                raise ValueError("page_id is required")
            
            labels = confluence.get_page_labels(page_id)
            
            return [types.TextContent(
                type="text",
                text=json.dumps(labels, indent=2)
            )]

        elif name == "get_page_attachments":
            page_id = arguments.get("page_id")
            
            if not page_id:
                raise ValueError("page_id is required")
            
            attachments = confluence.get_attachments_from_content(page_id)
            
            return [types.TextContent(
                type="text",
                text=json.dumps(attachments, indent=2)
            )]

        else:
            raise ValueError(f"Unknown tool: {name}")

    except Exception as e:
        error_message = str(e)
        error_details = {
            "error": error_message,  # Simple message for LLM
            "details": {  # Detailed context for debugging
                "name": e.__class__.__name__,
                "message": str(e),
                "tool": name,
                "arguments": arguments
            }
        }
        return [types.TextContent(
            type="text",
            text=json.dumps(error_details, indent=2),
            isError=True
        )]


import importlib.metadata

async def main():
    """Run the server using stdin/stdout streams."""
    # Get version from package metadata
    try:
        version = importlib.metadata.version(__package__)
    except importlib.metadata.PackageNotFoundError:
        version = "0.0.0"

    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=SERVER_NAME,
                server_version=version,
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
