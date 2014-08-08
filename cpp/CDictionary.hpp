
#ifndef __CDICTIONARY_HPP__
#define __CDICTIONARY_HPP__

#include "CTreeNode.hpp"

/**
 * class CDictionary                      
 */
class CDictionary{
protected:
  CTreeNode root;
public:

  /**
   * Default constructor
   */
  CDictionary ();

  /**
   * Destructor
   */
  ~CDictionary ();

  /**
   * Loads a dictrionary from a file
   * @param path The path of the dictionary file
   * @return True if everything whent ok. False otherwise
   */
  bool loadFromPath (std::string path);

  /**
   * Check a word in the dictionary
   * @param word The word to check
   */
  bool checkWord (std::string word) const;

  /**
   * Prints the tree
   */
  void printTree () const;

  /**
   * Finds all words with the given letters that fit in the given pattern
   * @param pattern The patter where the words have to fit in
   * @param letters The allowed letters
   */
  list <string> findWordsInPattern (string pattern, string letters) const;
};

#endif // __CDICTIONARY_HPP__
