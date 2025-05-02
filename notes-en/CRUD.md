# CRUD
-  This is a demonstration project and notes showcasing basic CRUD (Create, Read, Update, Delete) operations implemented with the ability to switch between different backend frameworks, databases, and API patterns while maintaining a consistent frontend. 
- This repository features minimalistic code and package usage, designed for interview scenarios and code tests.
- The original repository is located at https://github.com/luoxisteven/CRUD-Demo.

## Table of Contents
- **Frontend**
  - [React](#react)
    - RestAPI
    - GraphQL
  - [Angular](#angular)
- **Backend**
  - [Node.js](#nodejs)
    - JSON
    - MySQL
    - MongoDB
    - RestAPI
    - GraphQL
  - [.NET](#dotnet)
    - JSON
    - In-Memory Database
    - MySQL
    - MongoDB
  - [Django](#django)
    - SQLite
    - MySQL


## Task Module
### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/task     | Get all tasks |
| GET | /api/task/:id | Get a specific task by ID |
| POST | /api/task    | Create a new task |
| PUT | /api/task/:id | Update an existing task |
| DELETE | /api/task/:id | Delete a task |

### API Usage Examples

#### 1) Create a Task 

**Request:**
```http
POST /api/tasks
Content-Type: application/json

{
  "title": "Complete project",
  "description": "Finish the task management API",
  "status": "In Progress"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Finish the task management API",
  "status": "In Progress",
  "createdAt": "2025-03-15T10:30:00.000Z",
  "updatedAt": "2025-03-15T10:30:00.000Z"
}
```

#### 2) Get All Tasks

**Request:**
```http
GET /api/tasks
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Finish the task management API",
    "status": "In Progress",
    "createdAt": "2025-03-15T10:30:00.000Z",
    "updatedAt": "2025-03-15T10:30:00.000Z"
  },
  {
    "id": 2,
    "title": "Test API",
    "description": "Test all API endpoints",
    "status": "To Do",
    "createdAt": "2025-03-15T10:35:00.000Z",
    "updatedAt": "2025-03-15T10:35:00.000Z"
  }
]
```


## React

### Features

- View all tasks in a clean tabular layout
- Add new tasks with title, description, and status
- Edit existing tasks
- Delete tasks
- Simple and intuitive user interface
- Minimal dependencies

### Tech Stack

- React 18
- TypeScript
- Vite (for fast development and building)
- CSS (plain, no frameworks)
- RestAPI / GraphQL

### Project Structure

``` bash
src/
├── api/
│   └── taskApi.ts         # API client for backend communication
├── hooks/
│   └── useTasks.ts        # Custom hook for task state management
├── pages/
│   ├── Home.tsx           # Main page component
│   └── About.tsx          # About page component
├── types/
│   └── Task.ts            # TypeScript type definitions
├── App.css                # Global styles
├── App.tsx                # Root component
├── config.tsx             # Configuration
└── main.tsx               # Application entry point
```

### Setup and Installation
1. Install dependencies:
```bash
npm install
```

2. Configuration (`src/config.tsx`):

    1) In `src/api/taskApi.ts`, make sure the `API_URL` constant points to your backend API:
        ```typescript
        const API_URL = 'http://localhost:3000/api';
        ```
    2) Choose your apitype (either `restapi` or `graphql`)
        ```typescript
        apiType: 'restapi', // 'restapi' or 'graphql'
        ```

### Initialize the project
```bash
# Upgrade your node
nvm install --lts

npm create vite@latest ts-front -- --template react-ts
cd ts-front
npm install
```

### Install router dependencies (optional for router)
```bash
npm install axios
npm install react-router-dom @types/react-router-dom
```


### Building for Production
```bash
npm run build
```

### Run
```bash
npm run dev
```

### index.html
``` html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Task Manager: By Steven Luo</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

### src/config.tsx
``` jsx
const config = {
    apiUrl: 'http://localhost:3000/api',
    apiType: 'restapi', // 'restapi' or 'graphql'
  };
  
export default config;
```

### src/main.tsx
``` jsx
// src/main.tsx
// import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  // <StrictMode>
    <App />
  // </StrictMode>,
)
```

### src/App.tsx
``` jsx
// src/App.tsx
import Home from './pages/Home';
import './App.css';
import AppRoute from './AppRoute';

function App() {
  return (
    <div className="app">
      {/* Without Route */}
      <Home />

      {/* With Route */}
      {/* <AppRoute /> */}
    </div>
  );
}

export default App;
```

### src/AppRoute.tsx (optional: route)
``` jsx
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';

function AppRoute() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} /> 
      </Routes>
    </Router>
  );
}

export default AppRoute;
```

### src/App.css
``` css
/* Basic reset and global styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: sans-serif;
}

body {
  line-height: 1.5;
  background-color: #f5f5f5;
  color: #333;
}

/* Layout */
.container {
  max-width: 800px;
  margin: 0 auto; /* top and bottom is zero, and left and right are auto (middle) */
  padding: 20px;
}

h1 {
  margin-bottom: 20px;
  font-weight: 600;
  font-size: 24px;
}

h2 {
  margin-bottom: 15px;
  font-weight: 500;
  font-size: 18px;
}

/* Card style for form and task list */
.card {
  background: white;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  padding: 15px;
  margin-bottom: 20px;
}

/* Form styling */
.form-group {
  margin-bottom: 15px;
}

input, textarea, select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

textarea {
  min-height: 80px;
}

.button-group {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

button {
  padding: 8px 16px;
  background-color: #0066cc;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

button:hover {
  opacity: 0.9;
}

/* Task table styling */
.task-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.task-table th {
  text-align: left;
  padding: 10px;
  border-bottom: 2px solid #ddd;
  font-weight: 600;
}

.task-table td {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

.task-row:hover {
  background-color: #f9f9f9;
}

/* Button styles in table */
.task-table button {
  padding: 5px 10px;
  margin-right: 5px;
  font-size: 13px;
}

.task-table button:first-child {
  background-color: #6c757d;
}

.task-table button:last-child {
  background-color: #dc3545;
}

/* Utility classes */
.error-message {
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
  color: #721c24;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 15px;
  font-size: 14px;
}

.toggle-list {
  margin-bottom: 20px;
  margin-left: 5px;
}
```

### src/types/Task.tsx
``` typescript
export type TaskStatus = 'To Do' | 'In Progress' | 'Done';

export interface Task {
  id: number;
  _id?: number | undefined;
  title: string;
  description: string;
  status: TaskStatus;
  createdAt?: string | undefined;
  updatedAt?: string | undefined;
}

export interface TaskFormData {
  title: string;
  description: string;
  status: TaskStatus;
}

// Only for MongoDB
export function normalizeTask(task: any): Task {
  if (task.id === undefined && task._id !== undefined) {
    return {
      ...task,
      id: task._id
    };
  }
  return task as Task;
}
```

### src/api/taskRestAPI.tsx
``` jsx
import { Task, TaskFormData } from '../types/Task';
import config from '../config';

export const taskApi = {
  // Get all tasks
  async getAll(): Promise<Task[]> {
    const response = await fetch(`${config.apiUrl}/task`);
    if (!response.ok) {
      throw new Error(`Failed to fetch tasks: ${response.statusText}`);
    }
    return response.json();
  },

  // Get a task by ID
  async getById(id: number): Promise<Task> {
    const response = await fetch(`${config.apiUrl}/task/${id}`);
    if (!response.ok) {
      throw new Error(`Failed to fetch task with ID ${id}: ${response.statusText}`);
    }
    return response.json();
  },

  // Create a new task
  async create(task: TaskFormData): Promise<Task> {
    const response = await fetch(`${config.apiUrl}/task`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(task),
    });
    if (!response.ok) {
      throw new Error(`Failed to create task: ${response.statusText}`);
    }
    return response.json();
  },

  // Update a task
  async update(id: number, task: Partial<TaskFormData>): Promise<Task> {
    const response = await fetch(`${config.apiUrl}/task/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(task),
    });
    if (!response.ok) {
      throw new Error(`Failed to update task with ID ${id}: ${response.statusText}`);
    }
    return response.json();
  },

  // Delete a task
  async delete(id: number): Promise<void> {
    const response = await fetch(`${config.apiUrl}/task/${id}`, {
      method: 'DELETE',
    });
    if (!response.ok) {
      throw new Error(`Failed to delete task with ID ${id}: ${response.statusText}`);
    }
  },
};

// import axios from 'axios';
// import { Task, TaskFormData } from '../types/Task';
// import config from '../config';

// // const API_URL = 'http://localhost:3000/api';

// export const taskApi = {
//   // Get all tasks
//   async getAll(): Promise<Task[]> {
//     const response = await axios.get(`${config.apiUrl}/task`);
//     return response.data;
//   },

//   // Get a task by ID
//   async getById(id: number): Promise<Task> {
//     const response = await axios.get(`${config.apiUrl}/task/${id}`);
//     return response.data;
//   },

//   // Create a new task
//   async create(task: TaskFormData): Promise<Task> {
//     const response = await axios.post(`${config.apiUrl}/task`, task);
//     return response.data;
//   },

//   // Update a task
//   async update(id: number, task: Partial<TaskFormData>): Promise<Task> {
//     const response = await axios.put(`${config.apiUrl}/task/${id}`, task);
//     return response.data;
//   },

//   // Delete a task
//   async delete(id: number): Promise<void> {
//     await axios.delete(`${config.apiUrl}/task/${id}`);
//   }
// };
```

### src/api/taskGraphQL.tsx (For GraphQL)
``` jsx
import { Task, TaskFormData } from '../types/Task';
import config from '../config';

// Helper function to convert between UI status strings and GraphQL enum values
const convertStatus = {
  // Convert UI status string to GraphQL enum value string
  toGraphQL: (status: string | undefined): string | undefined => {
    if (!status) return undefined;
    switch (status) {
      case 'To Do': return 'TODO';
      case 'In Progress': return 'IN_PROGRESS';
      case 'Done': return 'DONE';
      default: return status; // fallback
    }
  },

  // No conversion needed for response data since our GraphQL schema
  // already returns the correct string values via the enum's value property
  fromGraphQL: (task: any): any => task // Just pass through as is
};

export const taskApi = {
  // Helper function to make GraphQL requests
  async graphqlRequest(query: string, variables: Record<string, any> = {}): Promise<any> {
    const response = await fetch(`${config.apiUrl}/task`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query, variables }),
    });

    if (!response.ok) {
      throw new Error(`GraphQL request failed: ${response.statusText}`);
    }

    const responseData = await response.json();
    if (responseData.errors) {
      throw new Error(`GraphQL errors: ${JSON.stringify(responseData.errors)}`);
    }

    return responseData.data;
  },

  // Get all tasks
  async getAll(): Promise<Task[]> {
    const query = `
      query GetAllTasks {
        tasks {
          id
          title
          description
          status
          createdAt
          updatedAt
        }
      }
    `;
    const data = await this.graphqlRequest(query);
    return data.tasks;
  },

  // Get a task by ID
  async getById(id: number): Promise<Task> {
    const query = `
      query GetTask($id: ID!) {
        task(id: $id) {
          id
          title
          description
          status
          createdAt
          updatedAt
        }
      }
    `;
    const variables = { id };
    const data = await this.graphqlRequest(query, variables);
    return data.task;
  },

  // Create a new task
  async create(task: TaskFormData): Promise<Task> {
    const query = `
      mutation CreateTask($title: String!, $description: String, $status: TaskStatus) {
        createTask(title: $title, description: $description, status: $status) {
          id
          title
          description
          status
          createdAt
          updatedAt
        }
      }
    `;
    const variables = {
      title: task.title,
      description: task.description,
      status: convertStatus.toGraphQL(task.status),
    };
    const data = await this.graphqlRequest(query, variables);
    return data.createTask;
  },

  // Update a task
  async update(id: number, task: Partial<TaskFormData>): Promise<Task> {
    const query = `
      mutation UpdateTask($id: ID!, $title: String, $description: String, $status: TaskStatus) {
        updateTask(id: $id, title: $title, description: $description, status: $status) {
          id
          title
          description
          status
          createdAt
          updatedAt
        }
      }
    `;
    const variables = {
      id,
      title: task.title,
      description: task.description,
      status: convertStatus.toGraphQL(task.status),
    };
    const data = await this.graphqlRequest(query, variables);
    return data.updateTask;
  },

  // Delete a task
  async delete(id: number): Promise<void> {
    const query = `
      mutation DeleteTask($id: ID!) {
        deleteTask(id: $id) {
          id
        }
      }
    `;
    const variables = { id };
    await this.graphqlRequest(query, variables);
  },
};
```

### src/hooks/useTasks.tsx
``` jsx
import { useState, useEffect, useCallback } from 'react';
import { Task, TaskFormData, normalizeTask } from '../types/Task';
// import { taskApi } from '../api/taskRestAPI';

import config from '../config';
import { taskApi as graphqlTaskApi } from '../api/taskGraphQL';
import { taskApi as restTaskApi } from '../api/taskRestAPI';

// Use the appropriate API based on the config
const taskApi = config.apiType === 'graphql' ? graphqlTaskApi : restTaskApi;

export const useTasks = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [error, setError] = useState<string | null>(null);

  // Fetch all tasks
  const fetchTasks = useCallback(async () => {
    try {
      const data = await taskApi.getAll();
      // Transform _id to id in each task
      const normalizedData = data.map((task: Task) => normalizeTask(task));
      // If you don't use MongoDB, you can skip the normalization step
      // setTasks(data);``
      setTasks(normalizedData);
      setError(null);
    } catch (err) {
      setError('Failed to fetch tasks');
      console.error(err);
    }
  }, []);

  // Create a new task
  const createTask = async (taskData: TaskFormData): Promise<Task> => {
    try {
      const newTask = await taskApi.create(taskData);
      setTasks(prev => [...prev, newTask]);
      return newTask;
    } catch (err) {
      setError('Failed to create task');
      throw err;
    }
  };

  // Update a task
  const updateTask = async (id: number, taskData: Partial<TaskFormData>): Promise<Task> => {
    try {
      const updatedTask = await taskApi.update(id, taskData);
      setTasks(prev => prev.map(task => task.id === id ? updatedTask : task));
      return updatedTask;
    } catch (err) {
      setError('Failed to update task');
      throw err;
    }
  };

  // Delete a task
  const deleteTask = async (id: number): Promise<void> => {
    try {
      await taskApi.delete(id);
      setTasks(prev => prev.filter(task => task.id !== id));
    } catch (err) {
      setError('Failed to delete task');
      throw err;
    }
  };

  // Load tasks on component mount
  useEffect(() => {
    fetchTasks();
  }, [fetchTasks]);

  return {
    tasks,
    error,
    fetchTasks,
    createTask,
    updateTask,
    deleteTask
  };
};
```

### src/pages/Home.tsx
``` jsx
import { useState } from 'react';
import { useTasks } from '../hooks/useTasks';
import { Task, TaskStatus } from '../types/Task';

const Home = () => {
  const { tasks, error, fetchTasks, createTask, updateTask, deleteTask } = useTasks();
  const [editingId, setEditingId] = useState<number | null>(null);
  // For Create and Updating task
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [status, setStatus] = useState<'To Do' | 'In Progress' | 'Done'>('To Do');

  const [openList, setOpenList] = useState(true);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const data = { title, description, status };
    
    try {
      if (editingId) {
        await updateTask(editingId, data);
        setEditingId(null);
      } else {
        await createTask(data);
      }
      resetForm();
    } catch (err) {
      console.error('Error:', err);
    }
  };

  const startEdit = (task: Task) => {
    setEditingId(task.id!);
    setTitle(task.title);
    setDescription(task.description);
    setStatus(task.status);
  };

  const resetForm = () => {
    setEditingId(null);
    setTitle('');
    setDescription('');
    setStatus('To Do');
  };

  const toggleList = () => {
    setOpenList(!openList);
  }

  return (
    <div className="container">
      <h1>Task Manager</h1>
      
      {error && <div className="error-message">{error}</div>}

      {/* Simple Form */}
      <div className="card">
        <h2>{editingId ? 'Edit Task' : 'Create Task'}</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <input
              type="text"
              placeholder="Task Title"
              value={title}
              onChange={e => setTitle(e.target.value)}
              required
            />
          </div>
          
          <div className="form-group">
            <textarea
              placeholder="Description"
              value={description}
              onChange={e => setDescription(e.target.value)}
            />
          </div>
          
          <div className="form-group">
            <select
              value={status}
              onChange={e => setStatus(e.target.value as TaskStatus)} // Default String
            >
              <option value="To Do">To Do</option>
              <option value="In Progress">In Progress</option>
              <option value="Done">Done</option>
            </select>
          </div>
          
          <div className="button-group">
            {editingId && (
              <button type="button" onClick={resetForm}>
                Cancel
              </button>
            )}
            <button type="submit">
              {editingId ? 'Update' : 'Create'}
            </button>
          </div>
        </form>
      </div>

      {/* Task List */}
      <button className="toggle-list" onClick={toggleList}>
        {openList ? 'Hide Task List' : 'Show Task List'}
      </button>

      <button className="toggle-list" onClick={fetchTasks}>
        Refresh
      </button>
      {openList && (
      <div className="card">
        <h2>Task List</h2>
        <table className="task-table">
          <thead>
            <tr>
              <th>Title</th>
              <th>Description</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {tasks.map(task => (
              <tr key={task.id} className="task-row">
                <td>{task.title}</td>
                <td>{task.description}</td>
                <td>{task.status}</td>
                <td>
                  <button onClick={() => startEdit(task)}>Edit</button>
                  <button onClick={() => deleteTask(task.id!)}>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      )}
    </div>    
  );
};

export default Home;
```

### src/pages/About.tsx
``` jsx
function About() {
    return (
      <div>
        <h1>About Page</h1>
        <p>This is the About page.</p>
      </div>
    );
  }
  
export default About;
```

## Angular

### Create
```bash
# Install and verify
npm install -g @angular/cli
ng version

# Create a new Angular project
ng new angular-front
```

### Run
```bash
ng serve 
# or
npm start
```

### Add Components / Services
```bash
# Add Components
ng generate component components/task-list

# Add Services
ng generate service services/task
```

### Building for Production
``` bash
ng build --prod
```



## Node.js

### Features

- Create, Read, Update, and Delete (CRUD) operations for tasks
- RESTful API / GraphQL design
- Automatic database creation and setup
- Minimal dependencies

### Task Model

Each task includes:
- **Title**: Short text describing the task
- **Description**: Longer text with details
- **Status**: One of "To Do", "In Progress", or "Done"

### Prerequisites

- Node.js (by default)
- MySQL (by default)
- or MongoDB
- or JSON

## Init
``` bash
# This is important for `npm start`
npm init -y

# Make sure you have 
"scripts": {
    "start": "node app.js",
    "dev": "nodemon app.js"
  },
# in your package.json
```

### Installation

1. Install dependencies:
    ``` bash
    npm install

    # If without package.json
    npm install dotenv express cors
    ```

2. Configure the database:
   - Open `.env.example`
   - Modify the Database connection settings (username, password, host) to match your environment
   - Choose your database type `DB_TYPE` ("json", "mysql", "mongodb"), api type `API_TYPE` ("restapi", "graphql")
   - Rename filename of `.env.example` into `.env`

3. Start the server:
    ```bash
    npm start
    ```

The server will automatically create the database if it doesn't exist and set up the required tables.


### Dependencies
```bash
npm install express mysql2 sequelize dotenv cors mongoose
```
- Express.js: Web framework
- MySQL2: MySQL database driver
- Sequelize: ORM for MySQL database interactions
- Mongoose: ORM for MongoDB interactions
- Express-GraphQL: Create GraphQL API
- Dotenv: Configuration management
- Cors: For cross-origin resource sharing (CORS)


### Project Structure
``` bash
task-manager/
├── app.js              # Main application entry point
├── config/
│   └── config.js       # Database configuration
├── models/
│   └── index.js        # Database models and connection
├── routes/
│   └── tasks.js        # API routes for tasks
├── .env                # Project enviornment
├── package.json        # Project dependencies
└── README.md           # Project documentation
```


### .env
``` bash
# Server configuration
PORT=3000
NODE_ENV=development

# Database configuration
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=abc123
DB_NAME=task_manager
DB_DIALECT=mysql

# MongoDB configuration
MONGODB_URI=mongodb://localhost:27017/task_manager

# Type Configuration
# Select "mysql" or "json" or "mongodb"
DB_TYPE = json
# Select "restapi" or "graphql"
API_TYPE = restapi
```

### app.js
``` js
// Configure Backend
require('dotenv').config();
const DB_TYPE = process.env.DB_TYPE || 'json';
const API_TYPE = process.env.API_TYPE || 'restapi';
const PORT = process.env.PORT || 3000;
const { syncDatabase } = require(`./models/index-${DB_TYPE}`);
const taskRoutes = require(`./routes/tasks-${API_TYPE}`);

// Import express and cors
const express = require('express');
const cors = require('cors');

// Create App
const app = express();
// CORS Middleware
app.use(cors());
// Middleware
app.use(express.json());
// Routes
app.use('/api/task', taskRoutes);

// Sync database and start server
syncDatabase()
  .then(() => {
    app.listen(PORT, () => {
      console.log(`=========Server running on port ${PORT}=========`);
      console.log(`=======Server running with ${DB_TYPE} and ${API_TYPE}========`);
    });
  })
  .catch(err => {
    console.error('Failed to start server:', err);
    process.exit(1);
  });


// If not using '=>'
// syncDatabase()
//   .then(function() {
//     app.listen(PORT, function() {
//       console.log('Server running on port ' + PORT);
//     });
//   })
//   .catch(function(err) {
//     console.error('Failed to start server:', err);
//     process.exit(1);
//   });

// It can also be done using async/await
// async function startServer() {
//   try {
//     await syncDatabase();
//     app.listen(PORT, () => {
//       console.log(`Server running on port ${PORT}`);
//     });
//   } catch (err) {
//     console.error('Failed to start server:', err);
//     process.exit(1);
//   }
// }

// startServer();
```

### config/config.js
``` js
require('dotenv').config();

const config = {
    development: {
      username: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      database: process.env.DB_NAME,
      host: process.env.DB_HOST,
      dialect: process.env.DB_DIALECT
    }
  };
  
module.exports = config;
```

### routes.tasks-restapi.js
``` js
const express = require('express');
const router = express.Router();

// Import the Task model based on the DB_TYPE
require('dotenv').config();
const DB_TYPE = process.env.DB_TYPE || 'json';
const { Task } = require(`../models/index-${DB_TYPE}`);

// GET all tasks
router.get('/', async (req, res) => {
  try {
    const tasks = await Task.findAll();
    res.json(tasks);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// GET task by ID
router.get('/:id', async (req, res) => {
  try {
    const task = await Task.findByPk(req.params.id);
    if (!task) {
      return res.status(404).json({ message: 'Task not found' });
    }
    res.json(task);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// CREATE new task
router.post('/', async (req, res) => {
  try {
    const { title, description, status } = req.body;
    
    if (!title) {
      return res.status(400).json({ message: 'Title is required' });
    }
    
    const newTask = await Task.create({
      title,
      description,
      status: status || 'To Do'
    });
    
    res.status(201).json(newTask);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// UPDATE task
router.put('/:id', async (req, res) => {
  try {
    const { title, description, status } = req.body;
    const task = await Task.findByPk(req.params.id);
    
    if (!task) {
      return res.status(404).json({ message: 'Task not found' });
    }
    
    const updatedTask = await task.update({
      title: title || task.title,
      description: description !== undefined ? description : task.description,
      status: status || task.status
    });
    
    res.json(updatedTask);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// DELETE task
router.delete('/:id', async (req, res) => {
  try {
    const task = await Task.findByPk(req.params.id);
    
    if (!task) {
      return res.status(404).json({ message: 'Task not found' });
    }
    
    await task.destroy();
    res.json({ message: 'Task deleted successfully' });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

module.exports = router;
```

### routes/tasks-restapi.js (For RestAPI)
``` js
const express = require('express');
const router = express.Router();

// Import the Task model based on the DB_TYPE
require('dotenv').config();
const DB_TYPE = process.env.DB_TYPE || 'json';
const { Task } = require(`../models/index-${DB_TYPE}`);

// GET all tasks
router.get('/', async (req, res) => {
  try {
    const tasks = await Task.findAll();
    res.json(tasks);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// GET task by ID
router.get('/:id', async (req, res) => {
  try {
    const task = await Task.findByPk(req.params.id);
    if (!task) {
      return res.status(404).json({ message: 'Task not found' });
    }
    res.json(task);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// CREATE new task
router.post('/', async (req, res) => {
  try {
    const { title, description, status } = req.body;
    
    if (!title) {
      return res.status(400).json({ message: 'Title is required' });
    }
    
    const newTask = await Task.create({
      title,
      description,
      status: status || 'To Do'
    });
    
    res.status(201).json(newTask);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// UPDATE task
router.put('/:id', async (req, res) => {
  try {
    const { title, description, status } = req.body;
    const task = await Task.findByPk(req.params.id);
    
    if (!task) {
      return res.status(404).json({ message: 'Task not found' });
    }
    
    const updatedTask = await task.update({
      title: title || task.title,
      description: description !== undefined ? description : task.description,
      status: status || task.status
    });
    
    res.json(updatedTask);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// DELETE task
router.delete('/:id', async (req, res) => {
  try {
    const task = await Task.findByPk(req.params.id);
    
    if (!task) {
      return res.status(404).json({ message: 'Task not found' });
    }
    
    await task.destroy();
    res.json({ message: 'Task deleted successfully' });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

module.exports = router;
```

### routes/tasks-graphql.js (For GraphQL)
``` js
// routes/tasks.js - Main router file
const express = require('express');
const router = express.Router();
const { graphqlHTTP } = require('express-graphql');
const schema = require('./graphql/schema');

// Set up GraphQL endpoint
router.use('/', graphqlHTTP({
  schema,
  graphiql: true
}));

module.exports = router;
```

### routes/graphql/schema.js (For GraphQL)
``` js
// routes/graphql/schema.js - Schema definition combining types, queries and mutations
const { 
    GraphQLSchema, 
    GraphQLObjectType, 
    GraphQLString, 
    GraphQLList, 
    GraphQLNonNull, 
    GraphQLID,
    GraphQLEnumType
  } = require('graphql');

  // Load environment variables and database model
  require('dotenv').config();
  const DB_TYPE = process.env.DB_TYPE || 'json';
  const { Task } = require(`../../models/index-${DB_TYPE}`);
  
  // Define GraphQL types
  const StatusEnum = new GraphQLEnumType({
    name: 'TaskStatus',
    values: {
      TODO: { value: 'To Do' },
      IN_PROGRESS: { value: 'In Progress' },
      DONE: { value: 'Done' }
    }
  });
  
  const TaskType = new GraphQLObjectType({
    name: 'Task',
    fields: () => ({
      id: { type: GraphQLNonNull(GraphQLID) },
      title: { type: GraphQLNonNull(GraphQLString) },
      description: { type: GraphQLString },
      status: { type: StatusEnum },
      createdAt: { type: GraphQLString },
      updatedAt: { type: GraphQLString }
    })
  });
  
  // Root Query
  const RootQueryType = new GraphQLObjectType({
    name: 'Query',
    fields: () => ({
      task: {
        type: TaskType,
        args: { id: { type: GraphQLNonNull(GraphQLID) } },
        resolve: async (_, args) => await Task.findByPk(args.id)
      },
      tasks: {
        type: new GraphQLList(TaskType),
        resolve: async () => await Task.findAll()
      }
    })
  });
  
  // Root Mutation
  const RootMutationType = new GraphQLObjectType({
    name: 'Mutation',
    fields: () => ({
      createTask: {
        type: TaskType,
        args: {
          title: { type: GraphQLNonNull(GraphQLString) },
          description: { type: GraphQLString },
          status: { type: StatusEnum }
        },
        resolve: async (_, args) => {
          return await Task.create({
            title: args.title,
            description: args.description,
            status: args.status || 'To Do'
          });
        }
      },
      updateTask: {
        type: TaskType,
        args: {
          id: { type: GraphQLNonNull(GraphQLID) },
          title: { type: GraphQLString },
          description: { type: GraphQLString },
          status: { type: StatusEnum }
        },
        resolve: async (_, args) => {
          const task = await Task.findByPk(args.id);
          if (!task) throw new Error('Task not found');
          
          return await task.update({
            title: args.title || task.title,
            description: args.description !== undefined ? args.description : task.description,
            status: args.status || task.status
          });
        }
      },
      deleteTask: {
        type: TaskType,
        args: { id: { type: GraphQLNonNull(GraphQLID) } },
        resolve: async (_, args) => {
          const task = await Task.findByPk(args.id);
          if (!task) throw new Error('Task not found');
          
          const deletedTask = { ...task.dataValues };
          await task.destroy();
          return deletedTask;
        }
      }
    })
  });
  
  // Create and export schema
  const schema = new GraphQLSchema({
    query: RootQueryType,
    mutation: RootMutationType
  });
  
  module.exports = schema;
```

### models/index-json.js (For JSON Database)
``` js
const fs = require('fs').promises;
const path = require('path');

// Data file path
const dataPath = path.join(__dirname, '../data/tasks.json');

// Read tasks data
async function readTasks() {
  try {
    const data = await fs.readFile(dataPath, 'utf8');
    return JSON.parse(data);
  } catch (error) {
    // Return empty array if file doesn't exist
    if (error.code === 'ENOENT') {
      return [];
    }
    throw error;
  }
}

// Write tasks data
async function writeTasks(tasks) {
  await fs.writeFile(dataPath, JSON.stringify(tasks, null, 2));
}

// Task model
const Task = {
  // Find all tasks
  findAll: async () => {
    const tasks = await readTasks();
    return tasks.map(task => Task.attachMethods(task));
  },

  // Find task by ID
  findByPk: async (id) => {
    const tasks = await readTasks();
    const task = tasks.find(task => task.id === parseInt(id));
    return task ? Task.attachMethods(task) : null;
  },

  // Create new task
  create: async (taskData) => {
    const tasks = await readTasks();
    const newId = tasks.length > 0 ? Math.max(...tasks.map(t => t.id)) + 1 : 1;
    
    const newTask = {
      id: newId,
      title: taskData.title,
      description: taskData.description || null,
      status: taskData.status || 'To Do',
      // createdAt: new Date(),
      // updatedAt: new Date()
    };
    
    tasks.push(newTask);
    await writeTasks(tasks);
    return Task.attachMethods(newTask);
  },

  // Attach methods to task object
  attachMethods: (taskData) => {
    return {
      ...taskData,
      // Update task
      update: async (updateData) => {
        const tasks = await readTasks();
        const index = tasks.findIndex(t => t.id === taskData.id);
        
        if (index === -1) throw new Error('Task not found');
        
        const updatedTask = {
          ...tasks[index],
          ...updateData,
          // updatedAt: new Date()
        };
        
        tasks[index] = updatedTask;
        await writeTasks(tasks);
        return Task.attachMethods(updatedTask);
      },

      // Delete task
      destroy: async () => {
        const tasks = await readTasks();
        const filteredTasks = tasks.filter(t => t.id !== taskData.id);
        
        if (filteredTasks.length === tasks.length) {
          throw new Error('Task not found');
        }
        
        await writeTasks(filteredTasks);
        return true;
      }
    };
  }
};

// Initialize data storage
async function syncDatabase() {
  try {
    // Ensure directory exists
    await fs.mkdir(path.dirname(dataPath), { recursive: true });
    
    // Ensure file exists
    try {
      await fs.access(dataPath);
    } catch (error) {
      if (error.code === 'ENOENT') {
        await writeTasks([]);
      } else {
        throw error;
      }
    }
    
    console.log('Database synchronized');
  } catch (error) {
    console.error('Error syncing database:', error);
    throw error;
  }
}

module.exports = { Task, syncDatabase };
```

### models/index-mysql.js (For MySQL)
``` js
const { Sequelize, DataTypes } = require('sequelize');
const mysql = require('mysql2/promise');
require('dotenv').config();

// const config = require('../config/config');
// config.DB_HOST

// Function to create database if it doesn't exist
const createDatabaseIfNotExists = async () => {
  try {
    // Create a connection without specifying a database
    const connection = await mysql.createConnection({
      host: process.env.DB_HOST,
      user: process.env.DB_USER,
      password: process.env.DB_PASSWORD
    });
    
    // Create the database if it doesn't exist
    await connection.query(`CREATE DATABASE IF NOT EXISTS ${process.env.DB_NAME}`);
    console.log(`Database ${process.env.DB_NAME} created or already exists`);
    
    // Close the connection
    await connection.end();
  } catch (error) {
    console.error('Error creating database:', error);
    throw error;
  }
};

// Create Sequelize instance
const sequelize = new Sequelize(
  process.env.DB_NAME,
  process.env.DB_USER,
  process.env.DB_PASSWORD,
  {
    host: process.env.DB_HOST,
    dialect: process.env.DB_DIALECT
  }
);

// Define Task model
// Datatypes: DataTypes.STRING, DataTypes.BOOLEAN, DataTypes.INTEGER, DataTypes.FLOAT, DataTypes.DATE
const Task = sequelize.define('Task', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  title: {
    type: DataTypes.STRING,
    allowNull: false
  },
  description: {
    type: DataTypes.TEXT
  },
  status: {
    type: DataTypes.ENUM('To Do', 'In Progress', 'Done'),
    defaultValue: 'To Do'
  },
  // createdAt: {
  //   type: DataTypes.DATE,
  //   defaultValue: DataTypes.NOW,
  //   allowNull: false
  // },
  // updatedAt: {
  //   type: DataTypes.DATE,
  //   defaultValue: DataTypes.NOW,
  //   allowNull: false
  // }
}, {
  timestamps: false // createdAt, updatedAt
});

// Sync database
const syncDatabase = async () => {
  try {
    // First create database if needed
    await createDatabaseIfNotExists();
    
    // Then sync models with database
    await sequelize.sync();
    console.log('Database synchronized successfully');
  } catch (error) {
    console.error('Error synchronizing database:', error);
    throw error;
  }
};

module.exports = { sequelize, Task, syncDatabase };

// Equals to
// module.exports.sequelize = sequelize;
// module.exports.Task = Task;
// module.exports.syncDatabase = syncDatabase;


// Below will lead to module.exports = syncDatabase;
// module.exports = sequelize, Task, syncDatabase;
```

### models/index-mongodb.js (For MongoDB)
``` js
const mongoose = require('mongoose');
require('dotenv').config();

// Connect to Database
const syncDatabase = async () => {
  try {
    await mongoose.connect(process.env.MONGODB_URI);
    console.log(`Connected to MongoDB successfully`);
  } catch (error) {
    console.error('Error connecting to database:', error);
    throw error;
  }
};

// Task Schema & Model
// type: Number, Date, Boolean
const Task = mongoose.model('Task', new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String, default: '' },
  status: {
    type: String,
    enum: ['To Do', 'In Progress', 'Done'],
    default: 'To Do'
  }
}, 
// CreatedAt, UpdatedAt
{ 
  // // CreatedAt, UpdatedAt
  // timestamps: true,
  // This disables the __v field
  // versionKey: false,
}
));

// Sequelize-compatible API methods
Task.findAll = async () => Task.find().sort({ _id: -1 });
// Task.findAll = async function() {
//   return await Task.find().sort({ id: -1 });
// };
Task.findByPk = async (id) => Task.findById(id);
// Task.findByPk = async function(id) {
//   return await Task.findById(id);
// };
Task.prototype.update = async function(data) {
  Object.assign(this, data);
  return this.save();
};
Task.prototype.destroy = async function() {
  return this.deleteOne();
};

module.exports = { mongoose, Task, syncDatabase };
```

### data/tasks.json (For JSON database)
``` json
[
  {
    "id": 1,
    "title": "Task 1",
    "description": "Save the world",
    "status": "To Do"
  },
  {
    "id": 2,
    "title": "Task 2",
    "description": "Get a job",
    "status": "Done"
  },
  {
    "id": 3,
    "title": "Mission 1",
    "description": "Get better job",
    "status": "In Progress"
  },
  {
    "id": 4,
    "title": "Mission 2",
    "description": "JSON Database",
    "status": "To Do"
  }
]
```

## Dotnet

### Init
``` bash
# dotnet webapi
mkdir dotnet-back
cd dotnet-back
dotnet new webapi

# add packages
dotnet add package Microsoft.EntityFrameworkCore
dotnet add package Microsoft.EntityFrameworkCore.Relational

# add package for InMemoryDatabase
dotnet add package Microsoft.EntityFrameworkCore.InMemory

# add package for MySQL
dotnet add package Pomelo.EntityFrameworkCore.MySql

# add package for MongoDB
dotnet add package MongoDB.Driver
```

### Run
``` bash
dotnet run
```

### appsettings.json
``` json
{
  "TaskFilePath": "data/tasks.json",
  "ConnectionStrings": {
    "MySQLConnection": "server=localhost;user=root;password=abc123;database=task_manager"
  },


  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
```

### Notice
``` bash
# Remember to modify your port in `Properties/launchSettings.json`
 "applicationUrl": "http://localhost:3000",
```

### Project Structure
``` bash
task-manager/
├── Controllers/
│   └── TaskController.cs    # API Route Controller
├── Models/
│   ├── TaskDBContext.cs     # DB Context for datbase and table
│   ├── TaskDTO.cs           # Task Entity DTO
│   └── TaskEntity.cs        # Task Entity
├── Services/
│   └── TaskService.cs       # Task Service
├── appsettings.json         # Project enviornment
└── Program.cs               # Main Entry
```

### Program.cs
``` cs
using Microsoft.EntityFrameworkCore;
using TaskManager.Api.Models;
using TaskManager.Api.Services;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// e.g. public class TasksController : ControllerBase
// e.g. public class TasksController : Controller
builder.Services.AddControllers();

// Register task service
// This means that within the same HTTP request, the same TaskService instance will be used.
builder.Services.AddScoped<TaskService>();

// Add MonogoDB Context (Don't forget using MongoDB.Driver)
// using MongoDB.Driver;
// builder.Services.AddSingleton<IMongoClient>(new MongoClient("mongodb://localhost:27017"));

// Add MySQL database context
// var connectionString = builder.Configuration.GetConnectionString("MySQLConnection");
// builder.Services.AddDbContext<TaskDBContext>(options =>
//     options.UseMySql(connectionString, ServerVersion.AutoDetect(connectionString)));

// Add In-memory database context
// dotnet add package Microsoft.EntityFrameworkCore.InMemory
// builder.Services.AddDbContext<TaskDBContext>(options =>
//     options.UseInMemoryDatabase("TaskDB"));


// Add CORS support
builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyHeader()
              .AllowAnyMethod();
    });
});

var app = builder.Build();

// Create database if it doesn't exist (For MySQL and In-memory database only)
// using (var scope = app.Services.CreateScope())
// {
//     var services = scope.ServiceProvider;
//     var context = services.GetRequiredService<TaskDBContext>();
//     context.Database.EnsureCreated();
// }

// Redirect Http to https (optional)
// app.UseHttpsRedirection();

// Cors
app.UseCors();

app.MapControllers();

app.Run();
```

### Controllers/TaskController.cs (For JSON, InMemory, MySQL Database)
``` cs
using Microsoft.AspNetCore.Mvc;
using TaskManager.Api.Models;
using TaskManager.Api.Services;

namespace TaskManager.Api.Controllers
{
    // will be 'api/Tasks': because the class name TasksController
    [Route("api/[controller]")]
    [ApiController]
    public class TaskController : ControllerBase
    {
        private readonly TaskService _taskService;

        public TaskController(TaskService taskService)
        {
            _taskService = taskService;
        }

        // GET: api/Tasks
        // Task<ActionResult<IEnumerable<TaskEntity>>>
        [HttpGet]
        public async Task<IActionResult> GetTasks()
        {
            var tasks = await _taskService.GetAllTasksAsync();
            return Ok(tasks);
        }

        // GET: api/Tasks/5
        // Task<ActionResult<TaskEntity>> 
        [HttpGet("{id}")]
        public async Task<IActionResult> GetTask(int id)
        {
            var task = await _taskService.GetTaskByIdAsync(id);

            if (task == null)
            {
                return NotFound();
            }

            return Ok(task);
        }

        // POST: api/Tasks
        [HttpPost]
        public async Task<IActionResult> CreateTask(CreateTaskDto taskDto)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            var task = await _taskService.CreateTaskAsync(taskDto);

            return CreatedAtAction(nameof(GetTask), new { id = task.Id }, task);
        }

        // PUT: api/Tasks/5
        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateTask(int id, UpdateTaskDto taskDto)
        {
            var task = await _taskService.UpdateTaskAsync(id, taskDto);

            if (task == null)
            {
                return NotFound();
            }

            return Ok(task);
        }

        // DELETE: api/Tasks/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteTask(int id)
        {
            var result = await _taskService.DeleteTaskAsync(id);

            if (!result)
            {
                return NotFound();
            }

            return NoContent();
        }
    }
}
```

### Controllers/TaskController.cs (For MongoDB-Only)
``` cs
using Microsoft.AspNetCore.Mvc;
using TaskManager.Api.Models;
using TaskManager.Api.Services;

namespace TaskManager.Api.Controllers
{
    // will be 'api/Tasks': because the class name TasksController
    [Route("api/[controller]")]
    [ApiController]
    public class TaskController : ControllerBase
    {
        private readonly TaskService _taskService;
        public TaskController(TaskService taskService)
        {
            _taskService = taskService;
        }

        // GET: api/Tasks
        [HttpGet]
        public async Task<IActionResult> GetTasks()
        {
            var tasks = await _taskService.GetAllTasksAsync();
            return Ok(tasks);
        }

        // GET: api/Tasks/5
        [HttpGet("{id}")]
        public async Task<IActionResult> GetTask(String id)
        {
            var task = await _taskService.GetTaskByIdAsync(id);

            if (task == null)
            {
                return NotFound();
            }

            return Ok(task);
        }

        // POST: api/Tasks
        [HttpPost]
        public async Task<IActionResult> CreateTask(CreateTaskDto taskDto)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            var task = await _taskService.CreateTaskAsync(taskDto);

            return CreatedAtAction(nameof(GetTask), new { id = task.Id }, task);
        }

        // PUT: api/Tasks/5
        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateTask(String id, UpdateTaskDto taskDto)
        {
            var task = await _taskService.UpdateTaskAsync(id, taskDto);

            if (task == null)
            {
                return NotFound();
            }

            return Ok(task);
        }

        // DELETE: api/Tasks/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteTask(String id)
        {
            var result = await _taskService.DeleteTaskAsync(id);

            if (!result)
            {
                return NotFound();
            }

            return NoContent();
        }
    }
}
```

### Models/TaskDBContext.cs (For JSON, In-Memory, and MySQL Database)
``` cs
using Microsoft.EntityFrameworkCore;

namespace TaskManager.Api.Models
{
    public class TaskDBContext : DbContext
    {
        public TaskDBContext(DbContextOptions<TaskDBContext> options) : base(options)
        {
        }

        public DbSet<TaskEntity> Tasks { get; set; } = null!;
    }
}
```

### Models/TaskDTO.cs
``` cs
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace TaskManager.Api.Models
{
    public class CreateTaskDto
    {
        [Required]
        public string Title { get; set; } = string.Empty;

        public string Description { get; set; } = string.Empty;

        public string Status { get; set; } = "To Do";
    }

    public class UpdateTaskDto
    {
        public string? Title { get; set; }

        public string? Description { get; set; }

        public string? Status { get; set; }
    }
}
```

### Models/TaskEntity.cs (For JSON, In-Memory, MySQL Database)
``` cs
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema; // No Need for JSON

namespace TaskManager.Api.Models
{
    public class TaskEntity
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]  // No Need for JSON
        public int Id { get; set; }

        [Required]
        public string Title { get; set; } = string.Empty;

        public string Description { get; set; } = string.Empty;

        [Required]
        public string Status { get; set; } = "To Do";

        // [Column(TypeName = "timestamp")]
        // public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

        // [Column(TypeName = "timestamp")]
        // public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;
    }

}
```

### Models/TaskEntity.cs (For MongoDB only)
``` cs
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using System.ComponentModel.DataAnnotations;

namespace TaskManager.Api.Models
{
    public class TaskEntity
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)] 
        public String? Id { get; set; }

        [Required]
        [BsonElement("title")]
        public string Title { get; set; } = string.Empty;

        [BsonElement("description")]
        public string Description { get; set; } = string.Empty;

        [Required]
        [BsonElement("status")]
        public string Status { get; set; } = "To Do";

        [BsonElement("__v")] // Ignore the __v field
        public int Version { get; set; }

        // If you want to re-enable timestamps:
        // [BsonElement("createdAt")]
        // public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

        // [BsonElement("updatedAt")]
        // public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;
    }
}
```

### Services/TaskService.cs (For JSON only)
``` cs
using System.Text.Json;
using Microsoft.Extensions.Configuration;
using TaskManager.Api.Models;

namespace TaskManager.Api.Services
{
    public class TaskService
    {
        private readonly string _filePath;

        public TaskService(IConfiguration configuration)
        {
            _filePath = configuration.GetValue<string>("TaskFilePath") ?? "data/tasks.json";

            if (!File.Exists(_filePath))
            {
                // Ensure _filePath is valid before writing to the file
                Directory.CreateDirectory(Path.GetDirectoryName(_filePath) ?? string.Empty);
                File.WriteAllText(_filePath, "[]");
            }
        }


        public async Task<IEnumerable<TaskEntity>> GetAllTasksAsync()
        {
            var json = await File.ReadAllTextAsync(_filePath);
            return JsonSerializer.Deserialize<List<TaskEntity>>(json) ?? new List<TaskEntity>(); // Ensure non-null return
        }

        public async Task<TaskEntity?> GetTaskByIdAsync(int id)
        {
            var tasks = await GetAllTasksAsync();
            return tasks.FirstOrDefault(t => t.Id == id);
        }

        public async Task<TaskEntity> CreateTaskAsync(CreateTaskDto taskDto)
        {
            var tasks = (await GetAllTasksAsync()).ToList();
            var newTask = new TaskEntity
            {
                Id = tasks.Any() ? tasks.Max(t => t.Id) + 1 : 1, // Generate a new ID
                Title = taskDto.Title,
                Description = taskDto.Description,
                Status = taskDto.Status
            };

            tasks.Add(newTask);
            await SaveTasksAsync(tasks);

            return newTask;
        }

        public async Task<TaskEntity?> UpdateTaskAsync(int id, UpdateTaskDto taskDto)
        {
            var tasks = (await GetAllTasksAsync()).ToList();
            var task = tasks.FirstOrDefault(t => t.Id == id);

            if (task == null)
            {
                return null;
            }

            // Update only properties that are not null
            if (taskDto.Title != null)
            {
                task.Title = taskDto.Title;
            }

            if (taskDto.Description != null)
            {
                task.Description = taskDto.Description;
            }

            if (taskDto.Status != null)
            {
                task.Status = taskDto.Status;
            }

            await SaveTasksAsync(tasks);

            return task;
        }

        public async Task<bool> DeleteTaskAsync(int id)
        {
            var tasks = (await GetAllTasksAsync()).ToList();
            var task = tasks.FirstOrDefault(t => t.Id == id);

            if (task == null)
            {
                return false;
            }

            tasks.Remove(task);
            await SaveTasksAsync(tasks);

            return true;
        }

        private async Task SaveTasksAsync(IEnumerable<TaskEntity> tasks)
        {
            var json = JsonSerializer.Serialize(tasks, new JsonSerializerOptions { WriteIndented = true });
            await File.WriteAllTextAsync(_filePath, json);
        }
    }
}
```

### Task/TaskService.cs (For In-Memory Database only)
``` cs
using Microsoft.EntityFrameworkCore;
using TaskManager.Api.Models;

namespace TaskManager.Api.Services
{
    public class TaskService
    {
        private readonly TaskDBContext _context;

        public TaskService(TaskDBContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<TaskEntity>> GetAllTasksAsync()
        {
            return await _context.Tasks.ToListAsync();
        }

        public async Task<TaskEntity?> GetTaskByIdAsync(int id)
        {
            return await _context.Tasks.FindAsync(id);
        }

        public async Task<TaskEntity> CreateTaskAsync(CreateTaskDto taskDto)
        {
            var task = new TaskEntity
            {
                Title = taskDto.Title,
                Description = taskDto.Description,
                Status = taskDto.Status,
            };

            _context.Tasks.Add(task);
            await _context.SaveChangesAsync();

            return task;
        }

        public async Task<TaskEntity?> UpdateTaskAsync(int id, UpdateTaskDto taskDto)
        {
            var task = await _context.Tasks.FindAsync(id);

            if (task == null)
            {
                return null;
            }

            // Update only properties that are not null
            if (taskDto.Title != null)
            {
                task.Title = taskDto.Title;
            }

            if (taskDto.Description != null)
            {
                task.Description = taskDto.Description;
            }

            if (taskDto.Status != null)
            {
                task.Status = taskDto.Status;
            }

            // task.UpdatedAt = DateTime.UtcNow;

            await _context.SaveChangesAsync();

            return task;
        }

        public async Task<bool> DeleteTaskAsync(int id)
        {
            var task = await _context.Tasks.FindAsync(id);

            if (task == null)
            {
                return false;
            }

            _context.Tasks.Remove(task);
            await _context.SaveChangesAsync();

            return true;
        }
    }
}
```

### Services/TaskService.cs (For MySQL only)
```cs
using Microsoft.EntityFrameworkCore;
using TaskManager.Api.Models;

namespace TaskManager.Api.Services
{
    public class TaskService
    {
        private readonly TaskDBContext _context;

        public TaskService(TaskDBContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<TaskEntity>> GetAllTasksAsync()
        {
            return await _context.Tasks.ToListAsync();
        }

        public async Task<TaskEntity?> GetTaskByIdAsync(int id)
        {
            return await _context.Tasks.FindAsync(id);
        }

        public async Task<TaskEntity> CreateTaskAsync(CreateTaskDto taskDto)
        {
            var task = new TaskEntity
            {
                Title = taskDto.Title,
                Description = taskDto.Description,
                Status = taskDto.Status,
            };

            _context.Tasks.Add(task);
            await _context.SaveChangesAsync();

            return task;
        }

        public async Task<TaskEntity?> UpdateTaskAsync(int id, UpdateTaskDto taskDto)
        {
            var task = await _context.Tasks.FindAsync(id);

            if (task == null)
            {
                return null;
            }

            // Update only properties that are not null
            if (taskDto.Title != null)
            {
                task.Title = taskDto.Title;
            }

            if (taskDto.Description != null)
            {
                task.Description = taskDto.Description;
            }

            if (taskDto.Status != null)
            {
                task.Status = taskDto.Status;
            }

            // task.UpdatedAt = DateTime.UtcNow;

            await _context.SaveChangesAsync();

            return task;
        }

        public async Task<bool> DeleteTaskAsync(int id)
        {
            var task = await _context.Tasks.FindAsync(id);

            if (task == null)
            {
                return false;
            }

            _context.Tasks.Remove(task);
            await _context.SaveChangesAsync();

            return true;
        }
    }
}
```

### Services/TaskService.cs (For MongoDB only)
``` cs
using MongoDB.Driver;
using TaskManager.Api.Models;

namespace TaskManager.Api.Services
{
    public class TaskService
    {
        private readonly IMongoCollection<TaskEntity> _tasks;
        
        public TaskService(IMongoClient mongoClient) 
        {
            var database = mongoClient.GetDatabase("task_manager");
            _tasks = database.GetCollection<TaskEntity>("tasks");
        }

        public async Task<IEnumerable<TaskEntity>> GetAllTasksAsync()
        {
            return await _tasks.Find(_ => true).ToListAsync();
        }

        public async Task<TaskEntity?> GetTaskByIdAsync(string id)
        {
            return await _tasks.Find(t => t.Id == id).FirstOrDefaultAsync();
        }

        public async Task<TaskEntity> CreateTaskAsync(CreateTaskDto taskDto)
        {
            var task = new TaskEntity
            {
                Title = taskDto.Title,
                Description = taskDto.Description,
                Status = taskDto.Status
            };
            
            await _tasks.InsertOneAsync(task);
            return task;
        }

        public async Task<TaskEntity?> UpdateTaskAsync(String id, UpdateTaskDto taskDto)
        {
            // First, find the task
            var task = await _tasks.Find(t => t.Id == id).FirstOrDefaultAsync();
            
            if (task == null)
            {
                return null;
            }

            // Build an update definition
            var updateDefinition = Builders<TaskEntity>.Update.Combine();
            
            if (taskDto.Title != null)
            {
                updateDefinition = updateDefinition.Set(t => t.Title, taskDto.Title);
            }
            
            if (taskDto.Description != null)
            {
                updateDefinition = updateDefinition.Set(t => t.Description, taskDto.Description);
            }
            
            if (taskDto.Status != null)
            {
                updateDefinition = updateDefinition.Set(t => t.Status, taskDto.Status);
            }
            
            // Apply the updates
            await _tasks.UpdateOneAsync(t => t.Id == id, updateDefinition);
            
            // Return the updated task
            return await _tasks.Find(t => t.Id == id).FirstOrDefaultAsync();
        }

        public async Task<bool> DeleteTaskAsync(String id)
        {
            var result = await _tasks.DeleteOneAsync(t => t.Id == id);
            return result.DeletedCount > 0;
        }
    }
}
```

## Django

## Init
```bash
# Install django
pip install django

# Create a new Django project "django_back"
django-admin startproject django_back
# Configure settings.py "ALLOWED_HOSTS = ["*"]"

# Create a new app
cd django_back
python manage.py startapp task
# Configure settings.py "INSTALLED_APPS" for app "task"

# Run initial migrations (Init sqlite database)
python manage.py migrate

# CORS
pip install django-cors-headers
# Configure settings.py "INSTALLED_APPS", "MIDDLEWARE", "CORS_ALLOW_ALL_ORIGINS" for CORS

# For MySQL
# pip install mysqlclient

# For Django: djongo pymongo
# pip install djongo pymongo

# If you finish coding models.py
python manage.py makemigrations
python manage.py migrate
```

## django_back/settings.py
``` py
"""
Django settings for django_back project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5^rg2%97&64gvwjiokp&+#n!=uh@&@9y9_r1r61s8yy28t1o-p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"] #!!!!!!!!!!!!

# Application definition

INSTALLED_APPS = [
    'task', #!!!!!!!!!!!!
    'corsheaders', #!!IMPORTANT: CORS headers for Django (pip install django-cors-headers)
    'rest_framework', #!!IMPORTANT: Django REST framework (pip install djangorestframework)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CORS_ALLOW_ALL_ORIGINS = True #!!IMPORTANT: CORS headers for Django (pip install django-cors-headers)

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', #!!IMPORTANT: CORS headers for Django (pip install django-cors-headers)
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASE_CHOICE = "SQLite" #!!IMPORTANT: Choose your database here. Options: "MySQL", "MongoDB", "SQLite"

if (DATABASE_CHOICE == "MySQL"):
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'task_manager',
        'USER': 'root',
        'PASSWORD': 'abc123',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
elif (DATABASE_CHOICE == "MongoDB"):
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'task_manager',
            'CLIENT': {
                'host': 'mongodb://localhost:27017',
            }
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }




# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### django_back/urls.py
``` py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('task.url')),  # Include the URLs from the task app
]
```

### task/url.py
``` py
from django.urls import path
from . import views

urlpatterns = [
    path('task', views.tasks, name='tasks'),  # Handles GET (list) and POST (create)
    path('task/<int:task_id>', views.task_detail, name='task_detail'),  # Handles GET (retrieve), PUT/PATCH (update), DELETE (delete)
]
```

### task/models.py
``` py
from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20, 
        choices=[('to_do', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')],
        default='to_do'
    )

    def __str__(self):
        return self.title

    class Meta:
         # Explicitly set the table name to 'task'. 
         # If not set, Django will use 'appname_task' as the default table name.
         # "task_task" in this case
        db_table = 'tasks'
```

### task/serializers.py (rest_framework)
``` py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status']
```

### task.views.py (basic)
``` py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import Task

# Handle GET (list) and POST (create) for /tasks/
@csrf_exempt
def tasks(request):
    if request.method == 'GET':
        # List all tasks
        tasks = list(Task.objects.values('id', 'title', 'description', 'status'))
        return JsonResponse(tasks, safe=False)
    elif request.method == 'POST':
        # Create a new task
        try:
            data = json.loads(request.body)
            title = data.get('title')
            description = data.get('description')
            status = data.get('status', 'to_do')

            if not title:
                return JsonResponse({"error": "Title cannot be empty"}, status=400)

            task = Task.objects.create(
                title=title,
                description=description,
                status=status
            )

            return JsonResponse({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "status": task.status
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# Handle GET (retrieve), PUT/PATCH (update), DELETE for /tasks/<task_id>/
@csrf_exempt
def task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)

    if request.method == 'GET':
        # Retrieve a specific task
        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status
        })

    elif request.method in ['PUT', 'PATCH']:
        # Update a specific task
        try:
            data = json.loads(request.body)
            if 'title' in data:
                task.title = data['title']
            if 'description' in data:
                task.description = data['description']
            if 'status' in data:
                task.status = data['status']
            task.save()

            return JsonResponse({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "status": task.status
            })
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    elif request.method == 'DELETE':
        # Delete a specific task
        task.delete()
        return JsonResponse({"message": "Task deleted successfully"}, status=204)

    return JsonResponse({"error": "Method Not Allowed"}, status=405)
```

### task/views.py (rest_framework)
``` py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET', 'POST'])
def tasks(request):
    if request.method == 'GET':
        # List all tasks
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new task
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Invalid JSON data"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def task_detail(request, task_id):
    # Retrieve the task or return 404 if not found
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'GET':
        # Retrieve a specific task
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        # Update a specific task
        serializer = TaskSerializer(task, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": "Invalid JSON data"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete a specific task
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
```