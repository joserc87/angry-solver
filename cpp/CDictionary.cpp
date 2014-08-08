
#include <iostream>
#include <fstream>
#include <string>
#include "CDictionary.hpp"
#include "common.h"

using namespace std;

/**************************************************************************************************/
/**************************************************************************************************/

CDictionary::CDictionary (){
  root = CTreeNode (' ');
}

/**************************************************************************************************/
/**************************************************************************************************/

CDictionary::~CDictionary (){

}

/**************************************************************************************************/
/**************************************************************************************************/

bool CDictionary::loadFromPath (string path){
  root = CTreeNode (' ');
  CTreeNode *node = new CTreeNode;
  ifstream fi;
  fi.open (path.c_str());
  string word;
  bool ok=false;
  if (fi){
    while (!fi.eof ()){
      fi >> word;
      node->add(word);
    }
    fi.close ();
    ok = true;
  }else{
    ok = false;
  }

  root.addChild (node);
  return ok;
}

/**************************************************************************************************/
/**************************************************************************************************/

bool CDictionary::checkWord (string word) const{
  string wordToCheck = string (" ")+word;
  return (root.checkString (wordToCheck.c_str ()));
}

/**************************************************************************************************/
/**************************************************************************************************/

void CDictionary::printTree () const{
  cout << "Tree:" << endl;
  root.print(0);
  cout << endl;
}

/**************************************************************************************************/
/**************************************************************************************************/

list <string> CDictionary::findWordsInPattern (string pattern, string letters) const{
  list <string> words;
  letters.append (" "); // In the tree, the first node is a space, so we need a space to form any word
  const char *patternConstCSTR = pattern.c_str ();
  const char *lettersConstCSTR = letters.c_str ();
  char patternCSTR [MAX_STRING];
  char lettersCSTR [MAX_STRING];
  strcpy (patternCSTR, patternConstCSTR);
  strcpy (lettersCSTR, lettersConstCSTR);

  // Get the words
  root.findWordsInPattern (patternCSTR, &lettersCSTR[0], words, "");
  return words;
}

/**************************************************************************************************/
/**************************************************************************************************/
