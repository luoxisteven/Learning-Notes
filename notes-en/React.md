# Web

## Reverse Proxy
1) Rounting
    - Mapping the path to your port
2) TLS/HTTPS
    - Decode input and encode output with TLS certificate
3) Load Balancing
    - Reverse proxy can distribute traffic across multiple servers
4) CORES handling
    - Add/modify CORS headers
5) Rate Limiting

## Load Balancing Strategy
```bash
# 1) Least Connections
# Sends each new request to the backend server that currently has the fewest active connections.
upstream app_backend {
  least_conn;
  server 10.0.1.11:8080;
  server 10.0.1.12:8080;
}

# 2) IP Hash
# ip_hash makes NGINX choose backend server based on the client’s IP address.
# for the purpose of the server may have cache or session for this IP address.
# So the same client IP keeps going to the same server:
# ✅ Client IP 1.2.3.4 → always Server A
# ✅ Client IP 5.6.7.8 → always Server B
upstream app_backend {
  ip_hash;
  server 10.0.1.11:8080;
  server 10.0.1.12:8080;
}

# 3) Weighted Servers
# Send more traffic to bigger machines.
upstream app_backend {
  server 10.0.1.11:8080 weight=3;
  server 10.0.1.12:8080 weight=1;
}
```

## TypeScript v.s. JavaScript
- JavaScript = Dynamic, flexible, runs anywhere
- TypeScript = JavaScript + static types + compile-time checks + better tooling
- TypeScript is a superset of JavaScript - all valid JavaScript code is valid TypeScript, but TypeScript adds optional type safety on top.

``` js
// Parameter Definition
let name = "John"
let name: string = "John"

// Function Definition
function add(a, b) {
    return a + b
}
// You can choose whether define the output or not
// But you have to define the type of input
function add(a: number, b: number): number {
    return a + b
}
const add = (a: number, b: number): number => {
    return a + b
}
const add = (a: number, b: number) => a + b
const add = (a: number, b: number): number => a + b
// Bad practice but valid: No types at all (just like JavaScript)
function add(a, b) {
    return a + b 
}

// Interfaces and Type
const user = { name: "John", age: 30 }
interface User {
    name: string
    age: number
}
const user: User = { name: "John", age: 30 }
```

## React

### Class Components v.s. Functional Components
- Class Components（类组件） - 老版
    - 主要使用 React Hooks（如 useState, useEffect）来管理状态和生命周期。
    - 语法简洁，推荐用于大多数情况。
- Functional Components（函数组件）- 旧版
    - 需要继承 React.Component，并使用 this.state 和 this.setState() 来管理状态。

### OnClick
``` html
✅
<button onClick={handleClick}>
❌
<button onClick={handleClick()}>
✅
<button onClick={() => alert('...')}>
❌
<button onClick={alert('...')}>
```

### Arrow function
``` javascript
() => expression
() => 5
() => 2 + 3

const calculateTotal = () => (
    eightYuan * 8 +
    tenYuan * 10 +
    fifteenYuan * 15 +
    twentyYuan * 20 +
    twentyEightYuan * 28 +
    otherAmount
)
```

### useState
- Trigger rendering everytime it updates.
- For State Variable
``` typescript
const [state, setState] = useState(initialState)
```

### useMemo
``` typescript
const cachedValue = useMemo(calculateValue, dependencies)

import { useMemo } from 'react';

function TodoList({ todos, tab, theme }) {
  const visibleTodos = useMemo(() => filterTodos(todos, tab), [todos, tab]);
}

const total = useMemo(() => {
return (
    eightYuan * 8 +
    tenYuan * 10 +
    fifteenYuan * 15 +
    twentyYuan * 20 +
    twentyEightYuan * 28 +
    otherAmount
)
}, [eightYuan, tenYuan, fifteenYuan, twentyYuan, twentyEightYuan, otherAmount])

function calculateTotal(amounts: {
    eightYuan: number,
    tenYuan: number,
    fifteenYuan: number,
    twentyYuan: number,
    twentyEightYuan: number,
    otherAmount: number
}) {
    return (
        amounts.eightYuan * 8 +
        amounts.tenYuan * 10 +
        amounts.fifteenYuan * 15 +
        amounts.twentyYuan * 20 +
        amounts.twentyEightYuan * 28 +
        amounts.otherAmount
    )
}
const total = useMemo(
    () => calculateTotal({eightYuan, tenYuan, fifteenYuan, twentyYuan, twentyEightYuan, otherAmount}),
    [eightYuan, tenYuan, fifteenYuan, twentyYuan, twentyEightYuan, otherAmount]
)
```

### useEffect
The useEffect Hook allows you to perform side effects in your components.
1) Runs on every render
``` JavaScript
useEffect(() => {
  // Runs on every render
});
```

2) Runs only on the first render
``` JavaScript
useEffect(() => {
  //Runs only on the first render
}, []);
```

3) Runs on the first render & any time any dependency value changes
``` JavaScript
useEffect(() => {
  //Runs on the first render
  //And any time any dependency value changes
}, [prop, state]);

useEffect(() => {
  console.log(`count 发生变化: ${count}`);
}, [count]); // 依赖 count，count 变化时执行
```

### useRef
- Persist useRef values between renders.
- 不触发渲染
- 修改 count.current 来改变 useRef 的值
    ``` JavaScript
    import { useRef } from "react";

    function Counter() {
    const count = useRef(0); // 初始化 count.current = 0

    const increment = () => {
        count.current += 1; // ✅ 直接修改 count.current
        console.log("Current count:", count.current); // 但是不会触发重新渲染
    };

    return (
        <div>
        <p>Count: {count.current} (不会更新 UI)</p>
        <button onClick={increment}>Increase</button>
        </div>
    );
    }

    export default Counter;
    ```

### useMediaQuery
``` bash

```

### useMemo
``` bash

```

### How can the parameters bind with each other
``` javascript
function Parent() {
  const [sharedData, setSharedData] = useState(0);
  
  return (
    <>
      <ChildA data={sharedData} setData={setSharedData} />
      <ChildB data={sharedData} setData={setSharedData} />
    </>
  );
}

function ChildA({ data, setData }) {
  return (
    <button onClick={() => setData(data + 1)}>
      Increment: {data}
    </button>
  );
}

function ChildB({ data }) {
  return <p>Value in ChildB: {data}</p>;
}
```