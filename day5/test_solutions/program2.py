#to process 4 queries
N = int(input())
queries = [input().strip() for _ in range(N)]

def queries(queries):
    stack = []
    max_stack = [] 
    
    results = []

    for query in queries:
        parts = query.split()
        operation = int(parts[0])
        
        if operation == 1:
            
            value = int(parts[1])
            stack.append(value)
            
            if max_stack:
                max_stack.append(max(value, max_stack[-1]))
            else:
                max_stack.append(value)
        
        elif operation == 2:
           
            if stack:
                stack.pop()
                max_stack.pop()
        
        elif operation == 3:
            
            if max_stack:
                results.append(max_stack[-1])
    
    return results





results = queries(queries)
for result in results:
    print(result)
