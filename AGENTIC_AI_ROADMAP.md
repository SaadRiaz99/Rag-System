# Hardcore Agentic AI Engineer Roadmap

## From Zero to Earning - Complete Guide

---

## Earning Potential

| Skill Level | Monthly Earning (PKR) | Monthly Earning (USD) |
|-------------|----------------------|----------------------|
| Beginner (Month 1-2) | 30,000 - 50,000 | $100 - $150 |
| Intermediate (Month 3-4) | 80,000 - 150,000 | $250 - $450 |
| Advanced (Month 5-6) | 200,000 - 400,000 | $600 - $1,200 |
| Expert (Month 6+) | 500,000+ | $1,500+ |

---

## Phase 1: Python Mastery (Week 1-2)

### Week 1: Core Python

| Day | Topic | YouTube Channel | Video to Watch |
|-----|-------|-----------------|----------------|
| 1 | Python Setup & Variables | **Programming with Mosh** | "Python Tutorial for Beginners 1" |
| 2 | Strings & Numbers | **Tech With Tim** | "Python Tutorial for Beginners" |
| 3 | If/Else Conditions | **Corey Schafer** | "Python Tutorial for Beginners 4" |
| 4 | For Loops | **freeCodeCamp** | "Python Tutorial for Beginners" |
| 5 | While Loops | **Programming with Mosh** | "Python Tutorial for Beginners 3" |
| 6 | Lists | **Tech With Tim** | "Python Lists and List Methods" |
| 7 | Dictionaries | **Corey Schafer** | "Python Dictionaries" |

### Week 2: Intermediate Python

| Day | Topic | YouTube Channel | Video to Watch |
|-----|-------|-----------------|----------------|
| 8 | Functions | **Corey Schafer** | "Python Functions" |
| 9 | Lambda Functions | **Tech With Tim** | "Python Lambda Functions" |
| 10 | File I/O | **Corey Schafer** | "Python Tutorial - File Objects" |
| 11 | Error Handling | **Programming with Mosh** | "Python Tutorial for Beginners 11" |
| 12 | Classes & Objects | **Corey Schafer** | "Python OOP Tutorials" |
| 13 | pip & Virtual Environments | **Tech With Tim** | "Python Virtual Environments" |
| 14 | Build Mini Project | **All Channels** | Practice what you learned |

### Practice Projects
```python
# Project 1: Calculator
def calculator():
    num1 = float(input("First number: "))
    op = input("Operator (+, -, *, /): ")
    num2 = float(input("Second number: "))
    
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2

print(calculator())
```

```python
# Project 2: Todo List
todos = []

def add_todo(task):
    todos.append({"task": task, "done": False})

def show_todos():
    for i, todo in enumerate(todos):
        status = "✓" if todo["done"] else "✗"
        print(f"{i+1}. [{status}] {todo['task']}")

add_todo("Learn Python")
add_todo("Build RAG")
show_todos()
```

---

## Phase 2: AI/ML Fundamentals (Week 3-4)

### Week 3: AI Basics

| Day | Topic | YouTube Channel | Video to Watch |
|-----|-------|-----------------|----------------|
| 15 | What is AI/ML/DL | **3Blue1Brown** | "Neural Networks" |
| 16 | How LLMs Work | **Andrej Karpathy** | "Let's build GPT from scratch" |
| 17 | Tokens & Embeddings | **Assembly AI** | "Understanding Embeddings" |
| 18 | OpenAI API Setup | **Fireship** | "OpenAI API in 100 Seconds" |
| 19 | First API Call | **Tech With Tim** | "OpenAI API Tutorial" |
| 20 | Prompt Engineering | **Learn Prompting** | "Prompt Engineering Guide" |
| 21 | Build Chatbot | **All Channels** | Practice |

### Week 4: RAG Deep Dive

| Day | Topic | YouTube Channel | Video to Watch |
|-----|-------|-----------------|----------------|
| 22 | What is RAG | **James Briggs** | "RAG is Simple" |
| 23 | Document Loading | **LangChain** | "Document Loaders" |
| 24 | Text Splitting | **James Briggs** | "Text Splitters in LangChain" |
| 25 | Vector Stores | **Pinecone** | "Vector Databases Explained" |
| 26 | Embeddings Deep Dive | **Assembly AI** | "Embeddings Tutorial" |
| 27 | Semantic Search | **James Briggs** | "Semantic Search Tutorial" |
| 28 | Build RAG System | **All Channels** | Full Project |

### Practice Projects
```python
# Project 3: OpenAI Chatbot
from openai import OpenAI

client = OpenAI()

def chat(message):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

print(chat("What is machine learning?"))
```

```python
# Project 4: Simple RAG
from openai import OpenAI
import faiss
import numpy as np

client = OpenAI()

# Load documents
documents = [
    "Python is a programming language",
    "AI is transforming industries",
    "RAG helps LLMs access external data"
]

# Get embeddings
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Build index
vectors = [get_embedding(doc) for doc in documents]
index = faiss.IndexFlatL2(1536)
index.add(np.array(vectors))

# Search
def search(query, k=2):
    query_vec = get_embedding(query)
    distances, indices = index.search(np.array([query_vec]), k)
    return [documents[i] for i in indices[0]]

print(search("What is Python?"))
```

---

## Phase 3: Agent Development (Week 5-6)

### Week 5: Agent Fundamentals

| Day | Topic | YouTube Channel | Video to Watch |
|-----|-------|-----------------|----------------|
| 29 | What are Agents | **AI Jason** | "AI Agents Explained" |
| 30 | LangChain Agents | **James Briggs** | "LangChain Agents Tutorial" |
| 31 | Function Calling | **OpenAI** | "Function Calling Guide" |
| 32 | Tool Creation | **LangChain** | "Custom Tools" |
| 33 | Agent Memory | **AI Jason** | "Agent Memory Systems" |
| 34 | Multi-Step Agents | **James Briggs** | "ReAct Agents" |
| 35 | Build Agent | **All Channels** | Full Project |

### Week 6: Advanced Agents

| Day | Topic | YouTube Channel | Video to Watch |
|-----|-------|-----------------|----------------|
| 36 | CrewAI Framework | **AI Jason** | "CrewAI Tutorial" |
| 37 | AutoGen | **Microsoft** | "AutoGen Tutorial" |
| 38 | Multi-Agent Systems | **James Briggs** | "Multi-Agent Debate" |
| 39 | Agent Evaluation | **LangChain** | "Evaluating Agents" |
| 40 | Production Agents | **All Channels** | Build & Deploy |

### Practice Projects
```python
# Project 5: Agent with Tools
from openai import OpenAI

client = OpenAI()

def calculator(expression):
    return str(eval(expression))

def web_search(query):
    # Simulated search
    return f"Search results for: {query}"

tools = [
    {
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
    },
    {
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
    }
]

def run_agent(query):
    messages = [{"role": "user", "content": query}]
    
    while True:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            tools=tools
        )
        
        if response.choices[0].finish_reason == "stop":
            return response.choices[0].message.content
        
        tool_call = response.choices[0].message.tool_calls[0]
        func_name = tool_call.function.name
        args = eval(tool_call.function.arguments)
        
        if func_name == "calculator":
            result = calculator(args["expression"])
        elif func_name == "web_search":
            result = web_search(args["query"])
        
        messages.append({"role": "tool", "content": result})

print(run_agent("What is 25 * 4 + 10?"))
```

---

## Phase 4: Production Skills (Week 7-8)

### Week 7: Backend & Deployment

| Day | Topic | YouTube Channel | Video to Watch |
|-----|-------|-----------------|----------------|
| 41 | FastAPI Basics | **FastAPI** | "FastAPI Tutorial" |
| 42 | REST APIs | **Traversy Media** | "REST API Crash Course" |
| 43 | Database (SQLite) | **Corey Schafer** | "SQLite Tutorial" |
| 44 | Database (PostgreSQL) | **Programming with Mosh** | "PostgreSQL Tutorial" |
| 45 | Docker Basics | **TechWorld with Nana** | "Docker Tutorial" |
| 46 | Deployment | **Fireship** | "Deploy Python App" |
| 47 | Build API | **All Channels** | Full Project |

### Week 8: Portfolio & Freelancing

| Day | Topic | YouTube Channel | Video to Watch |
|-----|-------|-----------------|----------------|
| 48 | GitHub Portfolio | **Fireship** | "Git & GitHub Crash Course" |
| 49 | README Writing | **All Channels** | Best practices |
| 50 | LinkedIn Profile | **Ali Abdaal** | "How to Get a Job" |
| 51 | Freelancing Basics | **Ali Abdaal** | "Freelancing for Beginners" |
| 52 | Fiverr/Upwork | **Adrian Twarog** | "How to Get Clients" |
| 53 | Cold Emailing | **Alex Berman** | "Cold Email Templates" |
| 54 | Final Portfolio | **All Channels** | Deploy Everything |

### Practice Projects
```python
# Project 6: FastAPI RAG API
from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()
client = OpenAI()

@app.post("/chat")
async def chat(query: str):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )
    return {"answer": response.choices[0].message.content}

@app.post("/rag")
async def rag_query(question: str, context: str):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Answer based on context:\n{context}"},
            {"role": "user", "content": question}
        ]
    )
    return {"answer": response.choices[0].message.content}

# Run: uvicorn main:app --reload
```

---

## Freelancing Roadmap

### Month 1-2: Learning Phase
- Complete Phase 1 & 2 above
- Build 5 practice projects
- **Earning:** 0 (investment phase)

### Month 3-4: Entry Level Jobs
**Services to Offer:**
1. **Chatbot Development** - $100-300 per project
2. **Data Entry Automation** - $50-150 per project
3. **API Integration** - $100-250 per project
4. **Basic RAG Systems** - $200-500 per project

**Where to Find Work:**
| Platform | Type | Rate |
|----------|------|------|
| Fiverr | Gigs | $50-500 |
| Upwork | Projects | $100-1000 |
| LinkedIn | Network | Varies |
| Local Businesses | Direct | $200-800 |

### Month 5-6: Intermediate Level
**Services to Offer:**
1. **Custom AI Agents** - $500-2000
2. **RAG Systems** - $1000-3000
3. **AI Automation** - $500-1500
4. **Consulting** - $50-100/hour

### Month 7+: Expert Level
**Services to Offer:**
1. **Enterprise AI Solutions** - $5000-20000
2. **Multi-Agent Systems** - $3000-10000
3. **AI Strategy Consulting** - $100-200/hour
4. **Training & Workshops** - $500-2000/day

---

## YouTube Channels - Complete List

### Python Learning
| Channel | Best For | Link |
|---------|----------|------|
| **Corey Schafer** | Python Basics | youtube.com/c/Coreyms |
| **Tech With Tim** | Projects | youtube.com/c/TechWithTim |
| **Programming with Mosh** | Tutorials | youtube.com/c/programmingwithmosh |
| **freeCodeCamp** | Full Courses | youtube.com/c/Freecodecamp |

### AI/ML Learning
| Channel | Best For | Link |
|---------|----------|------|
| **3Blue1Brown** | Math/Visual | youtube.com/c/3blue1brown |
| **Andrej Karpathy** | Deep Learning | youtube.com/c/AndrejKarpathy |
| **Sentdex** | ML Projects | youtube.com/c/sentdex |
| **Two Minute Papers** | Research | youtube.com/c/TwoMinutePapers |

### AI Agents & LLMs
| Channel | Best For | Link |
|---------|----------|------|
| **James Briggs** | LangChain/RAG | youtube.com/c/JamesBriggs |
| **AI Jason** | Agents | youtube.com/c/AIJason |
| **Fireship** | Quick Tutorials | youtube.com/c/Fireship |
| **Assembly AI** | Embeddings | youtube.com/c/AssemblyAI |

### Freelancing & Business
| Channel | Best For | Link |
|---------|----------|------|
| **Ali Abdaal** | Career | youtube.com/c/aliabdaal |
| **Adrian Twarog** | Fiverr/Upwork | youtube.com/c/AdrianTwarog |
| **Alex Berman** | Cold Email | youtube.com/c/AlexBerman |
| **TechLead** | Business | youtube.com/c/TechLead |

---

## Portfolio Projects (Must Build)

### Project 1: AI Chatbot
- Streamlit UI
- OpenAI integration
- Conversation memory
- **Deploy:** Streamlit Cloud

### Project 2: RAG System
- PDF/CSV document loading
- Vector search
- Context-aware answers
- **Deploy:** Railway/Render

### Project 3: AI Agent
- Multiple tools (calculator, search, weather)
- Multi-step reasoning
- Memory system
- **Deploy:** FastAPI + Docker

### Project 4: AI Automation
- Email automation
- Data extraction
- Report generation
- **Deploy:** GitHub Actions

### Project 5: Multi-Agent System
- Agent collaboration
- Task delegation
- Shared memory
- **Deploy:** Kubernetes

---

## Daily Schedule (2 Hours)

```
Morning (1 hour):
- 15 min: Review yesterday
- 30 min: Watch tutorial
- 15 min: Code along

Evening (1 hour):
- 30 min: Build project
- 15 min: Debug & test
- 15 min: Push to GitHub

Weekend:
- 4 hours: Build portfolio project
- 2 hours: Update LinkedIn/GitHub
```

---

## Success Checklist

### Week 2
- [ ] Can write Python without tutorials
- [ ] Built 2 practice projects
- [ ] Pushed code to GitHub

### Week 4
- [ ] Understand LLMs & Embeddings
- [ ] Built working RAG system
- [ ] Created OpenAI API integration

### Week 6
- [ ] Built AI Agent with tools
- [ ] Understand function calling
- [ ] Can explain agents to others

### Week 8
- [ ] Portfolio with 5 projects
- [ ] Active LinkedIn profile
- [ ] First Fiverr/Upwork gig live
- [ ] Sent 10 cold emails

---

## Key Mindset

1. **Consistency > Intensity** - 2 hours daily > 10 hours once
2. **Build > Watch** - Code more than you watch
3. **Teach > Learn** - Explain to learn better
4. **Fail Fast** - Errors are lessons
5. **Ship It** - Done > Perfect

---

## After This Roadmap

You will be able to:
- Build any AI/Agent system
- Freelance independently
- Earn $500-2000/month within 6 months
- Get hired as AI Engineer ($3000-8000/month)

**Your future self will thank you for starting today.** 🚀
