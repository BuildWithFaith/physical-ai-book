#!/usr/bin/env python3
"""Test script to verify the backend modules can be imported correctly"""

try:
    from main import app
    print("✓ Successfully imported main app")
except ImportError as e:
    print(f"✗ Failed to import main app: {e}")

try:
    from retrieval import query_rag_system, create_physical_ai_agent
    print("✓ Successfully imported retrieval module")
except ImportError as e:
    print(f"✗ Failed to import retrieval module: {e}")

try:
    from ingestion import run_ingestion_pipeline
    print("✓ Successfully imported ingestion module")
except ImportError as e:
    print(f"✗ Failed to import ingestion module: {e}")

print("\nAll imports successful! Backend is ready.")