#!/usr/bin/env python3
"""Test script to verify the chat endpoint works correctly"""

import asyncio
from retrieval import query_rag_system

def test_chat_query():
    """Test a sample query to the RAG system"""
    query = "What is the nervous system in ROS2?"
    print(f"Testing query: '{query}'")

    result = query_rag_system(query, top_k=3)

    print(f"Answer: {result['answer']}")
    print(f"Sources: {result['sources']}")
    print("\nTest completed successfully!")

if __name__ == "__main__":
    test_chat_query()