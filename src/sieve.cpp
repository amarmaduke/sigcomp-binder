/*                           Sieve of Eratothenes                            */
/*                                                                           */
/*                     O(n loglog(n)) time, O(n) space                       */
#include <bits/stdc++.h>
using namespace std;

vector<int> primes;

// Assumes primes is empty
void sieve(int n) {
   vector<bool> grid(n, true);

   for (int i = 2; i < floor(sqrt(n) + 1); ++i) {
      if (grid[i]) {
         for (int j = i*i; j < n; j += i) {
            grid[j] = false;
         }
      }
   }

   for (int i = 2; i < n; ++i) {
      if (grid[i])
         primes.push_back(i);
   }
}

int main() {
   sieve(100);
   for (int i = 0; i < primes.size(); ++i) {
      cout << primes[i] << " ";
   }
   cout << endl;
   return 0;
}
