/**
 * @file CTreeNode
 */

#ifndef __CTREENODE_HPP__
#define __CTREENODE_HPP__

#include <string>
#include <list>

using namespace std;


/**
 * A node in the character tree. It simply contains a letter
 * plus the pointer for the tree structure
 */
class CTreeNode
{
protected:
  char value;
  std::string ending; // This string makes sense for the end of the word, so we dont have to store all characters as nodes when not needed
  bool isAWord; // This boolean indicates if the node represents a word. This is necesary due that not only the leaf nodes can be a word.
  CTreeNode *child;
  CTreeNode *sibling;

  CTreeNode *createNewNodeFromString (std::string s);
public:
  CTreeNode ();
  CTreeNode (char val);
  CTreeNode (const CTreeNode &cpy);
  ~CTreeNode ();
  
  void addChild (CTreeNode *c);
  void addChildFromString (std::string s);
  void add (std::string s);
  std::string getChildCharacters () const;
  /**
   * Retreive the child with character c, or null if there is no such a child
   */
  CTreeNode *getChildFromChar (char c);
  bool checkString (const char *s) const;
  void print(int depth) const;
  void findWordsInPattern (const char *pattern, char *letters, list <string> &words, string word) const;
};

#endif // __CTREENODE_HPP__
