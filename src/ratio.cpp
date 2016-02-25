/*                           Rational Value Type                             */
/*                                                                           */
/*                   Use only if long double doesn't work                    */
#include <bits/stdc++.h>
using namespace std;

struct ratio {
   int n, d;

   ratio() : n(0), d(1) {}
   ratio(int x) : n(x), d(1) {}
   ratio(int x, int y) : n(x), d(y) {
      if (y == 0) assert(false);
   }
};

/* Greater Common Divisor */
int gcd(int n, int m) {
   int r = (n + m) % m;
   while (r != 0) {
      n = m;
      m = r;
      r = (n + m) % m;
   }
   return m;
}

/* Least Common Multiple */
int lcm(int n, int m) {
   int n0 = n, m0 = m;
   int r = (n + m) % m;
   while (r != 0) {
      n = m;
      m = r;
      r = (n + m) % m;
   }
   return (n0 / m) * m0;
}

void canonical(ratio &r) {
   int divisor = gcd(r.n, r.d);
   r.n /= divisor;
   r.d /= divisor;
   if (r.n < 0 and r.d < 0) {
      r.n *= -1; r.d *= -1;
   }
}

ratio operator- (const ratio &r) {
   ratio result(r);
   result.n *= -1;
   canonical(result);
   return result;
}

ratio operator+ (const ratio &a, const ratio &b) {
   ratio result;
   result.n = a.n*b.d + a.d*b.n;
   result.d = a.d*b.d;
   canonical(result);
   return result;
}

ratio operator- (const ratio &a, const ratio &b) {
   return a + (-b);
}

ratio operator* (const ratio &a, const ratio &b) {
   ratio result;
   result.n = a.n*b.n;
   result.d = a.d*b.d;
   canonical(result);
   return result;
}

ratio operator/ (const ratio &a, const ratio &b) {
   ratio temp(b.d, b.n);
   return a * temp;
}

bool operator==(const ratio &a, const ratio &b) {
   return a.n == b.n and a.d == b.d;
}

bool operator!=(const ratio &a, const ratio &b) {
   return not (a == b);
}

int main() {
   ratio zero;
   ratio one(1);
   ratio two(2);
   ratio half(1, 2);
   ratio fourth(1, 4);
   assert(zero + one == one);
   assert(one * one == one);
   assert(zero + half == half);
   assert(one != two);
   assert(half * half == fourth);
   assert(half / two == fourth);
   assert(zero - one == -one);
   return 0;
}
