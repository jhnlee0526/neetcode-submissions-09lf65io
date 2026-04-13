class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Graph + DFS
        #   Time: O(E log E), E = total # of emails across all accounts
        #   Space: O(E)
        
        emailIdx = {}   # maps each unique email to a unique integer id (node index in graph)
        emails = []     # reverse mapping so we can convert node index -> email string later
        emailToAcc = {} # maps each email node to the original account index. 
                        # Used to know which name to use for the merged result
        
        # Assign each unique email a unique id
        emailCount = 0
        for accId, a in enumerate(accounts): # index, each account
            for email in a[1:]:  # skip account name
                if email in emailIdx:
                    continue
                
                emailIdx[email] = emailCount
                emails.append(email)
                
                # remember which account this email first appeared in
                emailToAcc[emailCount] = accId
                
                emailCount += 1
        
        # build adjacency list graph
        # each email is a node
        # connect emails that appear in the same account
        adj = [[] for _ in range(emailCount)]
        
        for a in accounts:
            # connect consecutive emails in the same account
            # ex: [John, e1, e2, e3]
            # edges: e1-e2, e2-e3
            for i in range(2, len(a)):
                
                id1 = emailIdx[a[i - 1]]
                id2 = emailIdx[a[i]]
                
                adj[id1].append(id2)
                adj[id2].append(id1)

        # group emails by connected component
        # key   -> account id
        # value -> list of emails belonging to that component
        emailGroup = defaultdict(list)

        # track visited email nodes during DFS
        visited = [False] * emailCount
        
        # DFS explores all connected emails starting from one node
        def dfs(node, accId):
            
            visited[node] = True
            
            # add this email to the current group
            emailGroup[accId].append(emails[node])
            
            # visit all connected emails
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, accId)

        # run DFS for each email node (graph component)
        for i in range(emailCount):
            
            # start DFS only if email not visited yet
            if not visited[i]:
                
                # use original account id for grouping name later
                dfs(i, emailToAcc[i])

        # build final result format
        res = []
        
        for accId in emailGroup:
            
            name = accounts[accId][0]
            
            # sort emails lexicographically as required
            mergedEmails = sorted(emailGroup[accId])
            
            res.append([name] + mergedEmails)

        return res