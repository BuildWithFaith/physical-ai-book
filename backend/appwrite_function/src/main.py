import json
import asyncio
from .retrieval import query_rag_system
import os

# Appwrite Function Entrypoint
async def main(context):
    """
    Appwrite Function Entrypoint
    
    The 'context' object contains:
    - req: The request object (headers, body, method, path)
    - res: The response object (json, send)
    - log: Function to log messages
    - error: Function to log errors
    """
    
    # Enable CORS
    if context.req.method == 'OPTIONS':
        return context.res.send('', 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, X-Appwrite-Project, X-Appwrite-Key'
        })

    if context.req.method != 'POST':
        return context.res.json({
            'error': 'Method not allowed. Use POST.'
        }, 405, {
            'Access-Control-Allow-Origin': '*'
        })

    try:
        # Parse Request Body
        body = context.req.body
        if isinstance(body, str):
            try:
                payload = json.loads(body)
            except json.JSONDecodeError:
                return context.res.json({
                    'error': 'Invalid JSON body'
                }, 400, {
                    'Access-Control-Allow-Origin': '*'
                })
        else:
            payload = body

        query = payload.get('query')
        top_k = payload.get('top_k', 5)

        if not query:
            return context.res.json({
                'error': 'Missing required field: query'
            }, 400, {
                'Access-Control-Allow-Origin': '*'
            })

        # Log connection info (optional, be careful with secrets)
        context.log(f"Processing query: {query}")

        # Ensure environment variables are set (they should be set in Appwrite Console)
        if not os.environ.get("OPENAI_API_KEY"):
            context.error("OPENAI_API_KEY not set")
            return context.res.json({'error': 'Server configuration error'}, 500)

        # Call the RAG system
        # Note: query_rag_system is async, so we await it
        result = await query_rag_system(query, top_k)

        return context.res.json(result, 200, {
            'Access-Control-Allow-Origin': '*'
        })

    except Exception as e:
        context.error(f"Error processing request: {str(e)}")
        return context.res.json({
            'error': 'Internal Server Error',
            'details': str(e)
        }, 500, {
            'Access-Control-Allow-Origin': '*'
        })
