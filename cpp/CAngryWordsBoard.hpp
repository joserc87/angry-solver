
#ifndef __CANGRYWORDSBOARD_HPP__
#define __CANGRYWORDSBOARD_HPP__

#include <string>
#include <list>
#include "CDictionary.hpp"
#include "common.h"

#define BOARD_WIDTH  15
#define BOARD_HEIGHT 15

using namespace std;

/**
 * An angry words board
 */
class CAngryWordsBoard
{
protected:
  char board [BOARD_HEIGHT][BOARD_WIDTH];
  unsigned int multipliers [BOARD_HEIGHT][BOARD_WIDTH];

  list<AngryWordsMove> findAllMovesIn (unsigned short row, unsigned short column, Direction direction, string myLetters, const CDictionary &dic);
  string getStringFromBoard (unsigned short row, unsigned short column, Direction direction);
  bool checkNeighbours (unsigned short row, unsigned short column, Direction direction, unsigned short length);
  short int calcScore (unsigned short row, unsigned short column, Direction direction, string word);
  AngryWordsMove maxMove(AngryWordsMove m1, AngryWordsMove m2);
  string getLettersUsed (string word, string pattern);
public:
  CAngryWordsBoard ();
  ~CAngryWordsBoard ();
  AngryWordsMove findBestMove (const CDictionary &dic, string myLetters);
  char elementAt (unsigned short i, unsigned short j);
};

#endif
