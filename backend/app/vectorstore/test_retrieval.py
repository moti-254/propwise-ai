import asyncio
from app.vectorstore.query import query_similar_properties

async def main():
    query = input("Enter a property description to search: ")
    results = await query_similar_properties(query, top_k=5)
    print("\nTop 5 similar properties:")
    for i, doc in enumerate(results.get('documents', [[]])[0]):
        print(f"{i+1}. {doc}")
    print("\nMetadata:")
    for i, meta in enumerate(results.get('metadatas', [[]])[0]):
        print(f"{i+1}. {meta}")

if __name__ == "__main__":
    asyncio.run(main())
