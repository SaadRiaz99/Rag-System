# Agentic AI Engineer Roadmap

A complete 30-day practical roadmap to become an Agentic AI Engineer.

## Project Structure
```
├── main.py           # Document loader
├── document/         # CSV documents
├── pyproject.toml    # Project config
└── README.md
```

---

## Phase 1: Python Fundamentals (Day 1-7)

### Day 1: Variables & Data Types
```python
name = "Saad"
age = 25
height = 5.9
is_student = True

print(f"Name: {name}, Age: {age}")
```

### Day 2: Conditions
```python
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Day 3: Loops
```python
for i in range(5):
    print(i)

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

### Day 4: Lists & Dictionaries
```python
# Lists
users = ["Ali", "Saad", "Ahmed"]
users.append("Usman")

# Dictionaries
user = {"name": "Saad", "age": 25, "city": "Lahore"}
print(user["name"])
```

### Day 5: Functions
```python
def greet(name):
    return f"Hello {name}!"

message = greet("Saad")
print(message)
```

### Day 6: File I/O
```python
# Read
with open("data.txt", "r") as f:
    content = f.read()

# Write
with open("output.txt", "w") as f:
    f.write("Hello World")
```

### Day 7: Error Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")
```

---

## Phase 2: RAG System (Day 8-14)

### Day 8: CSV Loading
```python
import csv

def load_csv(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))

docs = load_csv("document/data.csv")
```

### Day 9: Text Chunking
```python
def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

text = "Long document text here..."
chunks = chunk_text(text)
```

### Day 10: OpenAI Embeddings
```python
from openai import OpenAI

client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Hello world"
)

vector = response.data[0].embedding  # 1536 dimensions
```

### Day 11: Cosine Similarity
```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

score = cosine_similarity(vec1, vec2)
```

### Day 12: FAISS Vector Store
```python
import faiss

dimension = 1536
index = faiss.IndexFlatL2(dimension)

# Add vectors
index.add(np.array([vector1, vector2]))

# Search
distances, indices = index.search(np.array([query_vec]), k=3)
```

### Day 13: Store Document Embeddings
```python
def build_index(documents):
    vectors = []
    for doc in documents:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=doc["content"]
        )
        vectors.append(response.data[0].embedding)
    
    index = faiss.IndexFlatL2(1536)
    index.add(np.array(vectors))
    return index
```

### Day 14: Search Function
```python
def search(query, index, documents, k=3):
    query_vec = get_embedding(query)
    distances, indices = index.search(np.array([query_vec]), k)
    return [documents[i] for i in indices[0]]
```

---

## Phase 3: LLM Integration (Day 15-21)

### Day 15: Chat API
```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What is AI?"}]
)

answer = response.choices[0].message.content
```

### Day 16: System Prompts
```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain RAG"}
    ]
)
```

### Day 17: Context Injection
```python
def ask_with_context(query, context):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Answer based on context:\n{context}"},
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message.content
```

### Day 18: Full RAG Chain
```python
def rag_query(question):
    # Step 1: Search relevant docs
    docs = search(question, index, documents)
    context = "\n".join([d["content"] for d in docs])
    
    # Step 2: Generate answer
    return ask_with_context(question, context)
```

### Day 19: Error Handling
```python
from openai import APIError

try:
    response = client.chat.completions.create(...)
except APIError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"Error: {e}")
```

### Day 20: Stream Responses
```python
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

### Day 21: Test Your RAG
```python
# Ask questions about your documents
questions = [
    "What is this document about?",
    "Summarize the main points",
    "What are the key topics?"
]

for q in questions:
    print(f"Q: {q}")
    print(f"A: {rag_query(q)}\n")
```

---

## Phase 4: Agents (Day 22-30)

### Day 22: What Are Agents?
```
Agent = LLM + Tools + Memory + Planning

- LLM: Brain of the agent
- Tools: Functions agent can call
- Memory: Store past interactions
- Planning: Break tasks into steps
```

### Day 23: Function Calling
```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            }
        }
    }
}]

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Weather in Lahore?"}],
    tools=tools
)
```

### Day 24: Calculator Tool
```python
def calculator(expression):
    return eval(expression)

# LLM decides when to use calculator
tools = [{
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Calculate math expressions",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {"type": "string"}
            }
        }
    }
}]
```

### Day 25: Web Search Tool
```python
def web_search(query):
    # Use search API
    results = search_api(query)
    return results

tools = [{
    "type": "function",
    "function": {
        "name": "web_search",
        "description": "Search the web",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            }
        }
    }
}]
```

### Day 26: Multi-Step Agent
```python
def agent_run(query):
    messages = [{"role": "user", "content": query}]
    
    while True:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            tools=tools
        )
        
        if response.choices[0].finish_reason == "stop":
            return response.choices[0].message.content
        
        # Execute tool call
        tool_call = response.choices[0].message.tool_calls[0]
        result = execute_tool(tool_call)
        
        messages.append({"role": "tool", "content": str(result)})
```

### Day 27: Memory System
```python
class AgentMemory:
    def __init__(self):
        self.history = []
    
    def add(self, role, content):
        self.history.append({"role": role, "content": content})
    
    def get_context(self, last_n=10):
        return self.history[-last_n:]
```

### Day 28: LangChain Basics
```python
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

llm = ChatOpenAI(model="gpt-4")
conversation = ConversationChain(llm=llm)

response = conversation.predict(input="Hello!")
```

### Day 29: Build Simple Agent
```python
from langchain.agents import initialize_agent
from langchain.tools import Tool

tools = [
    Tool(name="Search", func=search_docs, description="Search documents"),
    Tool(name="Calculator", func=calculator, description="Calculate math")
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
result = agent.run("Find documents about AI and calculate 2+2")
```

### Day 30: Final Project
```
Your RAG + Agent Combined:

1. User asks question
2. Agent decides: search docs OR calculate OR web search
3. Agent executes tool
4. Agent generates answer with context
5. Store in memory for next query
```

---

## Learning Tips

### Daily Routine (30 mins)
```
5 min  - Review yesterday
15 min - Learn new concept
10 min - Code practice
```

### Debug Method
```python
# When stuck, print everything
print(f"Type: {type(variable)}")
print(f"Value: {variable}")
print(f"Length: {len(variable)}")
```

### Common Mistakes to Avoid
1. **Don't copy-paste** - Type code yourself
2. **Don't skip basics** - Master Python first
3. **Don't rush** - One concept per day
4. **Don't skip errors** - Fix them, don't ignore

---

## Resources

### Documentation
- Python: https://docs.python.org/3/tutorial/
- OpenAI: https://platform.openai.com/docs
- LangChain: https://python.langchain.com/

### Practice
- LeetCode: https://leetcode.com (Easy problems)
- HackerRank: https://hackerrank.com/python

### YouTube
- Corey Schafer - Python Tutorials
- FreeCodeCamp - Python Course

---

## After 30 Days

You will have:
- [x] Strong Python foundation
- [x] Working RAG system
- [x] LLM integration skills
- [x] Agent building capability
- [x] Portfolio project

**Next Level:** Build production-ready agents with memory, tools, and multi-agent systems.
