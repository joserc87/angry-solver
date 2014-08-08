
#include "CTreeNode.hpp"
#include "common.h"
#include <cstring>
#include <iostream>

using namespace std;

/*************************************************************************************************/
/*************************************************************************************************/

CTreeNode::CTreeNode (){
  CTreeNode(0);
  value = 0;
  child = NULL;
  sibling = NULL;
  isAWord = false;
}

/**************************************************************************************************/
/**************************************************************************************************/

CTreeNode::CTreeNode (char val){
  value = val;
  child = NULL;
  sibling = NULL;
  isAWord = false;
}

/**************************************************************************************************/
/**************************************************************************************************/

CTreeNode::CTreeNode (const CTreeNode &cpy){
  cout << "using copy constructor!";
}

/**************************************************************************************************/
/**************************************************************************************************/
/**************************************************************************************************/

CTreeNode::~CTreeNode (){
  if (sibling != NULL)
    delete sibling;
  sibling = NULL;
  if (child != NULL)
    delete child;
  child = NULL;
}

/**************************************************************************************************/
/**************************************************************************************************/

void CTreeNode::addChild (CTreeNode *c){
  // Change the ending string with a child
  if (ending.length()>0){
    string endingCopy = ending;
    ending = "";
    this->addChild(this->createNewNodeFromString (endingCopy));
  }
  if (child == NULL){
    child = c;
  }else{
    CTreeNode *node = child;
    while (node->sibling!=NULL){
      node = node->sibling;
    }
    node->sibling = c;
  }
}

/**************************************************************************************************/
/**************************************************************************************************/

void CTreeNode::add (string s){
  // If the node is empty (if is the ROOT)
  if (value == 0){
    value = s [0];
    string substr;
    if (s.length()<=1)
      substr = "";
    else
      substr = s.substr(1, s.length()-1);
    ending = substr;
  }else if (value == s[0]){ // If the value is the same, add as a subnode..
    // Change the ending string with a child
    if (ending.length()>0){
      string endingCopy = ending;
      ending = "";
      this->isAWord=false;
      CTreeNode *ch = this->createNewNodeFromString (endingCopy);
      ch->isAWord = true;
      this->addChild(ch);
    }
    string substr;
    if (s.length()<=1){
      substr = "\0";
      isAWord = true;
    }else{
      substr = s.substr(1, s.length()-1);
    }
    if (this->child == NULL){
      CTreeNode *ch =this->createNewNodeFromString (substr); 
      ch->isAWord = true;
      this->addChild(ch);
    }else{
      this->child->add (substr);
    }
  }else if (sibling!=NULL){
    sibling->add (s);
  }else{
    sibling = this->createNewNodeFromString (s);
    sibling->isAWord = true;
  }
}

/**************************************************************************************************/
/**************************************************************************************************/

CTreeNode *CTreeNode::createNewNodeFromString (string s){
  CTreeNode *node = new CTreeNode;
  node->value = s [0];
  string substr;
  if (s.length()<=1)
    substr = "";
  else
    substr = s.substr(1, s.length()-1);
  node->ending = substr; // TODO: Check
  return node;
}

/**************************************************************************************************/
/**************************************************************************************************/

void CTreeNode::addChildFromString (string s){
  if (child == NULL){
    if (ending.length () == 0){
      value = s[0];
      ending = s.substr (1, s.length ()-1);
    }else{
      CTreeNode *node = createNewNodeFromString (ending);
      this->addChild (node);
      this->addChildFromString (s);
    }
  }else{
    CTreeNode *node = getChildFromChar (s [0]);
    if (node == NULL){
      CTreeNode *node = createNewNodeFromString (s);
      this->addChild (node);
    }else{
      node->addChildFromString (s.substr (1, s.length ()-1)); // TODO: Check
    }
  }
}

/**************************************************************************************************/
/**************************************************************************************************/

CTreeNode *CTreeNode::getChildFromChar (char c){
  CTreeNode *node = child;
  while (node != NULL && node->value != c){
    node = node->sibling;
  }
  return node;
}

/**************************************************************************************************/
/**************************************************************************************************/

/*bool CTreeNode::checkString (char *s){
  if (s==NULL)
    return false;
  int len = strlen (s);
  if (len==0)
    return true;
  // If is a real string, check recursive
  if (sibling != NULL && sibling->checkString(s)){
    return true;
  }
  CTreeNode *subNode = getChildFromChar (s [0]);
  if (subNode==NULL){
    if (s [0]!=value)
      return false;
    if (ending == string (s+1)){
      return true;
    }else{
      return false;
    }
  }else{
    return (subNode->checkString (s+1));
  }
}*/

/**************************************************************************************************/
/**************************************************************************************************/

bool CTreeNode::checkString (const char *s) const{
  if (s == NULL){
    return false;
  }
  int len = strlen (s);
  if (len == 1){
    if (s [0] == value){
      if (this->isAWord){
	return true;
      }else{
	return false;
      }
    }
  }
  if (len == 0){
    return true;
  }
  // If is a real string, check recursive
  if (s[0] != value){
    if (sibling != NULL){
      if (sibling->checkString(s)){
	return true;
      }else{
	return false;
      }
    }else{
      return false;
    }
  }
  if (child==NULL){
    return value == s[0] && ending == string (s+1);
  }else{
    bool suc = child->checkString (s+1);
    return suc;
  }
}

/**************************************************************************************************/
/**************************************************************************************************/
short firstCharInString (char value, const char *str){
  for (int i=0; i<strlen (str); i++){
    if (str [i] == value){
      return i;
    }
  }
  return -1;
}

bool characterInString (char value, const char *letters){
  if (firstCharInString (value, letters)>=0){
    return true;
  }else{
    return false;
  }
}

void removeCharFromString (char value, char *letters){
  short i = firstCharInString (value, letters);
  if (i>=0){
    letters [i] = EMPTY;
  }
}

void addCharToString (char value, char *letters){
  for (int i=0; i<strlen(letters); i++){
    if (letters [i] == EMPTY){
      letters [i] = value;
      break;
    }
  }
}

void CTreeNode::findWordsInPattern (const char *pattern, char *letters, list <string> &words, string word) const{
  // ALGORITHM
  // -- CASE the node is child and we found a word
  // If child==NULL
  //   If pattern.length == 0
  //     words += word
  //   Return
  // -- CASE the position is fixed:
  // If pattern [0] != " "
  //   If pattern [0] == value
  //     If value IN letters
  //       call son, with pattern++ and letters -= value
  //     Else
  //       Return
  //   Else
  //     call sibling with same pattern and letters
  // Else --- Case the position is free
  //   If value IN letters
  //     call children
  //   call sibling
  //   
  //
  // Check if "value" is in letters (and pattern [0]==" ") OR if pattern [0]==value
  // Otherwise, go to sibling.
  if (strlen (pattern) == 0){
    // Is the end, check if there is a child
    if (child == NULL || isAWord){
      words.push_back (word);
    }
    return;
  }else{
    if (pattern [0] == value){
      // Recursive
      string extendedWord = word;
      extendedWord+= value;
      child->findWordsInPattern (pattern+1, letters, words, extendedWord);
    }else if (pattern [0] == EMPTY){
      // Check if value is in "letters"
      characterInString (value, letters);
      // Remove value from letters
      removeCharFromString (value, letters);
      // Call child with pattern+1, letters-value, words, etc.
      string extendedWord = word;
      extendedWord+= value;
      child->findWordsInPattern(pattern+1, letters, words, word);
      // Add the letter again
      addCharToString (value, letters);
    }else{ // Is not empty, but pattern!=value
      // Call siblings
      sibling->findWordsInPattern(pattern, letters, words, word);
    }
  }
}



/**************************************************************************************************/
/**************************************************************************************************/

void CTreeNode::print(int depth) const{
  cout << value;
  if (ending.length()!=0){
    cout << "(" << ending << ")";
  }
  if (child!=NULL){
    child->print (depth+1);
  }
  if (sibling!=NULL){
    cout << endl;
    for (int i=0; i<depth; i++){
      cout << " ";
    }
    sibling->print(depth);
  }
}

/**************************************************************************************************/
/**************************************************************************************************/
