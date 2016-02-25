/*                           Breadth First Search                            */
/*                                                                           */
/*                         O(|E|) time, O(|V|) space                         */
#include <bits/stdc++.h>
using namespace std;

typedef int id;
typedef int dist_type;
const int parentless = -1;
const int infinity = 1000;

map<id, set<id> > edges;
map<id, dist_type> dist;
map<id, id> parent;

void init(id first, id last) {
   for (id i = first; i <= last; ++i) {
      parent[i] = parentless;
      dist[i] = infinity;
   }
}

// Assumes the global state is init
void bfs(id start, id query) {
   queue<id> q;
   dist[start] = 0;
   q.push(start);

   while (not q.empty()) {
      typedef set<id>::iterator iter;
      id current = q.front(); q.pop();
      set<id> c = edges[current];
      for (iter i = c.begin(); i != c.end(); ++i) {
         id n = *i;
         if (dist[n] == infinity) {
            dist[n] = dist[current] + 1;
            parent[n] = current;
            q.push(n);
         }
      }
   }
}

/*
   number_of_vertices number_of_edges id_start id_target
   edge_0_0 edge_0_1
   edge_1_0 edge_1_1
   ...

   Find shortest path from id_start to id_target
*/
int main() {
   int n, e;
   id s, t;
   cin >> n >> e >> s >> t;
   for (int i = 0; i < e; ++i) {
      id a, b;
      cin >> a >> b;
      edges[a].insert(b);
      edges[b].insert(a);
   }
   init(1, n);
   bfs(s, t);
   cout << dist[t] << endl;
   return 0;
}
