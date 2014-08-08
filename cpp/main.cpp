#include <iostream>
#include <fstream>
#include <list>
#include <string>

#include "CTreeNode.hpp"
#include "CDictionary.hpp"
#include "CAngryWordsBoard.hpp"
#include "common.h"

using namespace std;

/**************************************************************************************************/
/**************************************************************************************************/

int main (int argc, char *argv [])
{
  string path = "./Resources/spanish.txt";
  CDictionary dict;
  bool end = false;;
  dict.loadFromPath (path);
  
  if (argc == 1){
    cout << "System ready" << endl << endl;
    while (cout && !end){
      cout << "Word to check: ";
      string word;
      cin >> word;
      cout << "The word \"" << word << "\" is ";
      if (dict.checkWord (word)){
	cout << "correct";
      }else{
	cout << "not correct";
      }
      cout << endl;
    }
  }else{
    string word = argv [1];
    if (word == "run"){
      CAngryWordsBoard board;
      AngryWordsMove move = board.findBestMove (dict, "hlo");
      cout << "The best solution is " << move.word;
    }
    cout << "The word \"" << word << "\" is ";
    //if (checkWord (words, wordToFind)){
    if (dict.checkWord (word)){
      cout << "correct";
    }else{
      cout << "not correct";
    }
    cout << endl;
  }
}

/**************************************************************************************************/
/**************************************************************************************************/
