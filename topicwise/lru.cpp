/*
  The LRU cache is a hash map of keys and double linked nodes. The hash map
  makes the time of get() to be O(1). The list of double linked nodes make the
  nodes adding/removal operations O(1).
 */
#include <list>
#include <unordered_map>
#include <iostream>

using namespace std;

class LRUCache {
  list<int> dq;

  unordered_map<int, int> ma;
  int max_size;

public:
  LRUCache(int);
  void set(int x, int val);
  int get(int);
  void display();
};

LRUCache::LRUCache(int n)
{
  max_size = n;
}

int LRUCache::get(int x)
{
  if (ma.find(x) != ma.end()) {
    auto val = ma[x];
    dq.remove(x);
    dq.push_front(x);
    return val;
  }
  else
    return -1;
}

void LRUCache::set(int x, int val)
{
  if (ma.find(x) != ma.end()) {
    dq.remove(x);
    dq.push_front(x);
    ma[x] = val;
  } else {
    if (dq.size() == max_size) {
      int last = dq.back();
      dq.pop_back();
      ma.erase(last);
    }
    dq.push_front(x);
    ma[x] = val;
  }
}

void LRUCache::display()
{
  for (auto it = dq.begin(); it != dq.end(); it++) {
    cout << (*it) << '\n';
  }
}


int main()
{
  LRUCache ca(4);

  ca.set(1, 2);
  ca.set(3, 4);
  ca.set(5, 6);
  ca.set(7, 8);

  ca.display();

  cout << '\n' ;
  int val = ca.get(3);
  cout << val << '\n' ;
  cout << '\n' ;
  ca.display();
}
